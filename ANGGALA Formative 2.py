#!/usr/bin/env python
# coding: utf-8

# # Programming Set 2
# 
# ## This assignment will develop your proficiency with Python's control flows.

# In[145]:


def shift_letter(letter, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter == " ":
        return " "
    else:
        #finding index of letter 
        i = alphabet.find(letter)
        #getting new index
        x = (i + shift) % len(alphabet) 
        return alphabet[x] 
    


# In[153]:


def caesar_cipher(message, shift):
    shifted_message = ""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in message: 
        if char != " ":
            shifted_char = alpha[(alpha.find(char) + shift) % len(alpha)]
            shifted_message += shifted_char
        else: 
            shifted_message += char
    return shifted_message


# In[151]:


def shift_by_letter(letter, letter_shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter == " ":
        return " "
    else:
        #finding index of letter and shift_index
        i = alphabet.find(letter)
        shift = alphabet.find(letter_shift)
        #getting new index
        x = (i + shift) % len(alphabet) 
        return alphabet[x] 


# In[157]:


def vigenere_cipher(message, key):
    cipher = "" 
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(message)): 
        if message[i] == " ":
            cipher += " "
        else:
            x = (alphabet.find(message[i]) + alphabet.find(key[i % len(key)])) % len(alphabet)
            cipher += alphabet[x]
    return cipher


# In[165]:


def scytale_cipher(message, shift):
    new_message = message
    code =""
    if len(message) % shift != 0 :
        new_message += "_"*(shift - (len(message) % shift))
    for i in range(len(new_message)):
        x = (i // shift) + (len(new_message) // shift) * (i % shift) 
        code += new_message[x]
    return code 


# In[163]:


def scytale_decipher(message, shift):
    code =""
    rows = len(message)//shift
    for j in range(shift):
        for i in range(rows):
            x = (j +(i* shift)) % len(message) 
            code += message[x]
    return code
    

