import os

def rename():
  i=0
  #Taking the path input from user
  path=input("Enter the location of directory: ")
  path=path+'/'
  
  #Iterating over the files in the directory
  for file in os.listdir(path):
    #Setting the new name for the file
    name="image"+str(i)+'.jpg'
    source=path+file
    destination=path+destination
    #Renaming the file name
    os.rename(source,destination)
    i+=1
    
#Driver code
if name=='__main__':
  rename()
  
  
  
  
