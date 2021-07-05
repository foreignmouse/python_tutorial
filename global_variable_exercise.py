x = 100

def myfunc():
  global x
  x = 200
  print(x)

myfunc()

print(x)