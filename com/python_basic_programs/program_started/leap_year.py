year = int(input("Enter the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is leap year")
        else:
            print(year,"not leap year")
    else:
      print(year, "not leap year")
else:
   print(year,"not leap year")
   # out-Enter the year:2000
   # 2000 is leap year