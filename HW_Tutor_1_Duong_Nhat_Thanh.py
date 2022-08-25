# Dương Nhật Thành

# 11219287

# DSEB 63

# Ex1:

# ![image.png](attachment:image.png)

# In[5]:


n = int(input("n (even number) = "))
a = int(input("a = "))
b = int(input("b = "))
step = [x/n for x in range(n*a,n*b+1)]
h = (b-a)/n
res = h/3*(1/a+1/b)
x0 = a
for i in range(n//2):
    x_odd= x0 + (2*i-1)*h/3
    x_even= x0 + (2*i)*h/3
    res = res + 4*1/x_odd + 2*1/x_even
print(res)
    


# Ex2:

# ![image.png](attachment:image.png)

# In[58]:


card_number = input("Please input card number:")
digits = [int(d) for d in str(card_number)]
odd_digits = digits[-1::-2]
even_digits = digits[-2::-2]
checksum = 0
checksum += sum(odd_digits)
for d in even_digits:
    d = d*2
    if d>=10:
        d = d//10 + d%10
    checksum += d
print('Valid') if checksum%10==0 else print('Invalid')


# Ex3:

# ![image.png](attachment:image.png)

# In[62]:


x = int(input("Please enter x ="))
n = int(input("Please enter n ="))
sum = 0
for i in range(1,n+1):
    sum += i*(x**(i-1))
print(sum)


# Ex4:

# ![image.png](attachment:image.png)
# 

# $A(x,y)=x^2+4x+y^2+7x-5$

# In[63]:


x = int(input("Please enter x="))
y = int(input("Please enter y="))
A = x**2+4*x+y**2+7*x-5
print(A)


# In[ ]:




