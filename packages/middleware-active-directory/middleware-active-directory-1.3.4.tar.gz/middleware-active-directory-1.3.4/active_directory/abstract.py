
from active_directory.active_directory import ActiveDirectory

from middleware.components.providers.providers_list import PROVIDERS_LIST

class ActiveDirectoryBase(ActiveDirectory):
    pass

PROVIDERS_LIST.append(ActiveDirectoryBase)
