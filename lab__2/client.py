from email import header
import requests
import json


class Client():

    def registration(login, password, email):
        url = "http://127.0.0.1:8000/users/"

        payload = 'username=' + login + '&password=' + password + '&email=' + email
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        ret_requst = requests.request(
            "POST", url, headers=headers, data=payload)
        return ret_requst.text

    def login(username, password):
        url = "http://127.0.0.1:8000/auth/jwt/create"
        payload = 'username=' + username + '&password=' + password
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        ret_requst = requests.request(
            "POST", url, headers=headers, data=payload)
        data = json.loads(ret_requst.text)
        return data['access']

    def add_task(token, title, body):
        url = "http://127.0.0.1:8000/todo/"
        payload = 'title=' + title + '&body=' + body
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + token}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text

    def get_task_all(token):
        url = "http://127.0.0.1:8000/todo/"
        payload = ''
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + token}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text

    def get_task_title(token, title):
        response = Client.get_task_all(token)
        tasks = json.loads(response)
        response_mas = []
        for task in tasks:
            if task['title'] == title:
                response_mas.append(task)
        return response_mas

    def get_task_id(token, id):
        url = "http://127.0.0.1:8000/todo/" + str(id) + "/"
        payload = ''
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + token}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text

    def update_task_id(token, title, body, id):
        url = "http://127.0.0.1:8000/todo/" + str(id) + "/"
        payload = 'title=' + title + '&body=' + body
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + token}
        response = requests.request("PUT", url, headers=headers, data=payload)
        return response.text

    def update_task_title_body(token, title, title_new, body):
        response_task = Client.get_task_title(token, title)
        response = []
        for resp in response_task:
            if resp['title'] == title:
                response.append(Client.update_task_id(
                    token, title_new, body, resp['id']))
        return response

    def update_task_title(token, title, title_new):
        response_task = Client.get_task_title(token, title)
        response = []
        for resp in response_task:
            if resp['title'] == title:
                response.append(Client.update_task_id(
                    token, title_new, resp['body'], resp['id']))
        return response

    def update_task_body(token, title, body):
        response_task = Client.get_task_title(token, title)
        response = []
        for resp in response_task:
            if resp['title'] == title:
                response.append(Client.update_task_id(
                    token, title, body, resp['id']))
        return response

    def delete_task_id(token, id):
        url = "http://127.0.0.1:8000/todo/" + str(id) + "/"
        payload = ''
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + token}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        return response.text
    def delete_task_title(token, title):
        response_task = Client.get_task_title(token, title)
        response = []
        for resp in response_task:
            if resp['title'] == title:
                response.append(Client.delete_task_id(token, resp['id']))
        return response
