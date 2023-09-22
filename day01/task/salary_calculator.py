"""

12. Create a python file named salary_calculator
            1.1 Ask the user to enter the following info:
                     1.1.1 "Enter your name"
                     1.1.2 "Enter your hourly rate"
                     1.1.3 "How many hours you work in a week?"

            1.2 write a program that can create the salary based on the user given info
                         Hint: number of weeks are 52

                         salary = hourlyRate * weeklyHour * 52

            Ex:
                Given Data:
                    name = Joshua
                    hourly_rate = 40
                    weekly_hours = 45


                Output:
                    Hello Joshua, your salary is $ 93600.00

"""

name = input("Enter your name : ")
hourly_rate = int(input("Enter your hourly rate : "))
weekly_hours = int(input("How many hours you work in a week :"))
salary = float(hourly_rate * weekly_hours * 52)

print(f"Hello {name}, your salary is $ {salary}")
