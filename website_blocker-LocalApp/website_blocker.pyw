import time
from datetime import datetime as dt
import json

from cv2 import startWindowThread

hosts_temp = 'C:\\Users\\user\\Documents\\python_dir\\new_folder\\hosts'
hosts_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
redirects='127.0.0.3'

with open('times.json','r+') as file:
    data = json.load(file)
    start = data['start']
    end = data['end']


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,start) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end):
        with open('websites.txt','r') as file:
            website_list = file.readlines()
        print('working time...')
        with(open(hosts_path, 'r+')) as file:
            contents = file.readlines()
            contents=contents[0:21]
            for website in website_list:
                contents.append(redirects+' '+website)
            file.seek(0)
            file.truncate()
            for line in contents:
                file.write(line)
    else:
       with(open(hosts_path, 'r+')) as file:
            contents = file.readlines()
            contents=contents[0:21]
            file.seek(0)
            file.truncate()
            for line in contents:
                file.write(line)
            print('fun hours...')
    time.sleep(10)
