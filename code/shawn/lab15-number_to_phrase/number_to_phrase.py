# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 15 - Number to Phrase
# Date: 10/25/2019

# use modulus or string operations to break things up to digits
# use the digit as an index for a list of strings or as a key for a dict of digit:phrase pairs
# ver 3 and 4 are optional
# make function to do this, then call the function

# for clearing screen
import os

# declare dictionary for number/english equivalents 
num_translated = {
    '0': '',        # will hardcode input of zero, but the empty string is needed for multiples of 10
    '1': 'one',
    '2': 'two', 
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven', 
    '8': 'eight', 
    '9': 'nine',
    '10': 'ten', 
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen', 
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty', 
    '30': 'thirty', 
    '40': 'fourty',
    '50': 'fifty', 
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninty'
}

# function for returning ones place
def return_ones_digit(num):
    ''' takes in a int, returns string '''
    return str(num % 10)

# function for returning tens place
def return_tens_digit(num):
    ''' takes an int, returns a string representing how many times that number can be divided by 10 '''
    return str((num // 10) * 10)

# function for returning hundreds place
def return_hundreds_digit(num):
    ''' takes an int, returns a string representing how many times number can be divided by 100 '''
    return str(num // 100)

# function for get input
def get_number_input():
    ''' returns user number input as an int'''
    while True:
        input_number = int(input("Please input number from 0 to 100: "))
        if input_number >= 0 and input_number < 1000:
            return input_number
        print("Please try different input")

# function for printing english version of number
def print_english_num():
    ''' this function takes no arguments, but will print english version of a number entered by user '''

    # get input 
    num = get_number_input()

    # use if statements to figure out which functions to call based on size of num
    if num == 0:
        print('\n***** Your number is: zero *****\n')  # edge case based on how dictionary is set up
    elif num < 20:
        print(f'\n***** Your number is {num_translated[str(num)]} *****\n')
    elif num >=20 and num <= 99:
        print(f'\n***** Your number is {num_translated[return_tens_digit(num)]} {num_translated[return_ones_digit(num)]} *****\n')
    elif num >=100 and num <= 999:
        print(f'\n***** Your number is {num_translated[return_hundreds_digit(num)]} hundred {num_translated[return_tens_digit(num % 100)]} {num_translated[return_ones_digit(num)]} *****\n')

# main loop
while True:

    prompt = 'Please type number for mode: \n (1) Number to English conversion \n (2) Number to Roman numeral conversion \n (3) Time to English \n (4) Exit \n Input: '
    mode_select = input(prompt)
    if mode_select not in ['1','2','3','4']:
        print('Invalid command, try again')
    elif mode_select == '1':
        print_english_num()
    elif mode_select == '4':
        break

print("Program Exiting")

