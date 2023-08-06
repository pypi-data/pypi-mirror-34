helper package to interface with required google api services. It is completely independent package for generic usage.

#### example-usage:
```python
from vedavaapi.google_helper.gsheets import GSheets
from vedavaapi.google_helper.gdrive import GDrive

credentials_file_path = 'path/to/credentials.json'
scopes = ['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/spreadsheets.readonly']

#get instance of GSheets helper class, from our credentials.
gsheets_helper = GSheets.from_creds_file(credentials_file_path, scopes)

#now use it to access data in our required valuesFormat with header row mapping, etc.
#we can provide only desired customized parameters in 'pargs' dictionary parameter. if no custom 'fields' are choosen in pargs, then all fields will be returned. if no range mentioned, all sheet values will be returned.
vakyas_sheet_values, statuscode = gsheets_helper.sheet_values_for(spreadsheet_id='someGooGleSheetId',sheet_id='Vakyas', pargs={'idType':'title', 'valuesFormat':'maps', 'fields':['Vakya_id', 'Tantrayukti_tag', 'Vakya'], 'range':'1:27'} )

#get instance of GDrive helper class, from our credentials.
gdrive_helper = GDrive.from_creds_file(credentials_file, scopes)

#now use it to retrieve spreadsheet files details in a google drive folder
list_of_files_in_folder, status_code = gdrive_helper.list_of_files_in_folder(folder_id='bJUyfjaitxkzsl_jagkkahajru2acd', mime_types=['application/vnd.google-apps.spreadsheet'], additional_pargs={'orderBy':'recency'})
```

above code just passes a credentials.json file and, get a GSheets/GDrive object. with these helper objects we query sheets/drive, etc, with their methods. But if we don't have credentials.json file(it represents owner's authorisation grant to our application), then we have to generate one from our application's client_secret.json file we get from google api console.(this client_secret.json is like id of our app.). in this case resource user, and application owner is same. we have to grant our app permission to access our files. for that fallow below. once credentials.json is there, no need of this.
```python
from vedavaapi.google_helper.oauth import Authorizer

authorizer = Authorizer(client_secret_path='path/to/client_secret.json', credentials_storage_path='path/to/credentials.json', scopes=['https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/spreadsheets.readonly'])

authorizer.authorize() #this will redirect us to web browser, and after completion of authorisation credentials will be stored at given path. we can use these credentials and start using helper packages like above.

```


