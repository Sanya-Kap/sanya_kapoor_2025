#3.6 hacks

```python 

num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

if num1 == num2:

        print("They are equal")

elif num1 > num2:

        print("The larger number is (num1)")

else:

        print("The larger number is (num2)")



#3.7 hacks


grade: int(input("Enter Grade:"))
attendance: int(input("Enter Attendance:"))

if grade >=75
<br>
    if attendance >= 75:
        <br>
        print("You have passed")
    <br>    
    else:
        <br>
        print("Failed bc of attendance")
<br>
else:
    <br>
    print("Failed bc of grade")


#python segment

weight = float(input("Enter the weight of the package in pounds: "))
delivery_days = int(input("Enter the delivery speed (number of delivery days): "))

express = delivery_days < 3

if express:
        if weight <= 5:
            print("Shipping costs 10$")
        else:
            print("Shipping costs 15$")
else: 
        if weight <= 5:
            print("Shipping is 10$)
        else:
            print("Shipping is 5$)



#age_ticketprices

age = int(input("Enter you age:"))
student = int(input("Are you a student; yes/no"))


if age <= 25:
    ticket_price = 20
else:
    ticket_price = 25

if student = yes:
        ticket_price= ticket_price*0.5

Print("Your ticket price is (ticket_price)")


#3.8popcorn

age = int(input("Enter Your Age:"))
student = int(input("Are you a stuent(yes/no)"))
ticket = 0

if student = no:
    if age <= 12:
        print("Your ticket is 5$")
    elif age>12 and age<=63:
        print("Your ticket is 10$")
    else:
        print("Your ticket is 8$")
else:
    if age <= 12:
        print("Your student ticket is 4$")
    elif age>12 and age<=63:
        print("Your student ticket is 8$")
    else:
        print("Your student ticket is 6.4$")

break

try: 
    number = int(input("Enter a value:"))
    result = 10/number
    print("The result is:", result)
except ValueError:
    print("Not a valid Error")
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("Successful operation")


#3.8 homework
<br>
def get_positive_number():
    <br>
    while True:
        <br>
        num = int(input("Enter a number:"))
        <br>    

        try: 
            number = float(num)
            if number > 0:
                print("Success")
                break
            else:
                print("Try again")
        except ValueError:
            print("Error: Enter a valid number")


#3.10 popcorn


my_list = [1, 2, 3]
<br>
my_list.append(4)
<br>
print(my_list)

#second popcorn

alist = ['book', 'pencil', 'pen']
<br>
alist.insert('book', 'a') 
<br>
del aList[2]
<br>
print(aList)
<br>
aList[1] = 'table'
<br>

#3.10 homework

#Code 1

user_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

even_sum = sum([num for num in user_list if num % 2 == 0])

print(f"The sum of even numbers is: {even_sum}")
```

```python

# Code 2

user_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

min_value = min(user_list)
max_value = max(user_list)

print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")
```
