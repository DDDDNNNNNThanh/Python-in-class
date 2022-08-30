
# Ex1

# 5.2

# In[249]:


test="equal"
print(test=="equal")
print(test!="equal")


# In[250]:


test="equal"
print(test.lower()=="equal")


# In[251]:


val=10
print(val>10)
print(val<10)
print(val<=10)
print(val>=10)


# In[252]:


val=10
print(val==10)
print(val!=10)
if val<=8 and val>=10:
    print(" ..")
    
if val<=8 or val>=10:
    print("---")


# In[253]:


val=[23,24,56,3]
23 in val


# In[254]:


23 not in val


# 5.3

# In[255]:


alien_color='green', 'yellow', 'red'
if "green" in alien_color:
    print("the player just earned 5 points")


# 5.4

# In[256]:


alien_color='green', 'yellow', 'red'
if "green" in alien_color:
    print("the player just earned 5 points")
else :
    print("the player just earned 10 points")


# 5.5

# alien_color='green', 'yellow', 'red'
# if "green" in alien_color:
#     print("the player just earned 5 points")
# elif "yellow" in alien_color :
#     print("the player just earned 10 points")
# elif  "red" in alien_color :
#     print("the player just earned 15 points")

# In[257]:


5.6


# In[ ]:


age=int(input("Age ="))
if age <2:
    print(" the person is a baby")
elif age <4:
    print("the person is a toddler.")
elif age <13:
    print("the person is a kid.")
elif age <20:
    print("the person is a teenager.")
elif age <65:
    print("the person is an adult.")
else:
    print("the person is an elder.")


# 5.7

# In[ ]:


favfruits=["bananas","apple","mango"]
for favfruit in favfruits:
    print(f" my fav fruite is {favfruit}")


# In[ ]:



favfruits=["bananas","apple","mango"]
for favfruit in favfruits:
    if favfruit in "bananas":
        print("i reaaly like bananas")
    elif favfruit in "mango":
        print("i reaaly like mango")
    elif favfruit in "apple":
        print("i reaaly like apple")


# Ex2:

# a

# In[260]:


aTuple = ("Orange", [10, 20,30], (5, 15, 25))
aTuple[1][1]


# b

# In[261]:


example = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')] 
example = [i for i in example if i]
example


# c

# In[262]:


tuple1 = (11, [22, 33], 44, 55)
tuple1 = list(tuple1)
tuple1[1][0]=222
tuple1 = tuple(tuple1)
tuple1


# Ex3

# a

# In[263]:


sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet2 = set(sampleList)
sampleSet3 = sampleSet.union(sampleSet2)
print(sampleSet3)


# b

# In[264]:


set1 = {10, 20, 30, 40, 50}
set1.difference_update({10,20,30})
set1


# Ex4

# In[265]:


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))


# In[266]:


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))


# In[267]:


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.difference_update(set2)
set1


# In[268]:


set1 = {10, 20, 30, 40, 50}
set1.difference_update({30,40,50})
set1


# In[269]:


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))


# Ex5:

# ![image.png](attachment:image.png)

# In[270]:


message2 = '''
Machine learning; (ML) is the study of \ computer algorithms that improve automatically
through# experience. It is seen as a subset of artificial intelligence. Machine learning
algorithms build a mathematical model based on sample data, known as "training data", in
order to make predictions or decisions without being explicitly programmed to do so.
Machine{ learning} algorithms are used in a wide variety of applications, such as email
filtering and computer() vision, where it is difficult or infeasible to develop conventional
algorithms to perform the needed tasks. Machine# learning is closely related to
computational *statistics, which focuses on making predictions! using computers. The
study of mathematical optimization delivers methods, theory and application domains to
the-- field ;of machine learning. Data mining is a related field of study, focusing on
exploratory data analysis through unsupervised learning In its application across business
problems, machine learning is also referred to as predictive analytics.
'''


# In[271]:


special_character = {'.',',',';',':','*','-','!'}
message2 = message2.lower()
for letter in special_character:
    message2 = message2.replace(letter, '')
words  = message2.split()
print(len(words))


# In[272]:


unique_word = set(words)
print(unique_word)
len(unique_word)


# In[273]:


count_word = []
for word in unique_word:
    count_word.append([word,words.count(word)])
print(count_word)


# Ex6:

# ![image.png](attachment:image.png)

# In[289]:


import random
random.seed = 63

women = ['Anh','Chi','Mai']
men = ['Bình','Đức','Mạnh','Minh']
names = women + men
customers = []
for _ in range(200):
    name = random.choice(names)
    age = random.randrange(1,70,5)
    price = random.randrange(100,500,10)
    customers.append((name,age,price))
    
customers


# In[291]:


customer_name_age = []
for i in customers:
    customer_name_age.append(i[0:2])
new_customer_name_age = set(customer_name_age)
new_customer_name_age

for i in new_customer_name_age:
    total_customer_money = 0
    discount = 0
    gift = 0
    for j in customers:
        if j[0:2] == i:
            total_customer_money += j[2]
            if j[1] < 10:
                discount = 0.15
                total_customer_money -= 2
            elif j[1] < 18:
                discount = 0.08
                if j[0] in women:
                    total_customer_money -= 2
            elif j[1] < 23:
                discount = 0.05
                if j[0] in women:
                    total_customer_money -= 2
            elif j[1] < 60:
                discount = 0.02
            else:
                discount = 0.25
                gift = 1
    total_customer_money = total_customer_money - total_customer_money*discount
    print(f"Customer{i} = {total_customer_money}")

# Ex7:

# ![image.png](attachment:image.png)

# $A=2xy+4x+5y+x^2-y^2-5$

# a

# In[295]:


A = '2*x*y + 4*x + 5*y + x**2 - y**2 - 5'
variable = []
for i in A:
    if 'a'<= i and i<='z':
        variable.append(i)
variable = set(variable)
print("The number of variable:",len(variable))

# b

# In[298]:


x = int(input('x = '))
y = int(input('y = '))
result = eval('2*x*y + 4*x + 5*y + x**2 - y**2 - 5')
print('A =',result)


# In[ ]:




