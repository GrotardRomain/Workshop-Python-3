## String substitution

# Example 01
text = "This is {variable_a} formatted string".format(variable_a="variable based")
print(text)

# Example 02
print("This is a {var} string")
print("This is a {var} string".format(var= "really really cool"))
# Example 03
print("My name is {name}.".format(name="Philippe"))
my_name = "Philippe"
print("Name is {the_name}.".format(the_name=my_name))
print("Name is {the_name}\n{the_name} is {the_name}.".format(the_name=my_name))

# Example 04
text = """So, {name}, the best part is formated strings you don't have to order it.
And these keyword argument replacements, ({var_a}, {var_b}, {name}) can be reused over and over.
Seriously, {name}, this is some fun formatting """.format(
    name="Jerry",
    var_a="Variable 1",
    var_b="Variable 2")
print(text, " this was more String substitution with .format()")

# Example 05
text = "This is {0} formatted string".format("argument based")
print(text)
# Example 05.1
text2 = "This is another {0} formatted string \
with multiple variables like {1} {2} {3}.".format(
    "variable based",
    "some random",
    "replacement",
    "text"
    )
print(text2)
# Example 05.2
text3 = """ So, {0}, the best part is formatted strings you don't have to order it. And these argument replacements,
({1},{2},{0}) can be used and reused over and over.
Seriously {0}, this is some fun formatting.""".format(
    "Jerry",
    "Variable 1",
    "Variable 2"
    )
print(text3)

# %s Subsistution
text4 = "This is %s formatted string"%("remplacement")
print(text4)

text4 = "The %%s format string is not as %s, but still very %s."%("robust", "useful")
print(text4)

# %f Float Subsistution
text5 = "0 decimal places: %.0f" %(20)
print(text5)

text5 = "2 decimal places: %.2f" %(20)
print(text5)

text5 = "10 decimal places: %.10f" %(20)
print(text5)

text5 = "400 decimal places: %.400f" %(10)
print(text5)

# Date Subsistution
import datetime
today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)

text = today.strftime('%-m/%-d/%-y')
print(text)

now = datetime.datetime.utcnow() #utc time
text = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
print(text)

now = datetime.datetime.now() #local time
text = now.strftime('%Y/%m/%d %H:%M:%S.%f') #[:-3]
print(text)

now = datetime.datetime.now()
date_text = now.strftime('%x')
text = "Time is %s" %(date_text)
print(text)