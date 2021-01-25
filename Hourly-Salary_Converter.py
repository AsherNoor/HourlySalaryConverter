"""
Hourly / Salary Converter
-------------------------
Dec/27/2020

Coder: ryn0f1sh (Ash Noor)
"""

#-- The Imports
import math
#-------------




"""
Formula 1
From Salary to Hourly.
(annual salary ÷ 52) ÷ 40 = hourly rate
"""
def sTOh():
    salary = int(input("Enter your Salary: "))
    hourly_rate = (salary/52) / 40
    print("Your hourly rate is: "+str(int(hourly_rate)))




"""
Formula 2
From Hourly to Salary.
(hourly rate x 40) x 52 = Salary
"""
def hTOs():
    hourly = int(input("Enter is your Hourly rate: "))
    salary_rate = (hourly * 40) * 52
    print("Your annual salary is: "+str(int(salary_rate)))




"""
Intro to the program.
"""
def intro():
    print("\n--------------------------------------"
          "\nWelcome to The Hourly Salary Converter"
          "\n--------------------------------------\n")

    #-- UI: Which Convertion.
    print("Which Convertion do you need?"
          "\n[1] From Salary to Hourly"
          "\n[2] From Hourly to Salary")
    choice = int(input("\nEnter your choice here: "))
    if choice == 1:
        sTOh()
    else:
        hTOs()


#-- Calling function
intro()


