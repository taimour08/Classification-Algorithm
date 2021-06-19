#!/usr/bin/env python
# coding: utf-8

# In[148]:



import pandas as pd
import math


# #### Read dataset from UCI. This is a balance dataset which has a class name and 4 attrbiutes. e.g ['B', 4, 2, 4, 1] 

# In[141]:


df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data",
                names = ["Class Name", "Left-Weight", "Left-Distance","Right-Weight","Right-Distance"])

data = df.to_numpy()



# In[145]:


df.head()


# #### This function recieves the class names of the three lowest distances and prints out the class which our instance of data belongs to

# In[156]:


centroids = [[1,1,4,4], 
            [4,5,1,0], 
            [2,2,2,2]]

def findMostCommon(i1, i2, i3):
    
    a = [i1, i2, i3]
    
    
    L = 0
    R = 0
    B = 0
    
    # Loop to find the common among the 3
    for i in range(0,3):
        
        if (a[i] == 'L'):
            L += 1
        
        if (a[i] == 'R'):
            R += 1
        
        if (a[i] == 'B'):
            B += 1
            
    if B > 1:
        print("Dataset belongs to class B")
    
    if R > 1:
        print("Dataset belongs to class R")
        
    if L > 1:
        print("Dataset belongs to class L")


# In[157]:


def findDistance(i, instance):
        
        global data
        
        n1 = data[i][1] - instance[0]
        n2 = data[i][2] - instance[1]
        n3 = data[i][3] - instance[2]
        n4 = data[i][4] - instance[3]

        d = math.sqrt(pow(n1,2) + pow(n2,2) + pow(n3,2) + pow(n4,2)) # Find distance between our instance 
                                                                     # and the all the elements in the dataset 
        return d    
    


# #### Function to find the K nearest neighbour

# In[158]:



def kNearestNeighbour():

    instance = [1, 1, 5, 4] # The instance of data of which we want to find the class
    low = secondLow = thirdLow = 99
    index1 = index2 = index3 = None
    
    for i in range(0,625):
            
        d = findDistance(i, instance)    
            
        if d < low:
            low = d
            index1 = data[i][0]
            
        elif d < secondLow:
            secondLow = d
            index2 = data[i][0]
            
        elif d < thirdLow:
            thirdLow = d
            index3 = data[i][0]
            
                        
    print("Lowest three:", index1, index2, index3)
    
    findMostCommon(index1, index2, index3)
    
    

        
        
        
        


# In[159]:


kNearestNeighbour()


# ## Find Mean of Data points in Cluster
# ### 1. First loop of size three as three clusters
# ### 2. Length of second loop is the number of points in the current cluster.
# ### - It will add each attribute separately, calculate the mean and store it in an array.
# ### - Then this array containing means will be considered as the new centroid.
# ### - This will be repeated for the 2 other clusters to calculate new centroids.

# In[160]:


cluster = [[], [], []] # Contains all the points in each of the three clusters

def findMean():
    
    # Find mean of datapoints in one cluster. Add all the elements indvidually c[0][0][1] + c[0][1][2] + c[0][1][3] + c[0][4]
    
    for i in range (0, 3):
        
        size = len(cluster[i])
        #print("len: ",size)
        
        # Mean of all elements will be calculated individually
        v1 = v2 = v3 = v4 = 0 
        
       # print("Clus:",cluster[i][2])
        
         
        for j in range(0, size - 1):
            v1 += cluster[i][j][1]
            v2 += cluster[i][j][2]
            v3 += cluster[i][j][3]
            v4 += cluster[i][j][4]
        
        #print (v1)
        #print (v1/size)
             
        # Calculate mean
        v1 = v1 / size
        v2 = v2 / size
        v3 = v3 / size
        v4 = v4 / size
        
        centroids[i] = [v1, v2, v3, v4]
        #print(centroids[i])
        
        
        
        
            
            
            
    
    #print(size)
    


# In[161]:


def clustering():
    
        
    #print(centroids[0])
    
    
    
    for i in range(0, 625): # Number of datapoints 625
        
        low = 20
        index = None
        
        for j in range(0, 3): # 3 as there are three centroids
            d = findDistance(i, centroids[j]) # Return distance bw centroid and datapoint
            #print(d)
            
            if d < low:  # nearest point will be found
                low = d
                index = j  # Index of nearest centroid/Index of cluster
         
        
        cluster[index].append(data[i]) # APPEND IN THE NEAREST CLUSTER
        
    findMean()
    
    print("New centroid 1: ", centroids[0])
    print("New centroid 2: ", centroids[1])
    print("New centroid 3: ", centroids[2])
        
           
    
    


# In[164]:


clustering()
findMean()

#for i in range(0,2):
print("Cus", cluster[0][0])
    


# In[ ]:





# In[ ]:




