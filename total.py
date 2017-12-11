import os

nodes =[]
dup = 0
f = []
fdup = 0

for subdir, dirs, files in os.walk('nodes'):
    for file in files:
        url = file.split('-')[3]
        if url not in f:
            f.append(url)
        else:
            fdup +=1
            
        curFile = open(subdir + '/' +file, 'r')
        for line in curFile:
            line = line.replace(',', ' ')
            L = line.split()           
            for l in L:
                clean = l.strip()
                if clean not in nodes:
                    nodes.append(clean)
                else:
                    dup+=1

        curFile.close()


print("unique: %d" % len(nodes))
print("dup: %d" % dup)
print("unique files: %d" % len(f))
print("fdup: %d" % fdup) 
