import datetime
a = int(input("Enter the year of your birth:"))
b = int(input("Enter the numeral for your birth month:"))
c = int(input("Enter the day of your birth:"))

def clock():
  origin = datetime.datetime(a, b, c)
  now = datetime.datetime.now()
  print(f"You are {(now - origin)} days old.")
  print("Time listed above is formatted as Days, Hours:Minutes:Seconds.microseconds")

clock()
