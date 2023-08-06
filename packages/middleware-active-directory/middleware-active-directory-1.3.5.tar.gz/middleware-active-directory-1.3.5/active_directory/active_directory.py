import io
import json
import urllib2

from ldap3 import MODIFY_REPLACE
from ldap3.core.exceptions import LDAPExceptionError, LDAPInvalidCredentialsResult
from tornado.options import options

from middleware.components.providers.base import BaseProvider, ACTIVE_DIRECTORY_USER_ID
from middleware.components.synchronization import AD_PICTURE_FIELD
from middleware.model import ActiveDirectoryUser

ACTIVE_DIRECTORY_SYSTEM_ID = '1'

class ActiveDirectory(BaseProvider):
    def __init__(self, sync_id):
        BaseProvider.__init__(self, ACTIVE_DIRECTORY_SYSTEM_ID, {}, sync_id)

    def download_raw_data_per_user(self, user):
        return json.loads(user["metadata"])

    def __transform__(self, data, user):
        for key, item in data.iteritems():
            if type(item) == list:
                data[key] = ' '.join(item).strip()
        return data

    def get_manager_dn(self, manager_full_name, user):
        try:
            db_user = ActiveDirectoryUser.get_manager(manager_full_name)
            return json.loads(db_user['metadata'])['distinguishedName']
        except Exception as e:
            self.log({"success": False,
                      "message": "Invalid manager name",
                      ACTIVE_DIRECTORY_USER_ID: user[ACTIVE_DIRECTORY_USER_ID],
                      "data_1": str(e)})
            return None

    def __reverse_transform__(self, data, user):
        result = {}
        for key, value in data.iteritems():
            if value:
                if isinstance(value, (list, tuple)):
                    result[key] = [(MODIFY_REPLACE, [str(v) for v in value])]
                else:
                    if key == 'manager':
                        value = self.get_manager_dn(value, user)
                        if not value:
                            continue
                    result[key] = [(MODIFY_REPLACE, [value])]
            elif key == 'thumbnailPhoto' and not value:
                continue
            else:
                result[key] = [(MODIFY_REPLACE, [])]
        return result

    def resize_picture(self, path):
        photo = urllib2.urlopen(path).read()
        from PIL import Image
        img = Image.open(io.BytesIO(photo)).convert('RGB')
        img.thumbnail((300, 300), Image.ANTIALIAS)
        output = io.BytesIO()
        img.save(output, format='JPEG')
        return output.getvalue()

    def update_profile_picture(self, data, connection, user, user_dn):
        operation = "add photo"
        user_id = user[ACTIVE_DIRECTORY_USER_ID]
        try:
            path = data.get(AD_PICTURE_FIELD)[0][1][0]
            hex_data = self.resize_picture(path)

            connection.modify(user_dn, {AD_PICTURE_FIELD: [(MODIFY_REPLACE, [hex_data])]})
            self.log({"success": True,
                      "message": "Photo updated",
                      "operation": operation,
                      ACTIVE_DIRECTORY_USER_ID: user_id,
                      "data_1": str(connection.result)})
        except Exception as e:
            self.log({"success": False,
                      "message": "Error in updating photo",
                      "data_1": str(e),
                      "operation": operation,
                      ACTIVE_DIRECTORY_USER_ID: user_id})

    def update_profile_if_possible(self, data, connection, user, user_dn):
        if data.get(AD_PICTURE_FIELD):
            try:
                self.update_profile_picture(data, connection, user, user_dn)
            finally:
                # picture was updated already, data[AD_PICTURE_FIELD] is link
                # Need to be removed before updating the rest of fields
                del data[AD_PICTURE_FIELD]

    def upload_raw_data_per_user(self, user, data):
        from ldap3 import Server, Connection, ALL
        s = Server(options.AD_server, get_info=ALL)
        connection = None
        try:
            connection = Connection(s, options.AD_admin, options.AD_password, auto_encode=True, check_names=True,
                                    auto_bind="NONE", version=3, authentication="SIMPLE",
                                    client_strategy="SYNC", auto_referrals=True, read_only=False,
                                    lazy=False, raise_exceptions=True)

            connection.open()
            connection.bind()
        except LDAPInvalidCredentialsResult as e:
            self.log({"success": False,
                      "message": "Invalid credentials",
                      "operation": "connection to AD server",
                      "data_1": str(e)})
            raise e
        except LDAPExceptionError as e:
            self.log({"success": False,
                      "message": "Socket Error",
                      "operation": "connection to AD server",
                      "data_1": str(e)})
            raise e
        else:
            if not data:
                self.log({"success": False,
                          "message": "no changes in modify request",
                          "operation": "update user",
                          ACTIVE_DIRECTORY_USER_ID: user[ACTIVE_DIRECTORY_USER_ID]})
            user_dn = json.loads(user['metadata'])['distinguishedName']
            self.update_profile_if_possible(data, connection, user, user_dn)

            connection.modify(user_dn, data)
            return connection.result
        finally:
            if connection:
                connection.unbind()
