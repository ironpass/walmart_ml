
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsRegressor


# In[3]:


csv = np.genfromtxt('train.csv', delimiter=",", dtype = '1int,1int,S10,1float,1bool', names=True)
testcsv = np.genfromtxt('test.csv', delimiter=",", dtype = '1int,1int,S10,1bool', names=True)


# In[4]:


# Construct training data
store = []*len(csv)
dept = []*len(csv)
date = []*len(csv)
sales = []*len(csv)
holiday = []*len(csv)
trainData = []*len(csv)
i = 0
while i < len(csv):
    store.append(csv[i][0])
    dept.append(csv[i][1])
    date.append(csv[i][2])
    sales.append(csv[i][3])
    holiday.append(csv[i][4])
    holidayInp = 1
    if csv[i][4]!=True:
        holidayInp = -1
    dateStr = str(csv[i][2]).split("-")
    dateInp = int(dateStr[1])+(int(dateStr[2][0:2])/100)
    trainData.append([store[i],dept[i],dateInp,holidayInp])
    i+=1


# In[5]:


# Construct testing data
storeTest = []*len(csv)
deptTest = []*len(csv)
dateTest = []*len(csv)
salesTest = []*len(csv)
holidayTest = []*len(csv)
testData = []*len(csv)
j = 0
while j < len(testcsv):
    storeTest.append(testcsv[j][0])
    deptTest.append(testcsv[j][1])
    dateTest.append(testcsv[j][2])
    holidayTest.append(testcsv[j][3])
    holidayTestInp = 1
    if testcsv[j][3]!=True:
        holidayTestInp = -1
    dateTestStr = str(testcsv[j][2]).split("-")
    dateTestInp = int(dateTestStr[1])+(int(dateTestStr[2][0:2])/100)
    testData.append([storeTest[j],deptTest[j],dateTestInp,holidayTestInp])
    j+=1


# In[8]:


# Train model
neigh = KNeighborsRegressor(n_neighbors=5,weights='distance')
neigh.fit(trainData, sales)
KNeighborsRegressor(...)


# In[9]:


# Write a csv file
file_object = open("C:/Users/Ood/Desktop/kagglesubmit.csv","w")
file_object.write("Id,Weekly_Sales\n");

classAttr = []*len(testcsv)
j = 0
while j<len(testcsv):
    classAttr.append(neigh.predict([testData[j]]))
    writeStr = str(storeTest[j])+"_"+str(deptTest[j])+"_"+str(dateTest[j])[2:-1]+","+str(classAttr[j])[1:-1]+"\n"
    file_object.write(writeStr)
    j+=1
file_object.close()


# In[60]:


# Visualization
plt.scatter(sales,date, c='blue', s=5.0, alpha=0.5)
plt.scatter(classAttr,dateTest, c='red', s=5.0, alpha=0.5)


# In[69]:


# Another visualization
plt.scatter(deptTest,classAttr, c='orange')
plt.scatter(dept,sales, c='blue', alpha=0.05)

