from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_1
from examples import custom_style_2
from examples import custom_style_3
from pprint import pprint
from termcolor import colored
import os
import sys
import json


factocli_settings_path = "/opt/factocli/settings.json"

# {
#     "installed_factorio_directory": "", 
#     "installed_factorio_version": "", 
#     "installed_factorio_server_service_file_path": "", 
#     "installed_factorio_api_service_file_path": "", 
#     "factocli_directory_path": "/opt/factocli", 
#     "factocli_backups_directory_path": "/opt/factocli/factocli_backups",
#     "servers":{
        
#     }
# }


def write_to_json_settings(accesstoken,servertoken):
    with open(factocli_settings_path, 'r') as file:
        data = json.loads(file.read())
    #print(data)
    server_data = {
        "access-token": accesstoken,
        "server-token": servertoken,
    }
    # data['servers'].append(server_data)
    # with open(factocli_settings_path, 'w+') as file:
    #     json.dump(data,file)
    
    #print(json.dumps(data))


def ask_for_access_token_prompt():
    ask_for_access_token = [
        {
        'type': 'input',
        'name': 'access-token',
        'message': 'What\'s your access token?',
        }
    ]
    answer = prompt(ask_for_access_token, style=custom_style_2)
    return answer['access-token']
    
def ask_for_server_token_prompt():
    ask_for_server_token = [
        {
            'type': 'input',
            'name':'server-token',
            'message':'What\'s your server token?'
        }
    ]
    answer = prompt(ask_for_server_token, style=custom_style_2)
    return answer['server-token']


def check_if_there_are_servers():
    with open(factocli_settings_path, 'r') as file:
        data = json.loads(file.read())
    
    server_list = []
    if(data['servers'] != False):
        for each_server in data['servers']:
            server_list.append(each_server['server-name'])
        which_server_prompt = [
            {
                'type': 'list',
                'message': 'Which server do you wan\'t to activate',
                'name': 'which_server',
                'choices': server_list,
            }
        ]
        answer = prompt(which_server_prompt, style=custom_style_2)
        if(answer['which_server'] == None):
                print("Nothing selected. Please try again.")
        
        if(answer['which_server'] != None):
                ask_for_access_token        = ask_for_access_token_prompt()
                ask_for_server_token        = ask_for_server_token_prompt()
                
                if((ask_for_access_token != False) and (ask_for_server_token != False)):
                    print(ask_for_access_token)
                    print(ask_for_server_token)
                    
                    for each_server in data['servers']:
                        if(answer['which_server'] == each_server['server-name']):
                            each_server['access-token'] = ask_for_access_token
                            each_server['server-token'] = ask_for_server_token
                    
                    with open(factocli_settings_path, 'w') as file:
                        json.dump(data,file)
                    
                else:
                    print("Please provide a server and a access token provided by your factorioheadless.com dashboard")
    elif(data['servers'] == False):
        print("There were no servers found")



def main():
    
    print(colored("This will activate a server for factorioheadless.com", "cyan"))
    print(colored("You will need a acces token and a server token.", "cyan"))
    print(colored("You will need to make a server in your factorioheadless.com dashboard.", "cyan"))

    check_if_there_are_servers()


