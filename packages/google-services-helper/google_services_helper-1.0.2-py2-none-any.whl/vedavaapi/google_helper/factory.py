from .oauth import creds_helper
from .gsheets import helper as gsheets_helper
from .gdrive import helper as gdrive_helper


class GServices(object):

    def __init__(self, credentials):
        '''
        initializes gservices with credentials
        :param credentials: credentials
        '''
        self.__services = {}
        self.__credentials = credentials

    @classmethod
    def from_creds_file(cls, creds_path, scopes, auth_through_service_account=False):
        '''
        :param creds_path: path to credentials file
        :param scopes: scopes to be enabled
        :param auth_through_service_account: are credentials are of service_account?
        '''
        credentials = creds_helper.credentials_from_file(creds_path, scopes, auth_through_service_account=auth_through_service_account)
        return cls(credentials)

    @classmethod
    def from_creds_string(cls, creds_string, scopes, auth_through_service_account=False):
        credentials = creds_helper.credentials_from_string(creds_string, scopes, auth_through_service_account=auth_through_service_account)
        return cls(credentials)

    def __init_gdrive(self, force=False, **kwargs):
        if 'drive' in self.__services and self.__services.get('drive', None) is not None:
            if not force:
                return

        try:
            gdrive_discovery_service = gdrive_helper.build_service(self.__credentials)
        except Exception as e:
            raise e
        if gdrive_discovery_service is None:
            raise RuntimeError('cannot instantiate gdrive_discovery_service')
        self.__services['drive'] = gdrive_helper.GDrive(gdrive_discovery_service, **kwargs)

    def __init_gsheets(self, force=False, enable_drive_service_linking=False, **kwargs):
        if 'sheets' in self.__services and self.__services.get('sheets', None) is not None:
            if not force:
                return

        if enable_drive_service_linking:
            self.__init_gdrive(force=False, **kwargs)

        try:
            gsheets_discovery_service = gsheets_helper.build_service(self.__credentials)
        except Exception as e:
            raise e
        if gsheets_discovery_service is None:
            raise RuntimeError('cannot instantiate gsheets_discovery_service')
        self.__services['sheets'] = gsheets_helper.GSheets(gsheets_discovery_service, drive_service=self.__services.get("drive", None), **kwargs) if enable_drive_service_linking else gsheets_helper.GSheets(gsheets_discovery_service, **kwargs)


    def gdrive(self, refresh=False, **kwargs):
        self.__init_gdrive(force=refresh, **kwargs)
        return self.__services['drive']


    def gsheets(self, refresh=False, enable_drive_service_linking=False, **kwargs):
        self.__init_gsheets(force=refresh, enable_drive_service_linking=enable_drive_service_linking, **kwargs)
        return self.__services['sheets']
