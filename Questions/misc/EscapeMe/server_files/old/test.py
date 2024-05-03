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
    return user_input

def main():
    print_banner()
    greet_user()

    while True:
        user_input = take_user_input()

        # Call the C program with the user input as an argument
        try:
            # subprocess.run(["./test", user_input])
            command = ["./test", user_input]
            #print(command)
           # print("return", os.system(f'./test {user_input}'))
            subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate()
            #a = subprocess.Popen(command,stdout=subprocess.PIPE)
            #print(a.communicate()[0].decode())
        except FileNotFoundError:
            print("Error: Please reconnect to the server.")
            break
        #print(os.listdir('/tmp'))
        #os.system("/bin/sh")
        with open("/tmp/data.txt","r") as fpt:
            print("You wrote:",fpt.read())

        choice = input("Do you want to continue writing data? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
