#Q1.
name = ''' Hi How are you?

 Starterd learning python.

It's really interesting.'''
# # Then what is the output of following code
print(name[:]) #everything from start to endprint(name[-10:-5]) #from last 10Th index to last Fifth num
print(name[3:12])
print(name[12:3]) #empty string as never start from upper index
print(name[5:6])
print(name[-4:-12]) # always moves left to right so start >end 
print(name[::2])# in steps count the elements while considering last counted index
print(name[::-2])


#Q2
L1 = ['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
print(L1[:]) 
print(L1[::3])
print(L1[::-2])
print(L1.index('Happy')-len(L1)) #if we want negative index then subtract len from positive index 
print(type(L1[4]))#check type of data in list at 4th position
print(L1[L1.index(100)],L1[L1.index(300)],L1[L1.index(400)])#Extract values for 100, 300, 400



#Q3
l2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, "Success"] 
print(l2[4])
print(l2[1:5])
print(l2[7])
print(l2[7][2])
print(l2[7][2:])
print(l2[ : 3])
print(l2[3:])

#4.	From the above l2 value ‘b’ must be changed to ‘BEE’
l2[4][1]='BEE'
print(l2)

#Q5.From l2 “BEE” has to discard.
l2[4].remove('BEE')
print(l2)

#Q6 6.	In l2 add a dictionary at the end {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}
l2.append({'insect': ['bee', 'moth'] , 'bird' : ['parrot', 'sparrow']})
print(l2)

#Q7.	From l2 extract insect information.
print(l2[-1]['insect'])

#Q8. Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of l2
d1 = {'a': 10, 'b': 20, 'c': 30}
l2.insert(1, d1)

# # 9. Based on new l2 created here extract the value 10 from l2 dictionary.
value = l2[1]['a']
print(value)


#10.If l2 =[1,2,3,5, (90,40,50,10), ‘Python’, 400 ,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”, (200,300, “Hundreds”)] then what is the output of following
l3=[1,2,3,5, (90,40,50,10), 'Python', 400 ,['a', 'b', 'work hard'],100 , 200, "Success", (200,300, "Hundreds")] 
print(l3[4][2])
print(l3[5][:])
print(l3[2:])
print(l3[1:5])
print(l3[5])
print(l3[5][3:-1])
print(l3[-1])
print(l3[-4:-3])
print(l3[-4:-10])
print(l3[7][2])
print(l3[-7][2:])
print(l3[ :- 3])
print(l3[ 3:])

'''11. Ask user to enter the marks and define if the user got distinction, first class, second class, pass, Fails
If marks are more than 80 output must be “You got distinction”
For marks more than 60 output must be “You got First class”
Marks more than 40 will display “You got second class”
Marks more than or equal to 35 “PASS” Otherwise Fail  '''

try:
    marks = int(input("Enter your marks: "))


    if marks < 0 or marks > 100:
        print("Invalid input: marks should be between 0 and 100")

    elif marks > 80:
        print("You got Distinction")

    elif marks > 60:
        print("You got First class")

    elif marks > 40:
        print("You got Second class")

    elif marks >= 35:
        print("PASS")

    else:
        print("Fail")

except ValueError:
    print("Invalid input: please enter numeric marks only")

'''12. Ask user to enter information about salary of the employee per year and rating received as A, B, C, D

If salary upto 5 lpa then increament based on ratings are A = 16% , B=12%, C= 10%, D=6%

If salary upto 10 lpa then increament based on ratings are A = 14% , B=10%, C= 8%, D=6%

If salary upto 15 lpa then increament based on ratings are A = 8% , B=6%, C= 4%, D = no increment

If salary upto 23 lpa then increament based on ratings are A = 7% , B=5%, C= 4%, D=no'''

