
for i in range(1, 6):
    print(i)
    if i == 3:
        break # exits the loop

print('-------------')

for i in range(1, 6):
    if i == 3 or i == 4:
        continue # skips to the next iteration
    print(i)

print('-------------')

# pass statement is like placeholder in a loop/function/class
# nothing happens when the pass is executed
# result in no operation
# the main purpose of pass statement is work on body of that statement block later on
# also is for achieving abstraction

for i in range(1, 6):
    if i == 3 or i == 4:
        pass
    print(i)




def function():
    pass

if True:
    pass

class Class:

    def method(self):
        pass

    pass

