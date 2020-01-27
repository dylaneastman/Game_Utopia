#Dylan Eastman
#Game Database
#Started: jan 27 2020
import pickle

def newgame():
   print("Running newgame()")

def editg():
   print("Running editg()")

def printall():
   print("Running printall()")

def search():
   print("Running search()")
   
def terminate():
   print("Running terminate()")
   
def savdat():
   print("Running savdat()")
   
def quit():
   print("Running quit()")


print("""

Welcome to Game Utopia
---------------------------

Program Menu
1) Add Game
2) Edit Game
3) Print all games
4) Search by Title
5) Remove a Game
6) Save Database

Q) Quit

""")

choice = input("What would you like to do? ")
if choice == "1":
   newgame()
elif choice == "2":
    editg()
elif choice == "3":
    printall()
elif choice == "4":
    search()
elif choice == "5":
    terminate()
elif choice == "6":
    savdat()
elif choice == "Q" or choice == "q":
    quit()
    keep_going = False
else:
    print("*** NOT A VALID CHOICE ***\n")
    