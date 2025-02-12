from datetime import datetime,timedelta
x = input("print today`s date")
today = datetime.strptime(x , "%Y-%m-%d")
tomr = today + timedelta(days= 1)
yestr = today - timedelta(days = 1)
print(yestr.strftime("%Y-%m-%d"))
print(today.strftime("%Y-%m-%d"))
print(tomr.strftime("%Y-%m-%d"))


