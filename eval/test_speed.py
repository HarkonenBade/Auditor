import sys,cProfile,os,itertools,random,pstats
from os import path
from auditor import *

class flushfile(object):
	def __init__(self, f):
		self.f = f
	def write(self, x):
		self.f.write(x)
		self.f.flush()

sys.stdout = flushfile(sys.stdout)

k=5
iterations = 10
maxval = 12
testpath="/home/tom/testbeds/tstspd"


pm = plugin_manager.PluginManager('/home/tom/prj/auditor/plugins','')
fData = file_data_tree.FileDataTree()
fScanQ = file_scan_queue.FileScanQueue()
fScan = file_scanner.FileScanner(fScanQ,fData,pm)

pm.load("id3_plugin")
pm.load("mime_plugin")
#pm.load("exif_plugin")

def scan(db,logname):
    fData.load(db)
    #with open(logname,"wt") as log:
    for p,f in fData:
        n = k_nearest_neighbour.k_nearest_neighbour(p+'/'+f.name,fData,pm,k)
            #if n != '':
            #    log.write("%s/%s ---> %s\n" % (p,f.name,n))
            #else:
            #    log.write("%s/%s ---> NONE\n" % (p,f.name))

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
                fScanQ.add(f)
            fData.__init__()
            fScan.scan()
            fData.save("./%02d.%02d.tr"%(t,i))
        print("]")

def test():  
    for i in range(iterations):
        print("ITER:%02d:["%i,end="")
        for t in range(maxval):
            print("*",end="")
            cProfile.run('scan("./%02d.%02d.tr","./%02d.%02d.log")'%(t,i,t,i),"./%02d.%02d.log.pro"%(t,i))
        print("]")

def gather():
    with open("data.dat","wt") as out:
        for t in range(maxval):
            tmp = []
            for i in range(iterations):
                s = pstats.Stats("./%02d.%02d.log.pro"%(t,i))
                tmp += [s.total_tt]
            avg = sum(tmp)/len(tmp)
            avg = avg/(2**t)
            out.write("%04d\t%f\n"%(2**t,avg))

if __name__=="__main__":
    if(sys.argv[1] == "gen"):
        gen()
    elif(sys.argv[1] == "gather"):
        gather()
    else:
        test()
