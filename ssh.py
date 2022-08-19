from netmiko import ConnectHandler

SW = {
    'device_type' : 'aruba_os',
    'host' : '192.168.1.9',
    'username' : 'admin',
    'password' : 'aruba123'
}

net_connect = ConnectHandler(**SW)
net_connect.enable()
output = net_connect.send_command('show int 1/1/1')
print(output)

#Get state of interface
lines = output.split('\n')
loc = lines[2].find("Admin state")
state = lines[2][loc+15:]

if state == "up": 
    print("Interface 1/1/1 is working well")
else:
    print("Interface 1/1/1 is having problem")