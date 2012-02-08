import sys,configparser,subprocess,pstats

tname = sys.argv[1]

cfg = configparser.SafeConfigParser()
cfg.read([tname+".conf"])

klist = [int(k) for k in cfg.get("control","klist").split(":")]

reps = cfg.getint("control","reps")

ofile = open("%s.csv"%tname,"w")

ofile.write(",".join([""]+["%02d"%k for k in klist]) + "\n")

clist = ["Correct"]
flist = ["Fail"]
mlist = ["Miss"]
for k in klist:
    foo = subprocess.check_output("python ../res_eval.py %s.map %s.%02d.000.log"%(tname,tname,k),shell=True)
    (total,cor,fail,miss) = foo.decode("utf-8")[:-1].split(",")
    total = int(total)
    clist += ["%f"%(int(cor)/total)]
    flist += ["%f"%(int(fail)/total)]
    mlist += ["%f"%(int(miss)/total)]

ofile.write(",".join(clist) + "\n")
ofile.write(",".join(flist) + "\n")
ofile.write(",".join(mlist) + "\n\n\n")


for i in range(reps):
	tmp = ["%2d"%i]
	for k in klist:
		foo = pstats.Stats("%s.%02d.%03d.log.pro"%(tname,k,i))
		tmp += ["%f"%foo.total_tt]
	ofile.write(",".join(tmp) + "\n")

ofile.close()

ofile.close()
