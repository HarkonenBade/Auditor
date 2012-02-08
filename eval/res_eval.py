import re,sys

dirtab = {}
with open(sys.argv[1]) as foo:
	for l in foo:
		(i,f) = l[:-1].split(" ---> ")
		dirtab[i] = f

total = len(dirtab)
cor = 0
fail = 0
miss = 0
with open(sys.argv[2]) as foo:
	for l in foo:
		(i,f) = l[:-1].split(" ---> ")
		if(f == "NONE"):
			miss+=1
		else:
			if(dirtab[i]==f):
				cor+=1
			else:
				fail+=1
if(cor+miss+fail != total):
	print("ERROR: File quantity missmatch. Correct+Missed+Failed is not the same as total.")
else:
	print("%d,%d,%d,%d"%(total,cor,fail,miss))
