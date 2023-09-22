"""


17. Create a python file named crew_and_passanger, Given a number of people on the ship, determine how many need to be crew members and how many can be passengers. Print how many of each type there should be.

            Total: 50  ====> 20 crew, 30 passengers
            Total: 75  ====> 25 crew, 50 passengers
            Total: 100 ====> 30 crew, 70 passengers
            Any other number of people on the ship is not valid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT

"""

total_people = int(input("Enter the total number of people on the ship: "))

if total_people == 50:
    crew_count = 20
    passenger_count = 30
elif total_people == 75:
    crew_count = 25
    passenger_count = 50
elif total_people == 100:
    crew_count = 30
    passenger_count = 70
else:
    print("Any other number of people on the ship is not valid")

print(f"Total: {total_people} ===> {crew_count} crew, {passenger_count} passengers")
