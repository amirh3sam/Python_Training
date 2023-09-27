"""


2. Create a python file named encapsulation_practice:
		create a class called Item
		    private variables:
		        name, unit_price, quantity

		    Encapsulate all the fields:
		        Conditions:
		            name can not be empty
		            unit price can not be negative
		            quantity can not be negative

		        If invalid data are given to set the firled, then make sure to throw an error duribg the runtime.
		        	(hint: you can use 'raise RuntimeError('Exception message')')


		    Add a constructor that allows user to set all the fields when the object is created.
		            (If the arguments not valid it should not be set to the instances)

		    Methods:
		        calcCost(): returns the total cost
		        toString(): returns the name, unit price, quantity and total cost info as calculated by calcCost()
"""