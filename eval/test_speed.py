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
cfg.read([sys.argv[1]])

k=cfg.getint("data","k")
t_iter = cfg.getint("data","t_iter")
iterations = cfg.getint("data","iter")
maxval = cfg.getint("data","maxval")
testpath= cfg.get("data","testpath")


pm = plugin_manager.PluginManager('/home/tom/prj/auditor/plugins','')
fData = file_data_tree.FileDataTree()
fScanQ = file_scan_queue.FileScanQueue()
fScan = file_scanner.FileScanner(fScanQ,fData,pm)
per = perceptron_classifier.PerceptronClassifier(fData)

for p in cfg.get("data","plugins").split(":"):
    pm.load(p)

def scank():
    for p,f in fData:
        k_nearest_neighbour.k_nearest_neighbour(path.join(p,f.name),fData,pm,k)

def scanp():
    for p,f in fData:
        per.classify(path.join(p,f.name))
    
def train():
    for i in range(t_iter):
        per.train_all()    

def crawl(p):
    return [path.join(p,n) for n in os.listdir(p) if not path.isdir(path.join(p,n))]+\
        list(\
            itertools.chain.from_iterable(\
                [crawl(path.join(p,n)) for n in os.listdir(p) if path.isdir(path.join(p,n))]))

def gen():
    files = crawl(testpath)
    for i in range(iterations):
        print("ITER:%02d:["%i,end="")
        for t in range(maxval):
            print("*",end="")
            num = 2**t
            samp = random.sample(files, num)
            for f in samp:
                fScanQ.add(f,"attrib_update")
            fData.__init__()
            fScan.scan()
            fData.save("./%02d.%02d.tr"%(t,i))
        print("]")

def test(algo):
    for i in range(iterations):
        print("ITER:%02d:["%i,end="")
        for t in range(maxval):
            print("*",end="")
            fData.load("./%02d.%02d.tr"%(t,i))
            if(algo=="p"):
                cProfile.run("train()","./%02d.%02d.t.log.pro"%(t,i))    
                cProfile.run('scanp()',"./%02d.%02d.p.log.pro"%(t,i))
            else:
                cProfile.run('scank()',"./%02d.%02d.k.log.pro"%(t,i))
        print("]")

def gather():
    with open("data.dat","wt") as out:
        for t in range(maxval):
            out.write("%04d"%(2**t))
            for c in {"k","p","t"}:
                tmp = []
                for i in range(iterations):
                    s = pstats.Stats("./%02d.%02d.%s.log.pro"%(t,i,c))
                    tmp += [s.total_tt]
                avg = sum(tmp)/len(tmp)
                avg = avg/(2**t)
                if(c=="t"):
                    avg = avg/t_iter
                out.write("\t%f"%(avg))
            out.write("\n")

if __name__=="__main__":
    if(sys.argv[2] == "gen"):
        gen()
    elif(sys.argv[2] == "gather"):
        gather()
    else:
        test(sys.argv[3][0:1])
