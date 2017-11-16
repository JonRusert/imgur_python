import os
import shutil

nodes =[]
dup = 0
for subdir, dirs, files in os.walk('nodes'):
    for file in files:
        curFile = open(subdir + '/' +file, 'r')
        outLines = []
        i = -1
        for line in curFile:
            line = line.strip()
            if(not line.startswith(',')):
                i +=1
                outLines.append("")
                
            outLines[i] +=line  
        curFile.close()

        newFile = open(subdir + '/' +file + '-new', 'w')
        for j in outLines:
            newFile.write(j + "\n")

        newFile.close()
        

        shutil.copy(subdir + '/' +file + '-new', subdir + '/' +file)
        os.remove(subdir + '/' +file + '-new')
        

