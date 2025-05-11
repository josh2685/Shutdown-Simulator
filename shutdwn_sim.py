#####Shutdown Simulator#####

import os, time #needed libraries

os.system("clear") #clear the terminal

def shutdown(): #to shutdown the computer
    confirmation = int(input("are you sure you wish to shut the computer down? yes[1] or no[2]: ".title()))
    if confirmation == 1:
        print("okay, the terminal will shutdown in 10 seconds...".title())
        for i in range(10, 0, -1):
            time.sleep(1)
            print(i, end=" ", flush=True)
        os.system("shutdown -h now")
    elif confirmation == 2:
        print("thank you for playing!".title())

def restart(): #to restart the computer
    confirmation = int(input("are you sure you wish to restart the computer? yes[1] or no[2]: ".title()))
    if confirmation == 1:
        print("okay, the terminal will restart in 10 seconds...".title())
        for i in range(10, 0, -1):
            time.sleep(1)
            print(i, end=" ", flush=True)
        time.sleep(1)
        os.system("reboot")
    elif confirmation == 2:
        print("thank you for playing!".title())

#choose which one you want to do
print("this is a basic progam in python that will ask a user if they want to shutdown or restart the computer.".title())
choose = int(input("would you like to shutdown or restart the computer? neither[0], shutdown[1], or restart[2]: ".title()))
if choose == 0:
    print("thanks for playing. goodbye!".title())
elif choose == 1:
    shutdown()
elif choose == 2:
    restart()
else:
    print("sorry, but that is not a valid option!".title())
