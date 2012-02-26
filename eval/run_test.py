import configparser,sys,subprocess

class flushfile(object):
    def __init__(self, f):
        self.f = f
        self.flush = f.flush
    def write(self, x):
        self.f.write(x)
        try:
            self.f.flush()
        except AttributeError:
            return

sys.stdout = flushfile(sys.stdout)

if(len(sys.argv) != 3):
    print("USAGE: python ../../run_test.py test_name cmd\n\ntest_name:\tname of the test case.\ncmd:\t\tgen - generate the tree and initial map file\n\t\tscan - runs the test and generates appropriate log files.")
    sys.exit(1)

tname = sys.argv[1]
cfg = configparser.SafeConfigParser()
cfg.read(['../'+tname+".conf"])

klist = [int(k) for k in cfg.get("control","klist").split(":")]

reps = cfg.getint("control","reps")

if(sys.argv[2]=="gen"):
    with open("%s.gen.log"%tname,"w") as log:
        subprocess.call("PYTHONPATH=/home/tom/src/stagger-read-only:/home/tom/prj python -mcProfile -o%s.gen.pro.log /home/tom/prj/eval/test_accuracy.py ../%s.conf 1 gen"%(tname,tname),shell=True,stdout=log)
else:
    for i in range(reps):
        print("REP %03d :["%i,end="")
        for k in klist:
            print("*",end="")
            with open("%s.%02d.%03d.log"%(tname,k,i),"w") as log:
                subprocess.call("PYTHONPATH=/home/tom/src/stagger-read-only:/home/tom/prj/ python -mcProfile -o%s.%02d.%03d.log.pro /home/tom/prj/eval/test_accuracy.py ../%s.conf %02d scan"%(tname,k,i,tname,k),shell=True,stdout=log)
        print("]")