salary=("enter your salary");
ratings=("Enter your ratings 'A,B,C,D' ")
if salary<=500000 :
    if ratings=='A':
       salary=salary*1.16
       print(salary)
    elif ratings=='B':
        salary=salary*1.12
        print(salary)
    elif ratings=='C':
        salary=salary*1.10
        print(salary)
    else:
        salary=salary*0.6
        print(f"your salary is {salary}")
elif salary<=1000000 :
    if ratings=='A':
       salary=salary*1.16
       print(salary)
    elif ratings=='B':
        salary=salary*1.10
        print(salary)
    elif ratings=='C':
        salary=salary*1.08
        print(salary)
    else:
        salary=salary*0.6
        print(f"your salary is {salary}")       
elif salary<=1500000 :
    if ratings=='A':
       salary=salary*1.08
       print(salary)
    elif ratings=='B':
        salary=salary*1.06
        print(salary)
    elif ratings=='C':
        salary=salary*1.04
        print(salary)
    else:
        print(f"there is no increment,your salary is {salary}")
else:
    if ratings=='A':
       salary=salary*1.07
       print(salary)
    elif ratings=='B':
        salary=salary*1.05
        print(salary)
    elif ratings=='C':
        salary=salary*1.04
        print(salary)
    else:
        print(f"there is no increment,your salary is {salary}")                    

# 13.	Ask user to opt for courses for master degree based on the following  
# L1 = [“HR”, “Finance”, “Marketing”, “DS”]
# Based on above subject there are two different streams. For example- HR is having HR core and HR analytics and Marketing is having core and Marketing analytics. Analytics is the optional subject and having added extra fees. DS is not having analytics.
# If fees for L1 is 2 lakhs for each course core subject having the same fees but analytics subject having 10% extra on 2 lakhs.
# If student opts for hostel then 2 lakhs per year is added. For food monthly 2000 .
# # Transportation charges 13000 per semester. Calculate the total annual cost based on selected service.  
# User will enter values as subject, analytics(Y/N), Hostel (Y/N), food(How many months?), Transportation(semester/annual)

# Sol'n:-
class MastersCourse:
    def __init__(self,subject,analytics,hostel,food_months,transport_type):
        self.subject = subject
        self.analytics = analytics.upper()
        self.hostel = hostel.upper()
        self.food_months = food_months
        self.transport_type = transport_type.lower()
        self.base_fee = 200000

    def course_fee(self):
        fee = self.base_fee

        if self.analytics == 'Y' and self.subject in ["HR","Finance","Marketing"]:
            fee += self.base_fee*0.10

        return fee
    
                
    def hostel_fee(self):
        if self.hostel == "Y":
            return 200000
        return 0
    
    def food_fee(self):
        return self.food_months *2000
    
    def transport_fee(self):
        if self.transport_type == "semester":
            return 13000*2
        elif self.transport_type == "annual":
            return 13000
        return 0
    
    def total_annual_cost(self):
        return(
            self.course_fee()
            + self.hostel_fee()
            + self.food_fee()
            + self.transport_fee()
        )

subject = input("Enter subject (HR/Finance/Marketing?DS): ")
analytics = input("Do you want analytics? (Y/N): ")
hostel = input("Do you want hostel ? (Y/N): ")
food_months = input(input("Enter number of months for food: "))
transport = input("Transportion type (semester/annual: )")

student = MastersCourse(subject,analytics,hostel,food_months,transport)

print("Course Fee: ",student.course_fee())
print("Hostel Fee: ",student.hostel_fee())
print("Food Fee: ",student.food_fee())
print("Transport Fee: ",student.transport_fee())
print("Total Annual Cost: ",student.total_annual_cost())

