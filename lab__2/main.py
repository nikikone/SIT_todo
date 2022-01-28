from client import Client

login = "api_register"
mail = "api_register_mail@gmail.com"
password = "X2mC1VYSxo"
task = "Task_test"
task_new = "Task_test_3.0"
body = "Body_test"
test = Client
token = test.login(login,password)
#print(test.registration(login, password, mail))
#print(test.add_task(token, task, body))
print(test.get_task_all(token))
#print(test.get_task_title(token, task))
#print(test.get_task_id(token, 10))
#print(test.update_task_id(token, task, body, 10))
#print(test.update_task_title_body(token, task, task_new, body))
#print(test.update_task_title(token, task, task_new))
#print(test.update_task_body(token, task, body))
#print(test.delete_task_id(token, 14))
#print(test.delete_task_title(token, task))