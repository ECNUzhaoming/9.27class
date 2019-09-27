
# coding: utf-8

# In[1]:

a=[1,2,3]
print(a)


# In[2]:

a=list(range(1,11))
print(a)


# In[3]:

print(a(-1))


# In[5]:

print(a[-1])


# In[6]:

3 in a


# In[7]:

"3" in a


# In[1]:

for i in range(0,10):
    print("hello",end=" ")


# In[2]:

print("eqw")


# In[5]:

for i in range(0,10):
  print("+"*(9-i),"*"*(2*i+1),sep='')
    


# In[6]:

a=list(range(1,10))
print(a)
del a[0]
print(a)


# In[7]:

a.clear


# In[9]:

print(a)


# In[11]:

a.clear()
print(a)


# In[14]:

a=list(range(1,4))
b=a
print("a:",a)
print("b:",b)


# In[15]:

del b[0]
print("a:",a)
print("b:",b)


# In[17]:

a=list(range(1,4))
b=a.copy()
print("a:",a)
print("b:",b)


# In[18]:

del b[0]
print("a:",a)
print("b:",b)


# In[19]:

b.append(4)
print("a:",a)
print("b:",b)


# In[20]:

a=[12,3,3,[1,23]]
a[3][0]


# In[22]:

b=a.copy()
print("a:",a)
print("b:",b)


# In[23]:

a[3][0]=3.3
print("a:",a)
print("b:",b)


# In[25]:

from copy import deepcopy
a=[1,2,3,[4,5]]
b=deepcopy(a)
print("a:",a)
print("b:",b)


# In[26]:

a[3][1]=7
print("a:",a)
print("b:",b)


# In[27]:

a=[3,4,6,7,8,3,5,6,6]
a.count(3)


# In[28]:

len(a)


# In[29]:

a.index(3)


# In[30]:

a.index(5)


# In[31]:

a.index(3,2)


# In[32]:

a.insert(2,"*")


# In[33]:

print(a)


# In[34]:

a.remove("*")


# In[35]:

print(a)


# In[37]:

a.pop()
print(a)


# In[ ]:

a="a"
b="b"
print(a+b)


# In[16]:

a+=b
print(a)


# In[17]:

a=[1,2,3]
a.reverse()
print(a)


# In[24]:

import random
value=random.randint(1,6)
print(value)


# In[1]:

expression=input("please input an expression:")
my_stack=list()
left_quotes=["{","[","("]
right_quotes=["}","]",")"]

for ch in expression:
    if ch in left_quotes:
        my_stack.append(ch)
    elif ch in right_quotes:
        if my_stack==[]:
            print("not match")
        else:
            left_ch=my_stack.pop()
            if(left_quotes.index(left_ch)!=right_quotes.index(ch)):
                print("no match")
                break
if my_stack!=[]:
    print("no match")
else:
    print("match")
    


# In[7]:

import random 
a=list()
for i in range(0,20):
  a.append(random.randint(1,6))
    
print(a)
b=a
b.sort()
print(a)
print(b)


# In[10]:

get_ipython().run_cell_magic('timeit', '', 'a=[None]*1000\nfor i in range(0,1000):\n   a[i]=i')


# In[11]:

month=int(input("month"))
day=int(input("day"))
days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
count=day
i=1
while i<month:
    count+=days_in_month[i-1]
    i+=1
print(count)


# In[ ]:

grades=['D']*60+['c']*15+['B']*15+["A"]*11
while True:
    print("Grade=",grades[int(input("sceore"))])


# In[11]:

import random
count=[0]*6
for i in range(0,60):
    value=random.randint(1,6)
    count[value-1]+=1
    i+=1
print(count)


# In[ ]:




# In[12]:

import random
count=0
number_of_test=1000
last_three=[0,0,0]
for i in range(0,number_of_test):
    last_three.append(random.randint(1,6))
    last_three.pop(0)
    if (last_three==[6,6,6]):
        count +=1
print(count,count/number_of_test)


# In[18]:

import random
count=[0]*6
number_of_test=1000
last_three=[0,0,0]
for i in range(0,number_of_test):
    last_three.append(random.randint(1,6))
    last_three.pop(0)
    if(last_three[0]==last_three[1]==last_three[2]):
        count[last_three[2]-1]+=1
print(count)


# In[17]:

#元组tuple是不可变更的list
#没有名字
a=(1,2,3)
a[0]
a=(42,)


# In[ ]:




# In[ ]:



