import os


path =
files= os.listdir(path)
s = []
for file in files:
    if not os.path.isdir(file)
        f = open(path+"/"+file)
        lines = f.readlines(2)
        s.append(float(lines[-1]))

