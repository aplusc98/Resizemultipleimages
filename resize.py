#This python script needs to be initialized with the main directory containing the images
import os

dataset_path = "PATH"  #replace PATH with the actual path of the directory
       

#################################################
for a in os.listdir(dataset_path):                    #1
    a_path = os.path.join(dataset_path, alphabet)     #2
    os.chdir(a_path)
    os.system('mogrify -resize 105x105 *.jpg') #change picture format if necessary and specify dimensions accordingly
################################################    

# if more subfolders are present then repeat 1 and 2 in nested format
