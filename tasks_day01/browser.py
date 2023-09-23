"""
20. Create a python file named browser. Write a program that can display the name of selected browser
        1. declare a String variable named browser_name
        2. Assume that the valid browsers are: chrome, firefox, opera, safari, edge.
        3. if the browser name does not match with the valid browser names, out put should be: Invalid Browser Name

        Ex:
            String browser = "chrome";

        Output:
            Chrome Browser is selected

        Note: MUST use nested if
"""

browser = "firefox"
result = ""

if browser == "chrome" or browser == "firefox" or browser == "opera" or browser == "safari" or browser == "edge":
    if browser == "chrome":
        result += "Chrome Browser is selected"
    elif browser == "firefox":
        result += "firefox Browser is selected"
    elif browser == "opera":
        result += "opera Browser is selected"
    elif browser == "safari":
        result += "safari Browser is selected"
    elif browser == "edge":
        result += "edge Browser is selected"
else:
    result += "Invalid browser"
print(result)
