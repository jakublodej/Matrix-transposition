
# coding: utf-8

# In[1]:


m=int(input("Enter Number of Rows :"))
n=int(input("Enter number of Columns :"))
Mat=[]
for i in range(0,n):
    Mat.append([])
for i in range (0,m):
    for j in range(0,n):
        Mat[i].append(j)
        Mat[i][j]==0
for i in range (0,m):
    for j in range (0,n):
        print ('Entry in row:',i+1, ' column: ',j+1)
        Mat[i][j]=int(input())
print(Mat)

ask=input("Transpose it ? : Yes or No: ").lower().startswith('y')
print (ask)
if ask == True :
    result = [[Mat[j][i] for j in range(len(Mat))] for i in range(len(Mat[0]))]

    for r in result:
        print(r)
else:
    pass

