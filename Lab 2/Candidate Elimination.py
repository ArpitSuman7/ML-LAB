import numpy as np
import pandas as pd
data = pd.read_csv('/content/data.csv')
concepts = np.array(data.iloc[:,0:-1])
print("\nInstances:\n",concepts)
target = np.array(data.iloc[:,-1])
print("\nTarget Values: ",target)
def learn(concepts, target):
    sh = concepts[0].copy()
    print("\nInitialization of specific and genearal hypothesis")
    print("\nSpecific boundary: ", sh)
    gh = [["?" for i in range(len(sh))] for i in range(len(sh))]
    print("\nGeneric boundary: ",gh)  
    for i, h in enumerate(concepts):
        print("\nInstance", i+1 , "is ", h)
        if target[i] == "yes":
            print("Instance is positive ")
            for x in range(len(sh)):
                if h[x]!= sh[x]:                    
                    sh[x] ='?'                    
                    gh[x][x] ='?'       
        if target[i] == "no":            
            print("Instance is negative ")
            for x in range(len(sh)):
                if h[x]!= sh[x]:                    
                    gh[x][x] = sh[x]                
                else:                    
                    gh[x][x] = '?'        
        print("Specific boundary after ", i+1, "instance is ", sh)        
        print("Generic boundary after ", i+1, "instance is ", gh)
        print("\n")
    indices = [i for i, val in enumerate(gh) if val == ['?', '?', '?', '?', '?', '?']]    
    for i in indices:  
        gh.remove(['?', '?', '?', '?', '?', '?'])
    return sh, gh
sf, gf = learn(concepts, target)
print("Final specific hypothesis: ", sf, sep="\n")
print("Final general hypothesis: ", gf, sep="\n")
