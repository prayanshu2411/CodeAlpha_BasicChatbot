def hello( ):
    print("Hi ! How can i help you ?")
def add( ):
    a = int(input("enter the first number ="))
    b = int(input("enter the second number ="))
    print ("Sum = " , a+b)
def sub( ):
     a = int(input("enter tha first number="))
     b = int(input("enter the second number="))
     print("Sub =", a-b)
def mul( ):
         a = int(input("Enter tha first number: "))
         b = int(input("Enter the second number: "))
         print("Multiplication = " , a*b)
def div( ):
         a = int(input("Enter tha first number: "))
         b = int(input("Enter the second number: "))
         if b == 0:
          print("cannot divide by zero")
         else :
          print ("divide =" , a/ b)   
          
command = ("")
while command != "bye":
    command = input("Welcome to CodeAlpha Chatbot Type 'help' to see available commands.")
    if command == "hello":
        hello( )
    elif command == "help":
       
       print("Commands:")
       print("hello")
       print("how are you")
       print("your name")
       print("thanks")
       print("add")
       print("sub")
       print("mul")
       print("div")
       print("table")
       print("time")
       print("bye")
    elif command == "how are you":
        print("i am fine")
    elif command == "your name":
        print("i am code alfa bot")
    elif command == "thanks":
        print("you're welcome")
    elif command == "add":
       add( )
    elif command == "sub":
       sub( )
    elif command == "mul":
       mul( )
    elif command == "div":
       div( )
    elif command == "table":
        num = int(input("Enter any number:"))
        for i in range( 1, 11):
            print(num , "x", i ,"=", num * i)
    elif command == "time":
         print("feature coming soon")
    elif command == "bye": 
        print("Good bye")
    else:
        print(" Sorry , i don't understand.")