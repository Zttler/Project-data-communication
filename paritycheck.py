#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def parity_gen(dataword, word_size, parity_type,array_size):
    cnt = 0
    temp = np.array([])
    codeword = np.empty(shape=(4,8),dtype=str) 
    if parity_type == 1:
        if not dataword:
            return "Error array is NULL"
        for i in range(array_size):
            for j in range(len(dataword[i])):
                if dataword[i][j] == '1':
                    cnt = cnt + 1
            if cnt % 2 == 0:
                temp = np.append(dataword[i],'0')
                codeword[i] = temp
                cnt = 0
            else:
                temp = np.append(dataword[i],'1')
                codeword[i] = temp
                cnt = 0
        return codeword
##---------------Everything store in codeword--------------------------------------------------------------------------------##
    if parity_type == 2:
        count = 0
        temp2 = np.array([])
        second_parity = np.empty(shape=(5,8), dtype = str)
        column_parity = np.zeros(shape=(8,5), dtype = str)
        for i in range(array_size):
            for j in range(len(dataword[i])):
                if dataword[i][j] == '1':
                    cnt = cnt + 1
            if cnt % 2 == 0:
                temp = np.append(dataword[i],'0')
                codeword[i] = temp
                cnt = 0
            else:
                temp = np.append(dataword[i],'1')
                codeword[i] = temp
                cnt = 0
        ct = np.transpose(codeword)
        for x in range(len(ct)):
            for y in range(len(ct[x])):
                if ct[x][y] == '1':
                    count = count + 1
            if count % 2 == 0:
                temp2 = np.append(ct[x],'0')
                column_parity[x] = temp2
                count = 0
            else:
                temp2 = np.append(ct[x],'1')
                column_parity[x] = temp2
                count = 0
        second_parity = np.transpose(column_parity)
        second_parity = second_parity.astype('str')
        return second_parity


# In[90]:


arr = np.array([
    ['1','1','0','0','1','1','1'],
    ['1','0','1','1','1','0','1'],
    ['0','1','1','1','0','0','1'],
    ['0','1','0','1','0','0','1']
])
word_size = len(arr[0])
array_size = len(arr)
codeword = parity_gen(arr, word_size,2,array_size)
print(codeword)


# ## Test cases for parity check_gen()

# In[ ]:


# Test case 2
# arr = np.array([
#     ['1','1','0','0','1','1','1'],
#     ['1','0','1','0','1','0','1'],
#     ['0','1','1','1','0','0','1'],
#     ['0','1','0','1','0','0','1']])

# Test case 3
# arr = np.array([
#     ['1','1','0','1','1','1'],
#     ['1','0','0','1','0','1'],
#     ['0','1',','1','0','0','1'],
#     ['0','1','1','0','0','1']])

# Test case 4
# arr = np.array([
#     ['1','1','0','0','1','1','1'],
#     ['0','1','1','1','0','0','1'],
#     ['0','1','0','1','0','0','1']])

# Test case 5
# arr = np.array([None])

# Test case 6
# arr = np.array(['1'])

# Test case 7
# arr = np.array([
#     ['1'],
#     ['1'],
#     ['0'],
#     ['1'])

# Test case 8
# arr = np.array([
#     [''1','1'],
#     ['1','0','1','0','1','0','1'],
#     ['0','1','1','1','0','0','1'],
#     ['0','1','0','1','0','0','1']])

# Test case 9
# arr = np.array([
#     [1,'1','0','0','1','1','1'],
#     ['1','0','1','0','1','0','1'],
#     ['0','0','0','0','0','0','0'],
#     ['0','1','0','1','0','0','1']])

# Test case 10
# arr = np.array([
#     [1,1,0,0,1,1,1],
#     [1,0,1,0,1,0,1]])


# In[181]:


import numpy as np
def parity_check(codeword, parity_type, array_size):
    row = array_size
    column = len(codeword[0])
#     print(row,column)
    dataset = codeword[:row-1,:column-1]
    cnt = 0
    buffer = np.empty(shape=(row-1,column),dtype=str)
    temp = np.empty(shape=(),dtype=str)
    if parity_type == 1:
        for i in range(len(dataset)):
            for j in range(len(dataset[i])):
                if dataset[i][j] == '1':
                    cnt = cnt + 1
            if cnt % 2 == 0:
                temp = np.append(dataset[i],'0')
                buffer[i] = temp
                cnt = 0
            else:
                temp = np.append(dataset[i],'1')
                buffer[i] = temp
                cnt = 0
        validity = (codeword == buffer)
        if False in (buffer == codeword):
            return 'FAILED'
        else:
            return ':PASS'

