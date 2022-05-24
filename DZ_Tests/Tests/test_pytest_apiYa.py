from urllib import response
import pytest
import requests

token = 'AQAAAAAWC2sDAADLW0SVBXklZ0hIh-Eo0UNuDZw'

class TestSomething:    
    disk_file_path = 'Test'
    def setup(self):
        print("method setup")


    def teardown(self):
        print("method teardown")


    def test_create_folder_disk(self):
        '''
        Проверяем, что код ответа сервера = 201,
        т.е. запрос на создание папки успешен.
        '''
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }
        params = {"path": self.disk_file_path}

        response = requests.put(upload_url, headers=headers, params=params)
        assert response.status_code == 201



    def test_get_presenc_downloaded_folder(self):
        '''
        Проверяем, что папка есть на диске.
        '''
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }
        params = {"path": self.disk_file_path}
        response = requests.get(upload_url,  headers=headers, params=params)
        response_body = response.json()
        assert response_body['name'] == 'Test'


    def test_folder_already_disk(self):
        '''
        Проверяем, что папка с заданным именем уже существует
        '''
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }
        params = {"path": self.disk_file_path}

        response = requests.put(upload_url, headers=headers, params=params)
        assert response.status_code == 409

if __name__ == '__main__':
    pytest.main()