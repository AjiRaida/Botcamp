import time 
import math

def calculate_time(func):
    
    
    def inner1(*args, **kawrgs):
        
        
        
        begin = time.time()
        
        
        
        func(*args, *args, **kawrgs)
        
        
        
        end = time.time()
        print("total time taken in : ", func,__name__, end - begin)
        
        return inner1
    
    @calculate_time
    def factorial(num):
        
        time.sleep(2)
        print(math.factorial(num))
        
    factorial(10)