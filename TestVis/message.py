import matplotlib.pyplot as plt
import numpy as np

im =[[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
     [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
     [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
     [0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
     [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0,0, 0, 0,  0]]

im1 =[[0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1]]



for i in range(len(im)):
    print(im[i])
print('\n')

count = 1

#print(len(im), len(im[i]))

for i in range(len(im)):
       for j in range(len(im[i])):
            print(i, j)
            if (i - 1 >= 0) and (j - 1 >= 0) and (i + 1 < len(im)) and (j + 1 < len(im[i])):
                A0 = im[i][j]
                A1 = im[i][j+1]
                A2 = im[i+1][j+1]
                A3 = im[i+1][j]
                A4 = im[i+1][j-1]
                A5 = im[i][j-1]
                A6 = im[i-1][j-1]
                A7 = im[i-1][j]
                A8 = im[i-1][j+1]
                if (A0 != 0):
                    if (A5 != 0) or (A7 != 0):
                        if (A7 != 0):
                            im[i][j] = A7
                        if (A5 != 0):
                            im[i][j] = A5
                    if((A8 != 0) and (A1 != 0)) or ((A6 != 0) and (A5 != 0)):
                        print("-")
                        if (A1 != 0):
                            im[i][j] = A8
                        else:
                            im[i][j] = A6
                    elif ((A5 == 0) and (A7 == 0) and (A6 != 0) and (A8 == 0) and (A1 == 0)) or ((A5 == 0) and (A7 == 0) and (A6 == 0) and (A8 != 0) and (A1 == 0)):
                        im[i][j] = count
                        count += 1 
                    elif ((A5 == 0) and (A6 == 0) and (A7 == 0) and (A8 == 0)):
                        im[i][j] = count
                        count += 1
                    elif ((A5 == 0) and (A7 == 0) and (A6 != 0)):
                        im[i][j] = count
                        count += 1
                    elif ((A5 == 0) and (A7 == 0) and (A6 == 0) and (A8 == 0)) and (A1 !=0):
                         im[i][j] = count-1
                        
                        
            else:     
                if ((i - 1 < 0) or (i + 1 == len(im))) and (not(j - 1 < 0) and (not(j + 1 == len(im[i])))):
                    if (i - 1 < 0):
                        A0 = im[i][j]
                        A1 = im[i][j-1]
                        if(A0 != 0) and (i == 0) and (j == 0):
                            im[i][j] = count
                            count += 1
                        elif (A0 != 0) and (A1 == 0):
                            im[i][j] = count
                            count += 1
                        elif(A0 != 0) and (A1 != 0):
                            im[i][j] = A1
                    else:
                        A0 = im[i][j]
                        A1 = im[i][j-1]
                        A2 = im[i-1][j-1]
                        A3 = im[i-1][j]
                        A4 = im[i-1][j+1]
                        A5 = im[i][j+1]
                        if (A0 != 0):
                            if(A1 != 0):
                                im[i][j] = im[i][j-1]
                            elif(A3 != 0):
                                im[i][j] = im[i-1][j]
                            elif(A3 == 0) and (A1 == 0) and (A2 != 0):
                                im[i][j] = count
                                count += 1
                        
                        
                        
                elif((j - 1 < 0) or (j + 1 == len(im[i]))) and (not(i - 1 < 0) or (not(i + 1 == len(im)))):
                    if (j - 1 < 0):
                        A0 = im[i][j]
                        A1 = im[i-1][j]
                        A2 = im[i-1][j+1]
                        A3 = im[i][j+1]
                        if(A0 != 0):
                            if(A1 != 0):
                                im[i][j] = im[i-1][j]
                            elif((A1 == 0) and (A2 != 0) and (A3 == 0)) or ((A1 == 0) and (A2 == 0)):
                                im[i][j] = count
                                count += 1
                            elif(A1 == 0) and (A2 != 0) and (A3 != 0):
                                im[i][j] = im[i-1][j+1]
                    else:
                        A0 = im[i][j]
                        A1 = im[i-1][j]
                        A2 = im[i-1][j-1]
                        A3 = im[i][j-1]
                        if(A0 != 0):
                            if(A1 != 0) or (A3 != 0):
                                if(A1 != 0):
                                    im[i][j] = im[i-1][j]
                                else:
                                    im[i][j] = im[i][j-1]
                            elif(A1 == 0) and (A2 != 0) and (A3 == 0):
                                im[i][j] = count
                                count += 1
                            elif(A1 == 0) and (A2 == 0) and (A3 == 0):
                                im[i][j] = count
                                count += 1
                            elif(A1 == 0) and (A2 != 0) and (A3 != 0):
                                im[i][j] = im[i-1][j-1]
                            
                            
                elif((i == 0) and (j == 0)) or ((i == 0) and (j == len(im[i]) - 1)) or ((i == len(im) - 1) and (j == 0)) or ((i == len(im) - 1) and (j == len(im[i]) - 1)):
                    A0 = im[i][j]
                    if (A0 != 0):
                        if(i == 0) and (j == 0):
                            im[i][j] = count
                            count += 1
                        elif(i == 0) and (j == len(im[i])):
                            if(im[i][j-1] == 0):
                                im[i][j] = count
                                count += 1
                            else:
                                im[i][j] = im[i][j-1]
                        elif(i == len(im)) and (j == 0):
                            if((im[i][j+1] != 0) and (im[i-1][j+1] != 0)):
                                im[i][j] == im[i-1][j+1]
                            elif(im[i-1][j] != 0):
                                im[i][j] = im[i-1][j]
                            else:
                                im[i][j] = count
                                count += 1
                        elif(i == len(im) and (j == len(im[i]))):
                            if(im[i][j-1] != 0):
                                im[i][j] = im[i][j-1]
                            elif(im[i-1][j] != 0):
                                im[i][j] = im[i-1][j]
                            else:
                                im[i][j] = count
                                count += 1
            print(count)
                            
for i in range(len(im)):
       for j in range(len(im[i])):
            print(i, j)
            if (i - 1 >= 0) and (j - 1 >= 0) and (i + 1 < len(im)) and (j + 1 < len(im[i])):
                A1 = im[i][j]
                A2 = im[i][j+1]
                if A2 != 0 and A1 > 0:
                    if A2 != A1:
                        im[i][j] = im[i][j+1]
               
data = np.array(im)

for i in range(len(im)):
    print(im[i])

plt.imshow(data)
plt.show()