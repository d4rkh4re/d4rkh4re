################################################################################
# terminalOS.py
# William C. Morris
# <d4rkh4re@gmail.com>
# 
# This is open source. Take it, change it, sell it. Just leave a refference to
# either the original program name or myself so that other users can find the
# software easily. All code taken and derived from terminalOS MUST be at least
# as open as this.
# 
################################################################################

terminal_commands = ["help", "about", "exit"]

def terminalOS():
    """ terminalOS """
    
    while True:
        user_input = input("$termOS: ")
        execute_command(user_input)

def execute_command(u_command):
    """ Parses user input and checks to see if a command exists. """
    
    if u_command == "help":
        print("Commands:", terminal_commands)
    elif u_command == "about":
        print("Written by William C. Morris <d4rkh4re@gmail.com>")
    elif u_command == "exit":
        exit()
    else:
        print("'", u_command, "'", "is an unknown command")

################################################################################
################################################################################

terminalOS()
