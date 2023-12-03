import matplotlib.pyplot as plt
import numpy as np

im =  [[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0], 
       [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0], 
       [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1], 
       [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0], 
       [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], 
       [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0], 
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
       [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
       [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
       [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0]]

plt.imshow(np.array(im))
plt.show()

for i in range(len(im)):
    print(im[i])
print('\n')

m = 0

for i in range(len(im)):
       m+=1   
       for j in range(len(im[i])):
           count = i + j
           if (0 < j <= len(im[i])) and (i < len(im) - 1):
               a = im[i][j]
               b = im[i+1][j]
               c = im[i+1][j-1]
               if a == 0 and c == 0 and b != 0:
                    im[i+1][j] = count
                    
               elif a == 0 and b != 0 and c != 0:
                   im[i+1][j] = count
                   if im[i+1][j] > im[i+1][j-1]:
                       im[i+1][j] = im[i+1][j-1] 
                       
               elif a != 0 and b == 0 and c == 0:
                   pass
               
               elif a != 0 and b == 0 and c != 0:
                   im[i+1][j-1] = im[i][j]
                   
               elif a != 0 and b != 0 and c == 0:
                   if im[i][j] > im[i+1][j]:
                      im[i+1][j] = im[i][j]
                      
                   elif im[i][j] == im[i+1][j]:
                        im[i][j] = count
                        im[i+1][j] = im[i][j]
                      
               elif a != 0 and b != 0 and c != 0:
                   if im[i+1][j-1] >= im[i][j]:
                      im[i][j] = im[i+1][j-1]
                      im[i+1][j] = im[i+1][j-1]
                      

               elif a != 0 and b == 0 and c != 0:
                   im[i+1][j-1] = im[i][j]
                   
               elif a != 0 and b != 0 and c == 0:
                   if im[i][j] > im[i+1][j]:
                      im[i+1][j] = im[i][j]
                      
                   elif im[i][j] == im[i+1][j]:
                        im[i][j] = count
                        im[i+1][j] = im[i][j]
                      
               elif a != 0 and b != 0 and c != 0:
                   if im[i+1][j-1] >= im[i][j]:
                      im[i+1][j-1] = im[i][j]
                      im[i+1][j] = im[i+1][j-1]
                      
                   elif im[i+1][j-1] < im[i][j]:
                       im[i][j] = im[i+1][j-1]
                       im[i+1][j] = im[i+1][j-1]
               
data = np.array(im)

for i in range(len(im)):
    print(im[i])

plt.imshow(data)
plt.show()