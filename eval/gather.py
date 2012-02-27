import sys,configparser,subprocess,pstats,math
from auditor import file_data_tree

tname = sys.argv[1]

cfg = configparser.SafeConfigParser()
cfg.read(['../'+tname+".conf"])

klist = [int(k) for k in cfg.get("control","klist").split(":")]

reps = cfg.getint("control","reps")

ofile = open("%s.dat"%tname,"w")

#ofile.write(",".join([""]+["%02d"%k for k in klist]) + "\n")

#clist = ["Correct"]
#flist = ["Fail"]
#mlist = ["Miss"]
for k in klist:
    foo = subprocess.check_output("python ../../res_eval.py ../%s.map %s.%02d.000.log"%(tname,tname,k),shell=True)
    (total,cor,fail,miss) = foo.decode("utf-8")[:-1].split(",")
    total = int(total)
    #clist += ["%f"%(int(cor)/total)]
    #flist += ["%f"%(int(fail)/total)]
    #mlist += ["%f"%(int(miss)/total)]
    ofile.write("%02d\t%f\t%f\t%f\n"%(k,int(cor)/total,int(fail)/total,int(miss)/total))

ofile.write("\n\n")
#ofile.write(",".join(clist) + "\n")
#ofile.write(",".join(flist) + "\n")
#ofile.write(",".join(mlist) + "\n\n\n")


#for i in range(reps):
#	tmp = ["%2d"%i]
#	for k in klist:
#		foo = pstats.Stats("%s.%02d.%03d.log.pro"%(tname,k,i))
#		tmp += ["%f"%foo.total_tt]
#	ofile.write(",".join(tmp) + "\n")

for k in klist:
    tmp = []
    for i in range(reps):
        foo = pstats.Stats("%s.%02d.%03d.log.pro"%(tname,k,i))
        tmp += [foo.total_tt]
    avg = sum(tmp)/len(tmp)
    stddev = math.sqrt(sum([(t-avg)**2 for t in tmp])/len(tmp))
    ofile.write("%02d\t%f\t%f\n"%(k,avg,stddev))

ofile.write("\n\n")    

fd = file_data_tree.FileDataTree()
fd.load(cfg.get("data","db_loc"))

freqs = {}
for p,f in fd:
    if p in freqs:
        freqs[p] += 1
    else:
        freqs[p] = 1

#ofile = open("%s.info"%tname,'wt')

#ofile.write(",AVG FLDR,MIN FLDR,MAX FLDR\n")

fval = freqs.values()
min_folder = min(fval)
max_folder = max(fval)
avg_folder = sum(fval)/len(fval)

for p,f in fd.folder_iter():
    if p in freqs:
        freqs[p] += 1
    else:
        freqs[p] = 1



fval = freqs.values()
min_folder2 = min(fval)
max_folder2 = max(fval)
avg_folder2 = sum(fval)/len(fval)

ofile.write("%f\t%f\t%f\t%f\t%f\t%f\t1"%(avg_folder,avg_folder2,min_folder,min_folder2,max_folder,max_folder2))
ofile.close()
