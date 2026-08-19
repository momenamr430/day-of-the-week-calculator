from pycparser.c_ast import Switch

try:
    q = int(input("enter the day: "))
    while not(31>=q>=1):
        print("please enter a valid day:")
        q = int(input("enter the day:"))
except:
    print("please enter valid day:")
print("months :"
    """
    1-January 
    2-February 
    3-March 
    4-April 
    5-May 
    6-June 
    7-July 
    8-August 
    9-September 
    10-October 
    11-November 
    12-December """)
try:
    m = int(input("choose the month(1-12):"))
    while not(12>=m>=1):
        print("please enter a valid month:")
        m = int(input("choose the month(1-12):"))
except:
    print("please enter a valid month:")

year= input("enter the year(min: 1000, max: 9999):")
while len(year) != 4:
    print("please enter a valid year:")
    year= input("enter the year(min: 1000, max: 9999):")
k = int(year[-2:])
j = int(year[:2])

result =(q+((13*(m+1))//5)+k+(k//4)+(j//4)+5*j)
result = result%7
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
month =""
for i in range(len(months)):
    if(i+1 ==m):
        month =months[i]
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for i in range(len(days)):
    if(i+1 ==result):
        result =days[i+1]
print("{} {} {} is day: {}".format(q,month,year,result))

