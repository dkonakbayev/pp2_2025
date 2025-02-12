from datetime import datetime,timedelta
x=datetime.now()
print(x)
y = x.replace(microsecond=0)
print(y)