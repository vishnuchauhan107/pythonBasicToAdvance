import calendar
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

print(calendar.month(yy, mm))
# out-Enter year: 2021
# Enter month: 5
#       May 2021
# Mo Tu We Th Fr Sa Su
#                 1  2
#  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30
# 31