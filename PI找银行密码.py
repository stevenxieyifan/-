
# coding: utf-8

# In[ ]:


file = open('圆周率100万位.txt','r+')
newfile= open('圆周率100万位2.txt','w+')
for i in file.readlines():
    i = i.replace(' ','')
    i = i.replace('\n','')
    newfile.write(i)
newfile.close()
file.close
p = open('圆周率100万位2.txt','r')
pai = p.read()
pwds = []
for num in range(100000):
    pwds.append("0" * ( - len(str(num))) + str(num))

stat = []
for pwd in pwds:
    x = pai.find(pwd)
    if x == -1:
        break
    stat.append([pwd,x-1])
    
another = open('PI-stat.txt','w')
for data in stat:
    another.write(data[0]+':'+str(data[1])+'\n')

