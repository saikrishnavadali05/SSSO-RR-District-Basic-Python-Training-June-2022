from datetime import date
d=list(map(int,input("Enter your date dd-mm-yyyy:").split("-")))
d1=date(d[2],d[1],d[0])
d2=date(2022,11,23)


if(d1>d2):
    print("Date must be less than 23-11-2022")

elif((d[0] not in range(1,32))or d[1] not in range(1,13)):
    print("invalid input enter in the form of dd-mm-yyyy")
else:
    f=d2-d1
    print("difference in days is ",f.days)
    print("differnce in hours is ",f.days*24)
    print("differnce in minutes is ",f.days*1440)
    print("differnce in seconds is ",f.days*86400)
