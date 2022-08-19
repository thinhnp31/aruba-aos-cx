
from urllib import request
from urllib3.exceptions import InsecureRequestWarning
import requests
import json
import re

DEVICE_IP = "192.168.1.9"

URL = 'https://' + DEVICE_IP +  '/rest/v10.04'

ACCOUNT = {
            'username' : 'admin',
            'password' : 'aruba123'
        }

#Logout
def logout():
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = requests.post(
    URL + '/logout',
    verify=False,
    cookies=cookies
    )  
    print("Logout : " + str(response.status_code))

#Login
def login():
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = requests.post(
    URL + '/login',
    params = ACCOUNT,
    verify=False
    )
    print("Login : " + str(response.status_code))
    return response.cookies.get_dict()

#Show vlan list
def show_vlans():
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = requests.get(
    URL + '/system/vlans',
    verify=False,
    cookies=cookies
    )
    print(response.status_code)
    return json.loads(response.content.decode("utf-8"))

#Show vlan 
def check_vlan(id):
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = requests.get(
    URL + '/system/vlans/' + str(id),
    verify=False,
    cookies=cookies
    )
    print(response.status_code)
    if response.status_code == '200':
        return "There is VLAN " + str(id) + " on the switch"
    else:  
        return "VLAN " + str(id) + " does not exist"

#Create vlan
def create_vlan(id, name):
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    vlan = {
        "id" : id,
        "name" : name
    }
    response = requests.post(
      URL + '/system/vlans',
      verify=False,
      cookies=cookies,
      data = json.dumps(vlan, indent=4)
    )

    print(response.status_code)
    if str(response.status_code)[1] == "2":
        return "VLAN " + str(id) + " is created successfully"
    else:  
        return response.text

#Delete vlan
def delete_vlan(id):
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = requests.delete(
      URL + '/system/vlans/' + str(id),
      verify=False,
      cookies=cookies
    )

    print(response.status_code)
    if str(response.status_code)[0] == "2":
        return "VLAN " + str(id) + " is deleted successfully"
    else:  
        return response.text

#Get One interface
def get_interface(name):
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = requests.get(
    URL + '/system/interfaces/' + str(name).replace("/","%2F"),
    verify=False,
    cookies=cookies
    )
    print(response.status_code)
    return response

#############
# MAIN CODE #
#############

cookies = login()

print(get_interface('1/1/1').json()['admin_state'])

logout()
