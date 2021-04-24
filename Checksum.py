#!/usr/bin/env python
# coding: utf-8

# In[385]:


import numpy as np
def Complement(c):
    return '1' if (c == '0') else '0'
def Checksum_gen(dataword, word_size, num_blocks):
    redunDancyBit = 0
    com = ""
    buffer = ""
    carryBit = '1'
    for i in range(num_blocks):
        if(len(dataword[i]) <= word_size):
            if(len(bin(redunDancyBit)) - 2  > word_size):
                buffer = bin(redunDancyBit)[2:]
                buffer = bin(int(buffer,2) + int(carryBit,2))
                redunDancyBit = int(buffer[2:],2)
            #sum = bin(int(b[0], 2) + int(b[1], 2))
            redunDancyBit += int(dataword[i], 2)
    if len(bin(redunDancyBit)) > word_size:
        index = len(bin(redunDancyBit)) - word_size
        new2 = bin(redunDancyBit)[index:]
    for x in range(len(new2)):
        com += Complement(new2[x])
    checksum = np.append(dataword,com)
    return checksum

def Checksum_check(codeword, word_size, num_blocks):
    redunDancyBit = 0
    com = ""
    buffer = ""
    carryBit = '1'
    for i in range(num_blocks):
        if(len(codeword[i]) <= word_size):
            if(len(bin(redunDancyBit)) - 2  > word_size):
                buffer = bin(redunDancyBit)[2:]
                buffer = bin(int(buffer,2) + int(carryBit,2))
                redunDancyBit = int(buffer[2:],2)
            #sum = bin(int(b[0], 2) + int(b[1], 2))
            redunDancyBit += int(codeword[i], 2)
    if len(bin(redunDancyBit)) > word_size:
        index = len(bin(redunDancyBit)) - word_size
        new2 = bin(redunDancyBit)[index:]
    print(com)
    if (int(new2,2) == 0):
        return "PASS"
    else:
        return "FAIL"


# In[383]:


# 5 digits
dataword = np.array(['10011001','11100010','00100100','10000100'])
# dataword = '10101001 00111001'
word_size = len(dataword[0])
num_blocks = len(dataword)
codeword = Checksum_gen(dataword, word_size, num_blocks)
print('Checksum = ',codeword)


# ## Test cases for checksum_gen()

# In[ ]:


# Test case 2
#dataword = np.array(['0'])

# Test case 2
#dataword = np.array(['101010001100','011111111111'])

# Test case 3
#dataword = np.array(['10','10'])

# Test case 4
#dataword = np.array(['111010101','001100111','000000000'])

# Test case 5
#dataword = np.array(['110011','001110'])

# Test case 6
#dataword = np.array([None])

# Test case 7
#dataword = np.array([64,35])

# Test case 8
#dataword = np.array(['4','9'])

# Test case 9
#dataword = np.array(['00000','00000'])

# Test case 10
#dataword = np.array(['11100101011010', '10101000111100'])


# In[386]:


word_size2 = len(codeword[0])
num_blocks2 = len(codeword)
validity = Checksum_check(codeword, word_size2, num_blocks2)
print('Validity:',validity)


# ## Test cases for validity

# In[ ]:


# Test case 2
#dataword = np.array(['0'])

# Test case 2
#dataword = np.array(['101010001101','011111111111'])

# Test case 3
#dataword = np.array(['10','10'])

# Test case 4
#dataword = np.array(['111010101','001100111','000010000'])

# Test case 5
#dataword = np.array(['110111','001110'])

# Test case 6
#dataword = np.array([None])

# Test case 7
#dataword = np.array([64,35])

# Test case 8
#dataword = np.array(['4','9'])

# Test case 9
#dataword = np.array(['01000','00100'])

# Test case 10
#dataword = np.array(['11100101011010', '10101000111100'])

