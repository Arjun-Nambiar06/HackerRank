def timeConversion(s):
    if s[-2:]=='PM' and s[:2]!='12':
        s=str(int(s[:2])+12)+s[2:-2]
    elif s[-2:]=='AM' and s[:2]=='12':
        s='00'+s[2:-2]
    else:
        s=s[:-2]
    return s

time=input("Enter time in the 12-hour format (hh:mm:ssAM or hh:mm:ssPM): ")
print("The same time in 24-hour format is: ", timeConversion(time))