import art

print(art.logo)

def subtract(a,b):
  return a-b

def add(a,b):
  return a+b

def divide(a,b):
  return a/b

def multiply(a,b):
  return a*b


def calculator():
  a=float(input("What's the first number?\n"))
  flag=True
  while(flag):
    choice=input("+\n-\n*\n+\n/\nPick an operation\n")
    b=float(input("What's the next number?\n"))
    res=0
    if choice=='+':
      res=add(a,b)
      print(f"{a} {choice} {b} = {res}")
    elif choice=='-':
      res=subtract(a,b)
      print(f"{a} {choice} {b} = {res}")
    elif choice=='*':
      res=multiply(a,b)
      print(f"{a} {choice} {b} = {res}")
    elif choice=='/':
      res=divide(a,b)
      print(f"{a} {choice} {b} = {res}")
    else:
      print("Wrong selection")
    ans=input(f"Type 'y' to continue calculating with {res} or type 'n' to start a new calculation\n")
    if ans=='n':
      flag=False
    else:
      a=res
  calculator()


calculator()



