#3.6 hacks
<br>
```python
<br>
num1 = float(input("Enter the first number: "))
<br>
num2 = float(input("Enter the second number: "))

if num1 == num2:
<br>
        print("They are equal")
<br>
elif num1 > num2:
<br>
        print("The larger number is (num1)")
<br>
else:
<br>
        print("The larger number is (num2)")
<br>


#3.7 hacks
<br>
#First hack

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
