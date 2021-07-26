#Задача №1

import requests
# TOKEN = "2619421814940190"
request_url = "https://superheroapi.com/api/2619421814940190/search/"
super_heroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

for super_hero in super_heroes:
    super_hero_r = requests.get(request_url + super_hero['name'])
    super_hero['intelligence'] = int(super_hero_r.json()['results'][0]['powerstats']['intelligence'])

sorted_super_heroes = (sorted(super_heroes, key=lambda hero: hero['intelligence'])[0]['name'])

print(sorted_super_heroes)

# #Задача № 2
# токен не публикую
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headrs (self):
        return {'Content-type': 'application/json', 'Authorization': 'QAuth {}'}

"""Метод загруджает файлы по списку file_list на яндекс диск"""

def upload(self, yadisk_file_path):
        files_url = 'http://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headrs()
        params = {'path': yadisk_file_path, 'overwrite': 'true'}
        answer = requests.get(files_url, headers=headers, params=params)
        return answer.json()

def upload_file_to_disk(self,yadisk_file_path,filename):
        href = self.upload(yadisk_file_path=yadisk_file_path).get('href','')
        answer = requests.put(href, data=open(filename, 'rb'))
        answer.raise_for_status()
        if answer.status_code == 201:
            print('Файл успешно загружен на диск')
        else:
            print('Что-то пошло не так')


if __name__ == '__main__':
    uploader = YaUploader('c:\my_folder\file.txt')
    result = uploader.upload()