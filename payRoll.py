"""
Task: Write a program to prompt the user for hours
and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and
1.5 times the hourly rate for all hours worked
above 40 hours. Use 45 hours and a rate of 10.50
per hour to test the program (the pay should be 498.75).
You should use input to read a string and
float() to convert the string to a number. Do not worry
about error checking the user input - assume
the user types numbers properly.
"""
totalPay = 0.0
h = 0.0
employeeRate = 0.0
stdHrs = 40.0
def employeeHrs():
 hrs = input("Enter Hours:")
 try:
    h = float(hrs)
 except:
    h = -1.0
 return h

def employeePayRate():
 payPerHr = input("Enter Rates:")
 try:
    employeeRate = float(payPerHr)
 except:
    employeeRate = -1.0
 return employeeRate

def employee_PayRoll():
 nh = employeeHrs()
 nemployeeRate = employeePayRate()
 if nh <= stdHrs and nh > 0 and nemployeeRateemployeeRate > 0:
    totalPay = stdHrs * employeeRate
 elif nh > stdHrs and nh > 0 and nemployeeRate > 0:
    totalPay = (((nemployeeRate * 1.5) * (nh - stdHrs)) + (stdHrs * nemployeeRate))
 else:
    if nh == -1.0:
        print("{} is not a valid hour".format(nh))
        quit()
    if employeeRate == -1.0:
        print("{} is not a valid rate".format(nemployeeRate))
        quit()

 print(totalPay)
