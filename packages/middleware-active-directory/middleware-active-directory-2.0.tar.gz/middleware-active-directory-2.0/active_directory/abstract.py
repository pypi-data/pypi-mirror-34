
from active_directory.active_directory import ActiveDirectory

class ActiveDirectoryBase(ActiveDirectory):
    def download_raw_data_per_user(self, user):
        pass

    def __transform__(self, data, user):
        pass

    def __reverse_transform__(self, data, user):
        pass

    def upload_raw_data_per_user(self, user, data):
        pass


