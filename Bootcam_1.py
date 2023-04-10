a = ("hello world")
b = ("aji raida malela sirajd")
print(a + b)

for x in "Banana":
    print(x)
    
c = "Hello world"
print(len(c))


#variable
nama = "Aji"
print(type(nama))

#many value for many variable
nama_saya, nama_teman = "html" , "css"
print(nama_teman)

#collection/list
teman = ["html", "css", "php"]
teman = list(("html", "css", "php"))
teman1, teman2, teman3 = teman
print(teman)

#print
print(nama, nama_saya, teman)
print(1+2)

#global variable
x="awesome"
def myfunc():
    print("python is " + x)

myfunc()
print("python is " + x)

#example
a = "hello , word!"
print(len(a))

#check string


#upper class
a = "Hello, word!"
# print(a.split("!"))

#1
def sum_int_or_str(a,b):
    return int(a) + int(b)

assert(sum_int_or_str(1, '2')) == 3

#2
def get_second_character(a):
    "get second character , if only 1 character return 0"
    if len(a) > 1:
        return a[1]
    else:
        return 0
assert(get_second_character("ab")) =="b"
assert(get_second_character("a")) == 0

#3
car = {
    'brand' : 'toyota',
    'year': 2022
}
assert(car['brand']) == 'toyota'

#4
cars = [
    {
        'brand': 'toyota'
    },
    {
        'brand' : 'honda',
        'products' : [
            'civic'
        ]
    }
]
assert (cars[1]['products'][0]) == 'civic'

#5
raw_cars = 'toyota,honda,indiacar'
assert(raw_cars.split(',')) == ['toyota', 'honda', 'indiacar']

raw_cars = raw_cars.upper()

assert(raw_cars.split(',')) == ['TOYOTA', 'HONDA', 'INDIACAR']

# raw_cars = 'toyota, honda, indiacar, indiacar, indiacar'
# raw_cars = raw_cars.split(',')
# raw_cars = set(raw_cars)
# raw_cars = list[raw_cars]
# assert(raw_cars) == ['toyota', 'honda', 'indiacar']

raw_cars = 'toyota, honda, indiacar, indiacar, indiacar'
raw_cars = raw_cars.split(',')
raw_cars = set(raw_cars)
raw_cars = len[raw_cars]
assert(raw_cars)  == 3