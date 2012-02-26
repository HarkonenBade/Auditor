import os,sys,random
from auditor import *

lspath = sys.argv[1]
swaps = int(sys.argv[3])
newlist = open(sys.argv[4],"wt")
if(len(sys.argv)>6):
	destination=sys.argv[6]
else:
	destination=""

ft = file_data_tree.FileDataTree()
ft.load(sys.argv[2])

folders = set()
files = []

def com_pref(x,y):
    x = x.split("/")
    y = y.split("/")
    l = max(len(x),len(y))
    for a,b,i in zip(x,y,range(l)):
        if a!=b:
            return "/".join(x[:i])
    return "/".join(x)

with open(lspath,"rt") as f:
    for l in f:
        l = l.rstrip()
        files += [l]
        folders.add(os.path.dirname(l))

extras = set()

for f1 in folders:
    for f2 in folders:
        t = com_pref(f1,f2)

        if(t not in folders):   
            extras.add(t)        
    
folders = list(folders | extras)

fileswaps = random.sample(files,swaps)

for f in files:
    if(f in fileswaps):
        dest = random.choice(folders) if destination=="" else destination
        newlist.write("%s ---> %s\n"%(f,dest))
        of = ft.get(f)
        ft.remove(f)
        newname = os.path.join(dest,os.path.basename(f))
        ft.add(newname)
        nf = ft.get(newname)
        nf.attributes = of.attributes
        nf.last_scanned = of.last_scanned
    else:
        newlist.write("%s ---> %s\n"%(f,os.path.dirname(f)))

ft.save(sys.argv[5])
newlist.close()


