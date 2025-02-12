from datetime import datetime
x = input()
y = input()
firstdate = datetime.strptime(x , "%Y-%m-%d %H-%M-%S")
seconddate = datetime.strptime(y , "%Y-%m-%d %H-%M-%S")
diffr = firstdate - seconddate
print(diffr.total_seconds())