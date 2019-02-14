import datetime

#asking the user to input their year of birth
Year_Of_Birth = input("Enter your year of birth (yyyy)\n>>> ")

#Type conversion here
age = int(Year_Of_Birth)
age= 2019-age

#lets print the age now
print("Your age is {0:d}".format(age))
if age< 18:
    print('minor')
if age>= 18 and age<36:
    print('youth')
if age>36:
    print('elder')
