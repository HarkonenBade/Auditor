import sys,cProfile,os,itertools,random,pstats,configparser
from os import path
from auditor import *

class flushfile(object):
    def __init__(self, f):
        self.f = f
        self.flush = f.flush
    def write(self, x):
        self.f.write(x)
        self.f.flush()

sys.stdout = flushfile(sys.stdout)

cfg = configparser.SafeConfigParser()
cfg.read(["../%s.conf"%sys.argv[1]])

t_rep=cfg.getint("control","t_reps")
testpath= cfg.get("data","allowed")


pm = plugin_manager.PluginManager('/home/tom/prj/auditor/plugins','')
fData = file_data_tree.FileDataTree()
fScanQ = file_scan_queue.FileScanQueue()
fScan = file_scanner.FileScanner(fScanQ,fData,pm)
pclass = perceptron_classifier.PerceptronClassifier(fData)


for p in cfg.get("data","plugins").split(":"):
    pm.load(p)

def scan(logname):
    with open(logname,"wt") as lg:            
        pclass.train_all()
        for p,f in fData:
            n = pclass.classify(path.join(p,f.name))
#            print(n)
            if n != []:
                lg.write("%s/%s ---> %s\n" % (p,f.name,":".join(n)))
            else:
                lg.write("%s/%s ---> NONE\n" % (p,f.name))

def crawl(p):
    return [path.join(p,n) for n in os.listdir(p) if not path.isdir(path.join(p,n))]+\
        list(\
            itertools.chain.from_iterable(\
                [crawl(path.join(p,n)) for n in os.listdir(p) if path.isdir(path.join(p,n))]))

def gen():
    files = crawl(testpath)
    for f in samp:
        fScanQ.add(f,"attrib_update")
    dData.__init__()
    Scan.scan()
    fData.save("../%s.tr"%sys.argv[1])

def test():
    fData.load("../%s.tr"%sys.argv[1])  
    for i in range(t_rep):
        print("Training:%02d:"%i)
        cProfile.run('scan("./%02d.log")'%(i),"./%02d.log.pro"%(i))

def gather():
    dirtab = {}
    with open("../%s.map"%sys.argv[1]) as foo:
        for l in foo:
            (i,f) = l[:-1].split(" ---> ")
            dirtab[i] = f

    with open("data.dat","wt") as out:
        for t in range(t_rep):
            total = len(dirtab)
            cor = 0
            fail = 0
            miss = 0
            with open("./%02d.log"%(t)) as foo:
                for l in foo:
                    (i,f) = l[:-1].split(" ---> ")
                    f = f.split(":")
                    if(f == "NONE"):
                        miss+=1
                    else:
                        if(dirtab[i] in f):
                            cor+=1
                        else:
                            fail+=1
                out.write("%02d\t%f\t%f\t%f\n"%(t,cor/total,fail/total,miss/total))

if __name__=="__main__":
    if(sys.argv[2] == "gen"):
        gen()
    elif(sys.argv[2] == "gather"):
        gather()
    else:
        test()