#14.
class BookAlloment:
    def __init__(self,standard,notebooks,pages):
        self.standard = standard
        self.notebooks  = notebooks
        self.pages = pages


        self.book_price ={"Hindi":[60,100,150],
                          "Marathi":[60,100,150],
                          "English":[80,100,150],
                          "Science":[90,120,200],
                          "Maths": [100,140,250],}
        self.notebooks_prices = {
            "square": [40,70],
            "4lines":[30,50],
            "2lines":[30,50],
            "single lines": [60,100],
            "A4 notebook": [100,180],
        }
        
    def get_standard_index(self):
        if self.standard in ["1st","2nd","3rd","4th"]:
            return 0
        elif self.standard in ["5th","6th","7th","8th"]:
            return 1
        elif self.standard in ["9th","10th"]:
             return 2
        else:
            return -1
        
    def calculate_books_cost(self):
        index = self.get_standard_index()
        if index == -1:
            return 0
        
        total = 0
        for price in self.book_price.values():
            total += price[index]
        return total
    
    def calculate_notebook_cost(self):
        page_index = 0 if self.pages == 100 else 1

        total = 0
        for nb in self.notebooks:
            total += self.notebooks_prices[nb][page_index]
        return total
    
    def total_cost(self):
        return self.calculate_books_cost() + self.calculate_notebook_cost()
    

standard = input("Enter standard (1st–10th): ")

n = int(input("How many notebook types do you want? "))
notebooks = []
for _ in range(n):
    nb = input("Enter notebook type (square/4lines/2lines/single lines/A4 notebook): ")
    notebooks.append(nb)

pages = int(input("Enter pages (100 or 200): "))

student = BookAlloment(standard, notebooks, pages)

print("Total Books Cost:", student.calculate_books_cost())
print("Total Notebook Cost:", student.calculate_notebook_cost())
print("Total Amount to Pay:", student.total_cost())

#16.
string = """In most organized forms of writing, such as essays, paragraphs contain a topic sentence. 
This topic sentence of the paragraph tells the reader what the paragraph will be about.
Essays usually have multiple paragraphs that make claims to support a thesis statement,
which is the central idea of the essay.  """                   


#17.Create
a=100 
#Convert a to string 
print(type(str(a)))
print(type(a))
#Convert a to list  
#print(list(a))#int is not iterable
# print(type(a))  
# Convert a to tuple 
print(tuple(a))
print(type(a))  
# Convert a to dict 
print(dict(a))
print(type(a)) 
#Convert a to set 
print(set(a))
print(type(a)) 
#Convert to float
print(float(a))
print(type(a))  
# Observe the errors and note it down for all conversions. 

#Q18
city = "Pune"
# Convert to int  
print(int(city))  #int()with base 10 : 
# Convert float
print(float(city)) 
# # #Convert list  
print(list(city))#->['p','u','n','e']
# # #Convert tuple 
print(tuple(city))#->('p','u','n','e')
# # #Convert dict
print(dict(city)) 
# Convert set 
print(set(city))#->{'p','u','n','e'}
# # #Obsert errors and note it down for all conversions 

#19.	Create a list as 
marks = [20,18,15,17,18] 
# # #Convert to int 
int(marks)
print(type)
# Convert float 
# Convert list 
# Convert tuple 
a=tuple(marks)
print(type(a))
# Convert dict 
b=dict(marks)
print(type(b))
# Convert set 
print(type(set(marks)))
# # # •	observe : errors and note it down for all conversions 

#Q20.Create the empty list snames 
sname=[]
#  Add value 20 in the list using append 
sname.append(20)
print(sname)
# Add values in the list using append 
sname.extend([30])
print(sname)
# •	Add value “WORK" in the list using extend 
sname.extend("WORK")
print(sname)


#Q21
newlist=[1,'a','b',2 , 3] 
#Add sname to combo using addition operator 
combo=sname+newlist
print(combo)
#Add combo to snames using append 
sname.append(combo)
#Add combo to snames using extend. 
sname.extend(combo)


#Q22
#11.Create one list l1 having two elements and l3 having 7 elements. Now at 4th position add l1 
l1=[1,2]
l3=[46,87,90,7654,32,987,4332,246]
print(l3)
l3[3]=l1
print(l3)

