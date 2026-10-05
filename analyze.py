from random_username.generate import generate_username


#Welcome
def welcomeuser():
 print("\nWelcome to the text analysis tool, i will mine and analyze a body of text from a file you give me")

# Get a username
def getusername():
   Usernamefrominput= input("\nTo begin please enter your username\n")
    
   


   if len(Usernamefrominput) < 5 or not Usernamefrominput.isidentifier():
     print("\nYour username must be at least 5 characters long, (a-z/A-Z/0-9), no spaces and must not start with numbers")
     print("Assign username instead...")
     return generate_username()[0]
    
  
   return Usernamefrominput

#Greet user
def greetuser (name, instruction):
  print("\nHello ," + name + "," + instruction)




welcomeuser()
username = getusername()
greetuser(username, "get ready")







