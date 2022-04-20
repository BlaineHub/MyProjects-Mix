
from email.headerregistry import ContentTransferEncodingHeader


hosts_temp = 'C:\\Users\\user\\Documents\\python_dir\\new_folder\\hosts'
with open('websites.txt','r') as file:
    website_list = file.readlines()
redirects='127.0.0.3'

with(open(hosts_temp, 'r+')) as file:
    contents = file.readlines()
    contents=contents[0:21]
    for website in website_list:
        print(website)
        
print(website_list)