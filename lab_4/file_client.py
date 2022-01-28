import requests
import mimetypes
import os


class Files_client(object):

    def get_files():
        url = "http://127.0.0.1:8000/files/"
        response = requests.request("GET", url, headers={}, data={})
        return response.text

    def delete_file(name):
        url = "http://127.0.0.1:8000/files/"+name
        response = requests.request(
            "DELETE", url, headers={}, data={})
        return response.text

    def post_file(url_name, remark):
        url = "http://127.0.0.1:8000/files/"
        payload = {
            'remark': str(remark)
        }
        file_type = mimetypes.guess_type(url_name)
        file_name = os.path.basename(url_name)
        files = [
            ('file', (file_name, open(url_name, 'rb'), file_type[0]))
        ]

        response = requests.request(
            "POST", url, headers={}, data=payload, files=files)
        return response.text

    def get_file_name(name, dir): #Скачивание файла с сервера
        url = "http://127.0.0.1:8000/files/" + name
        response = requests.request("GET", url, headers={}, data={})
        if response.status_code == 200:
            with open(dir + '/' + name, "wb") as f:
                f.write(response.content)
            resp = "File saved"
        else:
            resp = "The specified file does not exist on the server"
        return resp


# import requests

# url = "http://127.0.0.1:8000/file/postman-logo-0087CA0D15-seeklogo.com.png"

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
