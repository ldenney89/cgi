#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print("")

form = cgi.FieldStorage()
listval = form.getlist('operand')
try:
    intlist = [int(x) for x in listval]
    body = sum(intlist)
except (ValueError, TypeError):
    body = "Unable to calculate a sum, please provide integer operands."
#print("Your job is to make this work")
print("You provided the numbers {}.".format(str(listval)))
print("The sum of the numbers is: {}".format(body))
