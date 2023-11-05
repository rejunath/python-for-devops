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
