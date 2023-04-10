# import datetime
# import math 

# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%d/%m/%Y"))


# x = datetime.datetime.now()
# # print(type(x))
# # print(x.year)
# print(datetime.strftime("%A"))

# import datetime
# x = datetime.datetime(2020, 5, 17)
# print(x.strftime("%d/%b/%Y"))


# arr_1 = [5, 78, 2, 0]

# assert(min(arr_1)) == 0
# assert(max(arr_1)) == 78
# assert(pow(5, 5)) == 3125


# x = 10
# try:
#   print(x)
# except:
#   print("An exception occurred")
  
  
# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")
  

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

#   try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# x = "234"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")


# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["name"])


# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)


# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))

# json.dumps(x, indent=4, separators=(". ", " = "))

# json.dumps(x, indent=4, sort_keys=True)


# f = open("demofile.txt")

# f = open("demofile.txt", "rt")

# f = open("demofile.txt", "r")
# print(f.read())

# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())

# f = open("demofile2.txt", "w")
# f.write("Now the file has more content!")
# f.close()

# f = open("demofile2.txt", "r")
# print(f.read())

# import os
# os.remove("demofile.txt")

# import os
# if os.path.exists("demofile2.txt"):
#   os.remove("demofile2.txt")
# else:
#   print("The file does not exist")
  
# import os
# os.rmdir("myfolder")

# import json

# f = open('./file_json.py')

# json_string = f.read()
# print(json_string)

# json_dict = json.loads(json_string)
# print(json_dict)
# print(type(json_dict))
# print(json_dict)['user, password']

# users = [
#     {
#         'user': 'aji@gmail.com',
#         'password': '333',
        
#     },
#     {
#        'user': 'aji@gmail.com',
#        'password': '333',
#     }
# ]

# json_string = json.dumps(users)

# f = open("./file_json.txt", "r")

