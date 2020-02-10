from function import *


def handle_check(command):
    respond="no <arg> try again"
    arg=command.split()
    if len(arg)==2:
        if arg[1].isdigit():
            if int(arg[1])%2==0:
                respond="Come on dude, you know even numbers are not prime!"
            else:
                if is_prime(int(arg[1])):
                    respond = "prime"
                else:
                    respond = "not prime"
        else:
            respond = "wrong <arg> try again it have to a number"
    return respond


def handle_factorial(command):
    respond="no <arg> try again"
    arg=command.split()
    if len(arg)==2:
        if arg[1].isdigit():
            respond=factorial(int(arg[1]))
        else:
            respond = "wrong <arg> try again it have to a number"

    return respond


def handle_palindrome(command):
    respond="no <arg> try again"
    arg=command.split()
    if len(arg)==2:
        if arg[1].isdigit():
            if palindrome([i for i in arg[1]]) :
                respond = "palindrome"
            else:
                respond = "not palindrome"
        else:
            respond = "wrong <arg> try again it have to a number"

    return respond


def handle_sqrt(command):
    respond="no <arg> try again"
    arg=command.split()
    if len(arg)==2:
        if arg[1].isdigit():
            if sqrt(int(arg[1])):
                respond = "number is a perfect square"
            else:
                respond = "number is not a perfect square"
        else:
            respond = "wrong <arg> try again it have to a number"
    return respond

def help_command():
    return 'commands list :\n ' \
                     '/help - to get to this* command list. \n ' \
                     '/check  <number> - check if the number is prime.\n ' \
                     '/factorial  <number> - get the factorial of the number.\n ' \
                     '/palindrome  <number> - to check if the number is palindrome.\n ' \
                     '/sqrt  <number> - check if the number have an integer square root (perfect square).\n '

def messageparser(message):
    if message == '/start' or message == '/help':
        tosendback = help_command()
    elif message.split()[0] == '/check':
        tosendback = handle_check(message)
    elif message.split()[0] == '/factorial':
        tosendback = handle_factorial(message)
    elif message.split()[0] == '/palindrome':
        tosendback = handle_palindrome(message)
    elif message.split()[0] == '/sqrt':
        tosendback = handle_sqrt(message)
    else:
        tosendback = "wrong command try again"
    return tosendback
