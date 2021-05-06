import os
def rename():
  i=0
  path=input("Enter the location of directory: ")
  path=path+'/'
  for file in os.listdir(path):
    name="image"+str(i)+'.jpg'
    source=path+file
    destination=path+destination
    os.rename(source,destination)
    i+=1
if name=='__main__':
  rename()
  
  
  
  
