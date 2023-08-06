
from office_vibe.office_vibe import OfficeVibe

from middleware.components.providers.providers_list import PROVIDERS_LIST

class OfficeVibeBase(OfficeVibe):
    def download_raw_data_per_user(self, user):
        pass

    def __transform__(self, data, user):
        pass

    def __reverse_transform__(self, data, user):
        pass

    def upload_raw_data_per_user(self, user, data):
        pass

PROVIDERS_LIST.append(OfficeVibeBase)
