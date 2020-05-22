#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dictionary functions
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)


# In[2]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x) 


# In[3]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car) 


# In[4]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x) 


# In[15]:


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car) 


# In[18]:



#creation of student record table
import statistics
mydict={"name":['amala','serita','emili','hereena'],
        "age":[22,21,21,21],
        "marks1":[86,86,83,86],
        "marks2":[78,72,69,72],
        "marks3":[91,90,90,98]}
# to print the whole dict
for i in mydict:
    print(mydict[i])
print("\n")

#to print the values of the key:marks2
a=mydict.get('marks2')
print(a)

#code to find average marks
b=0
for i in a:
    b=b+i
print(b)
average=b/len(a)
print("Average is ",average)

#to find median
a.sort()
median1=statistics.median(a)
print("Median is ",median1)                              
#if len(a)%2==0:
#median=a[len(a/2)]+a[len(a/2+1)]


# In[24]:


#to find mode
mode1=statistics.mode(a3)
print(mode1)
 mydict.add("total":)


# In[26]:



mydict['Total of marks 2 of all students']=b

for i in mydict:
    print(mydict[i])



#copy function
newdict=mydict.copy()
#print("New dict is ",newdict)


#items() function
itemss=newdict.items()
#print(itemss)

#pop() function

newdict.pop("age")
for i in newdict:
    print(newdict[i])
   
#get function

newa=newdict.get('marks3')
print("Marks 3 is",newa)

#mydict.clear() function

newdict.clear()
print(newdict)


# In[ ]:




