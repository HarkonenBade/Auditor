import sys,configparser,subprocess

tname = sys.argv[1]

cfg = configparser.SafeConfigParser()
cfg.read([tname+".conf"])

klist = [int(k) for k in cfg.get("control","klist").split(":")]

reps = cfg.getint("control","reps")

cfile = open("%s.cor.csv"%tname,"w")
ffile = open("%s.fal.csv"%tname,"w")
mfile = open("%s.mis.csv"%tname,"w")

for k in klist:
    cfile.write(",%02d"%k)
    ffile.write(",%02d"%k)
    mfile.write(",%02d"%k)

cfile.write(",\n")
ffile.write(",\n")
mfile.write(",\n")


for i in range(reps):
    cfile.write("%03d,"%i)
    ffile.write("%03d,"%i)
    mfile.write("%03d,"%i)
    for k in klist:
        foo = subprocess.check_output("python ../res_eval.py %s.map %s.%02d.%03d.log"%(tname,tname,k,i),shell=True)
        (total,cor,fail,miss) = foo.decode("utf-8")[:-1].split(",")
        total = int(total)
        cor = int(cor)
        fail = int(fail)
        miss = int(miss)
        cfile.write("%f,"%(cor/total))
        ffile.write("%f,"%(fail/total))
        mfile.write("%f,"%(miss/total))
    cfile.write("\n")
    ffile.write("\n")
    mfile.write("\n")
cfile.close()
ffile.close()
mfile.close()
