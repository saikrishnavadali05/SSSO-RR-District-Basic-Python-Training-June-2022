1. Write a program to build a calculator. The calculator should be able to read 4 numbers and print the addition and multiplication of ONLY THE EVEN numbers using functions. You can follow these steps -
	a) Create different python files - add.py, multiple.py and write functions for these operations.
	b) main.py file should call the above functions based on the inputs provided. For example, input 'add 1,2,3,4'  should call add.py 
	'multiply 1,2,3,4'  should call multiply.py
	c) If there are less than 4 numbers provided, the code should be able to handle the error and throw relevant message to the user.
	d) All the 4 numbers should be taken up with input() method.
	e) If no even number is there among the 4 numbers, it should throw relevant message to the user.
	f) Save the program output into a text file output.txt  


 
a=25
b=34
c=38
d=50
def calculator(a,b,c,d):
    return a+b+c+d
    
result=a+b+c+d
print("addition :",calculator(a,b,c,d))   # addition : 1503

def multiple(a,b,c,d):
    return a*b*c*d
    
result=a*b*c*d
print("multiple :",multiple(a,b,c,d))  #multiple : 17433292888  

a=888
b=500
c=485
d=344
result=10
def add(m,n,o,p):
    print("addition is:",m+n+o+p)      
    import Exam
Exam.add(25,45,56,34)       #  addition is: 160  
def mul(m,n,o,p):
    print("multiplication is:",m*n*o*p)
    import Exam 
Exam.mul(23,30,45,62)       #multiplication is:1925100    

#2Write a program to calculate number of days, hours, minutes, seconds to the birthday of Sri Sathya Sai Baba from the current timestamp(Birthday is on 23-November). 
	a) Use datetime module. 
	b) Calculate using datetime, the difference in days, hours, minutes, seconds from the current timestamp. For birthday, you can consider date as 23-11-2022 00:00:00
	c) Print the output in following format - "Current timestamp is "XXXXXXXXX" and "Countdown for the birthday is xx days, xx hours, xx minutes, xx seconds"
	d) Also, create a program to read input date in DDMMYYYY format. And calculate number of days to birthday.
	e) The program must also  handle the errors. For eg., if date given is 20-May-2022, the program must throw error and send message to user - 'The date format provided is invalid. Please provide input in DDMMYYYY format' 
	f) The program must also be able to handle future dates greater than 23112022 and throw a message to the user to input a date less than 23112022.

#a.data module
from datetime import date
from datetime import timedelta
today = date.today()
print("Today is: ", today)     #Today is:  2022-07-24
yesterday = today - timedelta(days = 1)
print("Yesterday was: ", yesterday)    #Yesterday was:  2022-07-23

# time module
import time
cur_time = time.localtime()
cur_clock = time.strftime("%H:%M:%S", cur_time)

print(cur_clock)      #16:02:42




