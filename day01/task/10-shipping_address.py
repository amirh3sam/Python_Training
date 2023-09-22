"""
10. Create a python file named shipping_address
            Ask the user to enter the following info, and display the shipping address of the user:
                    1. "Enter your full name"
                     2. "Enter your building number"
                     3. "Enter your street name"
                     4. "Enter your city name"
                     5. "Enter your state name"
                     6. "enter your zip code"

             Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping addrrees is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030

"""
name = input("Enter your full name : ")
building_number = input("Enter your building number : ")
street = input("Enter your street name : ")
city = input("Enter your city name : ")
state = input("Enter your state name : ")
zipcode = input("enter your zip code : ")

print(f"Your shipping addrrees is:\n\t\t{name}\n\t\t{building_number} {street}\n\t\t{city}, {state} {zipcode}")
