#!/usr/bin/env python
# coding: utf-8

# # Programming Set 4
# 
# ## This assignment will test your proficiency in pattern recognition and programming in Python.
# 

# In[28]:


def bin_to_dec(binary_string):
    dec = 0 
    for i in range(len(binary_string)):
        if binary_string[len(binary_string) - 1 - i] == "1":
            dec = dec + (2**i)
    return dec


# In[2]:


def dec_to_bin(number):
    if number == 0: 
        return "0"
    bin = ""
    while number > 0 :
        bin = str(number % 2) + bin
        number = number // 2 
    return bin


# In[198]:


def telephone_cipher(message):
    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

    num_string = ""
    for i in range(len(message)):
        num_string += encoder_dict.get(message[i])
        if i < (len(message)-1):
            if str(encoder_dict.get(message[i]))[0] == str(encoder_dict.get(message[i+1]))[0]:
                num_string += "_"

    return num_string


# In[194]:


def telephone_decipher(telephone_string):
    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
   
    message = ""
    current_digit = ""
    i = 0
    while i < len(telephone_string):
        current_digit = telephone_string[i]
        count = 1 
        while i +1 < (len(telephone_string)) and telephone_string[i] == telephone_string[i + 1]:
            i += 1 
            count += 1
        key = current_digit*count
        if key in decipher_dict:
            message += str(decipher_dict.get(key))
        i += 1
    return message


