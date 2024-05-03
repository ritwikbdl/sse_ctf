#!/usr/bin/python3
import subprocess
import os
def print_banner():
    # ASCII art banner
    print('''
░██████╗░██████╗███████╗  ██████╗░░█████╗░██████╗░░░██╗██╗
██╔════╝██╔════╝██╔════╝  ╚════██╗██╔══██╗╚════██╗░██╔╝██║
╚█████╗░╚█████╗░█████╗░░  ░░███╔═╝██║░░██║░░███╔═╝██╔╝░██║
░╚═══██╗░╚═══██╗██╔══╝░░  ██╔══╝░░██║░░██║██╔══╝░░███████║
██████╔╝██████╔╝███████╗  ███████╗╚█████╔╝███████╗╚════██║
╚═════╝░╚═════╝░╚══════╝  ╚══════╝░╚════╝░╚══════╝░░░░░╚═╝
''')

def greet_user():
    # Greet the user
    print("Welcome! This program allows you to save some data.")


def take_user_input():
    # Ask user for input
    user_input = input("Enter your data: ")
    user_input = r"{}".format(user_input)
    return user_input

def main():
    print_banner()
    greet_user()

    while True:
        user_input = take_user_input()

        # Call the C program with the user input as an argument
        try:
            # subprocess.run(["./test", user_input])
            # test = r'-n t>>r &'
            #os.chdir('/app')
            print("Here is my /bin:",os.listdir('/bin'),"\n")
            command = ["./test", user_input]
            #print(r"{}".format(user_input))
            #subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()
            a = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print(a.communicate()[0].decode())
        except FileNotFoundError:
            print("Error: Please reconnect to the server.")
            break
        with open("/tmp/data.txt","r") as fpt:
                print("You wrote:",fpt.read())

        #print(subprocess.check_output("echo a>>r", shell=True).decode("utf-8"))
        #print(subprocess.check_output("cat r", shell=True).decode("utf-8"))
        print(os.getcwd(),",",os.listdir('/app'))
        choice = input("Do you want to continue writing data? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
