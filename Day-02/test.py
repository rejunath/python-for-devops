name="reju_nath"
age=28
print(name.split("_"))
print(name.split("_")[1].upper())
print(name.split("_")[0].upper()+" "+name.split("_")[1].upper())
print(len(name))
print(name[0].upper())
print(name[3:6])
##Formatting
print('%s %d' % (name,age)) 
txt1 = "My name is {fname}, I'm {old}".format(fname = name, old = age)        
print(txt1)
##reference for Reg expression : https://www.w3schools.com/python/python_regex.asp
##pattern r("") ---> r stands for regular expression
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connections: {max_connections}")
