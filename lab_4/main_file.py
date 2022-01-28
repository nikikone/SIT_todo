from file_client import Files_client

path = 'C:/Users/Nikita/Desktop/file/procr.jpg' # Путь к файлу для загрузки на сервер
direct = 'C:/Users/Nikita/Desktop/file' # Путь к папке для сохранения файла с сервера

client_file = Files_client


print(client_file.get_files())
#print(client_file.post_file(path, "123"))
#print(client_file.delete_file("procr_FWMB0k8.jpg"))
#print(client_file.get_file_name("txt.txt", direct))