##--------------- Everything store in buffer --------------------------------------------------------------------------------##
    if parity_type == 2: 
        cnt = 0
        count = 0
        temp2 = np.array([])
        row = array_size
        column = len(codeword[0])
        dataset = codeword[:row-1,:column-1]
        buffer = np.empty(shape=(row-1,column),dtype=str)
        buffer2d = np.empty([])
        column_parity = np.empty(shape=(column ,row ), dtype=str)
        for i in range(len(dataset)):
            for j in range(len(dataset[i])):
                if dataset[i][j] == '1':
                    cnt = cnt + 1
            if cnt % 2 == 0:
                temp = np.append(dataset[i],'0')
                buffer[i] = temp
                cnt = 0
            else:
                temp = np.append(dataset[i],'1')
                buffer[i] = temp
                cnt = 0
        ct = np.transpose(buffer)
        for x in range(len(ct)):
            for y in range(len(ct[x])):
                if ct[x][y] == '1':
                    count = count + 1
            if count % 2 == 0:
                temp2 = np.append(ct[x],'0')
                column_parity[x] = temp2
                count = 0
            else:
                temp2 = np.append(ct[x],'1')
                column_parity[x] = temp2
                count = 0
        second_parity = np.transpose(column_parity)
        second_parity = second_parity.astype('str')
        validity = (second_parity == codeword)
        if False in validity:
            return 'FAILED'
        else:
            return 'PASS'


# In[182]:


from numpy import array
arr2 = array([
 ['1','1','0','0','1','1','1','1'],
 ['1','0','1','1','1','0','1','1'],
 ['0','1','1','1','0','0','1','0'],
 ['0','1','0','1','0','0','1','1'],
 ['0','1','0','1','0','1','0','1']
])
array_size = len(arr2)
codeword = parity_check(arr2, 2, array_size)
print(codeword)


# ## Test cases for parity validty check

# In[ ]:


# Test case 2
# arr2 = array([
#  ['1','1','0','0','1','1','1','1'],
#  ['1','0','1','1','1','0','1','1'],
#  ['0','1','1','1','0','0','1','0'],
#  ['0','1','0','1','0','0','1','1'],
#  ['0','0','0','0','0','0','0','0']
# ])


# Test case 3
# arr2 = array([
#  ['1','1','0','0','1','1','1','1'],
#  ['1','0','1','1','1','0','1','1'],
#  ['0','1','1','1','0','0','1','0'],
#  ['0','1','0','1','0','0','1','1'],
#  ['1','1','1','0','0','1','0','1']
# ])


# Test case 4
# arr2 = array([
#  ['1','1','0','0','1','1','1'],
#  ['1','0','1','1','1','0','1'],
#  ['0','0','1','1','0','0','1'],
#  ['0','1','0','1','0','0','1'],
#  ['1','1','1','0','0','1','1']
# ])


# Test case 5
# arr2 = array([
#  ['1','1','0','0','1','1','1','1'],
#  ['1','0','1','1','1','0','0','1'],
#  ['0','1','1','1','0','0','1','0'],
#  ['0','1','0','1','0','0','0','1'],
#  ['1','1','0','0','0','0','0','1']
# ])


# Test case 6
# arr2 = array([
#  ['0','1','0','0','1','1','1','1'],
#  ['1','0','1','1','1','0','1','1'],
#  ['0','1','1','1','0','0','1','0'],
#  ['0','1','0','1','0','0','1','1'],
#  ['1','0','1','0','0','1','0','0']
# ])


# Test case 7
# arr2 = array([
#  ['1','1','0','0','0','1','1','1'],
#  ['1','0','1','1','1','0','1','1'],
#  ['0','0','1','1','0','0','1','0'],
#  ['0','1','0','1','0','0','1','1'],
#  ['0','0','0','0','0','1','0','0']
# ])


# Test case 8
# arr2 = array([
#  ['1','1','0','0','1','1','1','1'],
#  ['1','0','1','1','1','0','1','1'],
#  ['0','1','1','1','0','0','1','0'],
#  ['0','1','0','1','0','0','1','1'],
#  ['1','1','1','0','0','0','0','0']
# ])


# Test case 9
# arr2 = array([
#  ['1','1','0','0','1','1','1','1'],
#  ['1','0','1','1','1','0','1','1'],
#  ['0','1','0','1','0','0','0','0'],
#  ['0','1','0','1','0','0','1','1'],
#  ['1','0','0','0','0','1','0','1']
# ])


# Test case 10
# arr2 = array([
#  ['0','1','0','0','1','1','1','1'],
#  ['1','0','1','1','1','0','1','1'],
#  ['0','1','1','1','0','0','1','0'],
#  ['0','1','0','1','0','0','1','1'],
# ])

