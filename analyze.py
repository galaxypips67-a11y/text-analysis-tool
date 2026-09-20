#Welcome
def welcomeuser():
 print("\nWelcome to the text analysis tool, i will mine and analyze a body of text from a file you give me")

# Get a username
def getusername():
 #print message  prompting  user  get to get username into the terminal.
 Usernamefrominput= input("\nTo begin please enter your username\n")
 return Usernamefrominput


#Greet user
def greetuser (name, instruction):
  print("\nHello," + name + "," + instruction)




welcomeuser()
username = getusername()
greetuser(username, "get ready")





