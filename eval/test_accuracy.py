import os,configparser,sys
from os import path
from auditor import *

def scan(allowed,disallowed,iNoteAdd = True):
    global fScanQ
    global ini
    pathlist = []
    pathlist.extend(allowed)
    for p in pathlist:
        p = path.abspath(p)
        if(not p in disallowed and not path.basename(p).startswith('.')):
            cont = os.listdir(p)
            print(cont)
            cont = [path.join(p,k) for k in cont]
            for k in cont:
                if path.isdir(k):
                    print(k)
                    pathlist.extend([k])
                else:
                    print(k)
                    f = fData.get(k)
                    if(f==None or f.last_scanned < os.stat(k).st_ctime):
                        fScanQ.add(k,"attrib_update") 

cfg = configparser.SafeConfigParser()
cfg.read([sys.argv[1]])

pm = plugin_manager.PluginManager('/home/tom/prj/auditor/plugins','')
fData = file_data_tree.FileDataTree()
fScanQ = file_scan_queue.FileScanQueue()
fScan = file_scanner.FileScanner(fScanQ,fData,pm)


for p in cfg.get("data","plugins").split(":"):
    pm.load(p)

if(sys.argv[3] == "gen"):
    print("GENERATING .TR FILE")
    scan(cfg.get("data","allowed").split(":"),cfg.get("data","disallowed").split(":"))
    fScan.scan()
    with open(cfg.get("data","listing"),"w") as ls:
        for p,f in fData:
            ls.write("%s/%s\n" % (p,f.name))
    fData.save(cfg.get("data","db_loc"))
    print("TREE GENERATION COMPLETE, DATA SAVED")
else:
    fData.load(cfg.get("data","db_loc"))
    k = int(sys.argv[2])
    for p,f in fData:
        n = k_nearest_neighbour.k_nearest_neighbour(path.join(p,f.name),fData,pm,k)
        if n != '':
            print("%s/%s ---> %s" % (p,f.name,n))
        else:
            print("%s/%s ---> NONE" % (p,f.name))
