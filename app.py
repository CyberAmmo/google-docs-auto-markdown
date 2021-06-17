from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
doc_id = '1GRB9QPPMGwZcJK7D3GpXuuKSMB9_tLJAmMALZfu_4uI'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/documents',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('docs', 'v1', http = httpAuth)

# Пример чтения файла
# values = service.documents().get(
#     documentId=doc_id,
# ).execute()
# pprint(values)

# Пример записи в файл
values = service.documents().batchUpdate(
    documentId=doc_id,
    body={
        "data": [
         {
            'insertText': {
                'location': {
                    'index': 25,
                },
                'text': 'text1'
            }
        },
                 {
            'insertText': {
                'location': {
                    'index': 50,
                },
                'text': 'text2'
            }
        },
                 {
            'insertText': {
                'location': {
                    'index': 75,
                },
                'text': 'text3'
            }
        },
    ]
    }
).execute()