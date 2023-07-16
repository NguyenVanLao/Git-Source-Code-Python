import datetime
now = datetime.datetime.now()
a = now.strftime("%d - %m - %Y")
b = now.strftime("%H: %M: %S ")
print(a)
print(b)
