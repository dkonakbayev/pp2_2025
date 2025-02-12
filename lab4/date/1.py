from datetime import datetime,timedelta
x = input()
xx=datetime.strptime(x,"%Y-%m-%d")
y = xx - timedelta(days=5)
print(y)

    