#Q23.Collection is the list having values [1,2,3,[‘a’, ‘b’, ‘c’], 100, ‘Nisha’, 20.50, 90.10 ] if the data is in integer or float then multiply with 5.  
collection= [1,2,3,['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10 ] 
collectionlist=[]
print(collection)
for i in collection:
    if type(i)==int or type(i)==float:
        i=i*5
        collectionlist.append(i)
    else:
        i=i
        collectionlist.append(i)
        print(collectionlist)  
# From the collection delete the record for “Nisha” 
collection.remove('Nisha')
print(collection)
#Find the location of 20.50 
print(collection.index(20.50))

#24.Create a comprehensive list for square upto 10 
squarelist=[x*x for x in range(1,11)]
print(squarelist)

#25.	Create the comprehensive list to find number divisible by 13 till 200
divideby13=[i for i in range(1,201)if i%13==0 ]
print(divideby13)


#26.Create the list which is divisible by 4 from 300 to 400 
divideby4=[i for i in range(300,401)if i%4==0 ]
print(divideby4) 

#27.Create a comprehensive list to generate list up to x, y as a number. For example if x = 3 list will be x_list = [0,1,2] and y=2 then y_list =[0,1]
x=int(input("enter the length of x-length"))
y=int(input("enter the length of y-length"))
x_list=[]
for i in range(x):
    x_list.append(i)
    print(x_list)  
y_list=[]
for i in range(y):
   y_list.append(i)
   print(y_list) 


#28.Then generate a new list based on all combination of x and y.
# # # # For example: if x = 1 and y =2  then x_list = [0] and y_list = [0,1]
# # # # And output will be [[0,0],[0,1]]
# If x=2 and y = 2 then output will be [[0,0],[0,1][1,0],[1,1]]
result=[]
for i in (x_list):
    for j in (y_list):
       result.append([i,j])
print(result)

# # # #23.Create l2 as a list and perform set operation on s1 with l1 

#Q35.Ask user to enter the name and DOB and generate the password based on first name 4 characters 
# and  @ddmm. For example name = SURESH and DOB = 05-05-1978 then password will be SURE@0505 
user=input("enter user name")
dob=input("enter dob dd-mm-yyyy")
password=user[:5]+'@'+dob[:5:2]
print(password)

#36.	Create the format mentioned here.
# *
# * *
# * * *
# * * * *
for i in range(5):
    print("*"*i)

# 37.	Create the format as mentioned below:
# ****
# ***
# **
# *
n=5
for i in range(5):
    print("*"*(n-i))

# 38.	Str_val = “ABCD” then create the format as mentioned below:
# A
# A B
# A B C
# A B C D
str_val="ABCD"
triangle_val=""
for i in range(len(str_val)):
    triangle_val=triangle_val+" "+str_val[i]
    print(triangle_val)

#Q39.
# A
# BB
# CCC
# DDDD

i=1
while i< len(str_val):
   print(str_val[i-1]*i)
   i +=1


#Q40.
# 1
# 22
# 333
# 4444

n = 4  
for i in range(1, n + 1):
    print(str(i) * i)



#Q 41.	Val = “ABCD”  based on the Val, create the format mentioned below
# D
# DC
# DCB
# DCBA
s = "ABCD"

for i in range(len(s)-1, -1, -1):
    print(s[len(s)-1:i-1:-1])




class LowBalanceError(Exception):
    pass

try:
    balance = 1000
    withdraw = 5000

    if withdraw > balance:
        raise LowBalanceError("Not enough balance")

except LowBalanceError as e:
    print(e)

#47.Create a function to accept marks from user utilize exception concept to validate proper marks.
def properMarks():
    while True:
        try:
            marks=int(input("enter your marks"))
            if marks<=0 or marks>100:
                    raise  ValueError("value must be in  between(1-100)")
            
            return marks
        except ValueError as e :
                    print("value error",e)
                    print("try again...")

properMarks()    

# 48.	Create a function to validate user first name/last name. 
# User first name/last name should contain only characters. No special characters, numbers, space in name 

def  credentials():
    try:
        first_name=input("enter first name")
        last_name=input("enter last name ")

        if  not first_name.isalpha():
            raise ValueError("invaild name")
        if not last_name.isalpha() :
            raise ValueError("invaild name")
    except ValueError as e :
            print("name should contain letters only",e)
            return None
    else:
           return first_name,last_name
          
    finally:
          print("code executed successfully")
             

result=credentials()
print(result)


# # def student_data():
# #     students = {}

# #     try:
# #         n = int(input("Enter number of students: "))
# #     except ValueError:
# #         print("Please enter valid number")
# #         return

# #     for i in range(n):
# #         while True:
# #             try:
# #                 name = input("Enter student name: ")

# #                 if not name.isalpha():
# #                     raise ValueError("Name must contain only letters")

# #                 marks = int(input("Enter marks (0-100): "))

# #                 if marks < 0 or marks > 100:
# #                     raise ValueError("Marks must be between 0 and 100")

# #                 if name in students:
# #                     raise ValueError("Student already exists")

# #                 students[name] = marks
# #                 break
            

# #             except ValueError as e:
# #                 print("Error:", e)
# #                 print("Try again...\n")

# #     print("\nStudent Data:", students)

#     # calculate average
#     # avg = sum(students.values()) / len(students)
#     # print("Average marks:", avg)


# # student_data()
#49.Create a function to accept mobile number. 
# #Mobile number should contain 10 digits. No Special character, alphabets and space.
def mobileNo():
    try:
        phonenum=input("enter your contact no : ")
        if (not phonenum.isdigit()) or len(phonenum) != 10:
            raise ValueError("invaild mobile no ")

    except ValueError as e:
        print("error",e)
        print("be careful and try again")

    else:
        print("phone no is saved successfully")

    finally:
        print("your contact number is safe with us ")


mobileNo()    

#50.Create a function to generate auto-password based on specific person details. 
#Ask user to enter name, DOB. And password must be First name 4 characters and year of birth.
def auto_password():
    name = input("Enter your name: ").strip()
    dob = input("Enter your DOB (DD-MM-YYYY): ").strip()

    # get first 4 characters of name
    first_part = name[:4]

    # get year from DOB
    year = dob.split("-")[-1]

    password = first_part + year
    print("Your auto-generated password is:", password)


auto_password()





#Q51,52,53.	Create a empty dictionary and ask user to enter values as name, DOB, mobile number add all the details in dictionary with customer number as 1 for first time. If user try to enter another value, then number should increase as 2 with new details and previous values should not change.
# For example:
# {}
# {1:{name : "Sachin", "DOB": "21-06-1965" , "mobile": "1234123423"}}

# {1:{name : "Sachine", "DOB": "21-06-1965" , "mobile": "1234123423"},
# 2: {name : "Sumedh", "DOB": "02-02-2002" , "mobile": "1234123433"}}

import os

File_name="cust_info.text"

def read_data():
    if os.path.exists(File_name):
        with open (File_name,"r")as f:
            content=f.read()
            if content:
                return eval(content)
    return {}

def write_data(data):
    with open(File_name,"w")as f:
        f.write(str(data))
 
customer_dict=read_data()

while True:
    print("\n Enter customer details ")

    name=input("enter name : ")
    dob=input("enter DOB(dd-mm-yyyy)")
    mobile=input("enter mobile number ")

    if customer_dict:
        new_id=max(customer_dict.keys())+1
    else:
        new_id=1

    customer_dict[new_id]={
        "name":name,
        "DOB":dob,
        "mobile":mobile
    }    
    print(customer_dict)
    write_data(customer_dict)

    choice = input("\nAdd another customer? (y/n): ")
    if choice.lower() != "y":
        break


#54Create a table  cust_info as sr_no, name, DOB, mobile. 
# Ask user to enter the information from python code. Validate all fields and after validation insert records in the table.
import pyodbc
conn=pyodbc.connect(
    "Driver:{SQL server};",
    "Server:DESKTOP-I7V7GR2\\SQLEXPRESS;"
    "Database: ;",
    "Trusted_Connection=yes;"
)
cursor=conn.cursor()

while True:
    try:
        name=input("enter name : ")
        if not name.isalpha() and name.strip() == "": 
            raise("invaild name")
        dob=input("enter DOB(dd-mm-yyyy)")
       
        mobile=input("enter mobile ")
        if not mobile.isdigit() or len(mobile) != 10:
                raise ValueError("Mobile must be 10 digits")

    except Exception as e:
        print("error: ",e)

    cursor.excute("INSERT INTO cust_info(name,dob,mobile)VALUES ?,?,?",name,dob,mobile)    

# 55.	Dict1= {“Key”: {“subkey”:20} ,  “k2”:{“sub2” : 5}, “k3” : {“sub4” :16},  “k4” : {“sub4” : 6}}
# Sort elements based on values
# Output must be {,  “k2”:{“sub2” : 5}, “k4” : {“sub4” : 6},  “k3” : {“sub4” : 16}, “Key”:{“subkey”:20}}


    Dict1 = {
    "Key": {"subkey": 20},
    "k2": {"sub2": 5},
    "k3": {"sub4": 16},
    "k4": {"sub4": 6}
}

sorted_dict = dict(
    sorted(Dict1.items(), key=lambda x: list(x[1].values())[0])
)

print(sorted_dict)



#56.Create a function to calculate age till now.
from datetime import datetime

def calculateAge(dob):
    today = datetime.today().date()
    birth_date = datetime.strptime(dob, "%d-%m-%Y").date()

    age = today.year - birth_date.year

    print("Your age is:", age)


# Q57	Create a function to check age eligibility for given customer based on DOB. 
# Function will take two input DOB and ELIGIBILITY age.
DOB = input("Enter date of birth (DD-MM-YYYY): ")
calculateAge(DOB)

from datetime import datetime

def check_eligibility(dob, eligibility_age):
    # dob format: "YYYY-MM-DD"
    dob_date = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()

    age = today.year - dob_date.year - (
        (today.month, today.day) < (dob_date.month, dob_date.day)
    )

    if age >= eligibility_age:
        return f"Eligible (Age: {age})"
    else:
        return f"Not Eligible (Age: {age})"

print(check_eligibility("2000-05-10", 18))

# Q58.	Create a function to check if string is palindrome or not ? 
# For example, if input is NITIN then reverse of the string is same then it is palindrome. 
# If input is ANIL then reverse is LINA which is not same then it is not palindrome.  

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("NITIN"))  # True
print(is_palindrome("ANIL")) 

#Q59.	Create a function to generate a Fibonacci Series.
# 0 1 1 2 3 5 8 13 21 34 …..  upto 100 
def fibonacci_upto_100():
    a, b = 0, 1
    
    while a <= 100:
        print(a, end=" ")
        a, b = b, a + b

fibonacci_upto_100()

# 60.Write a code to generate factorial of the number 
# For example: factorial of 5 = 5! = 5*4*3*2*1
def factorial(n):
    fact = 1
    
    for i in range(1, n+1):
        fact *= i
        
    return fact

print(factorial(5))

# 61.	Write a program to find largest number in the list.
lst = [10, 45, 67, 23, 89, 12]

largest = lst[0]

for num in lst:
    if num > largest:
        largest = num

print("Largest:", largest)

# 62.	There are two string l1 =[ 1,2,3,4,5] and l2 =[3,2,8,7,9]


lst = [1,2,2,3,4,1,2,3]

freq = {}

for item in lst:
    freq[item] = freq.get(item, 0) + 1

print(freq)

#Q63 then write a program to find common elements in the list.
l1 = [1,2,3,4,5]
l2 = [3,2,8,7,9]

common = []

for item in l1:
    if item in l2:
        common.append(item)

print(common)










        





        




