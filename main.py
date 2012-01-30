import configparser
from auditor import *
import os
from os import path

'''Init the config parser. Then load the default and current configs.'''
config = configparser.SafeConfigParser()
config.read(['~/.config/auditor/conf','./auditor_conf.cfg','./auditor_conf_tmp.cfg'])

#print("Enter the plugin directory")
#pDir = input(">")
pDir = config.get("Plugins","plugin_dir")
pCache = config.get("Plugins","cache_dir")

pm = plugin_manager.PluginManager(pDir,pCache)
ini = inotify_interface.INotifyInterface(100)
fData = file_data_tree.FileDataTree()
fScanQ = file_scan_queue.FileScanQueue()
fScan = file_scanner.FileScanner(fScanQ,fData,pm)
evHan = event_handler.EventHandler(fScanQ,fData)

ini.setHandler(evHan.process)
pm.loadAll()

def inote_scan():
    global ini
    print("iNotify Scanning...")
    ini.scan()
    print("iNotify Scan Complete.")

def fscan_scan():
    global fScan
    print("File Scanning..")
    fScan.scan()
    print("File Scan Complete.")

def path_add():
    al = []
    dis = []
    tmp = ""
    while True:
        print("Enter more allowed paths.")
        tmp = input(">")
        if(tmp != ""):
            al = al+[tmp]
        else:
            break
    while True:
        print("Enter more disallowed paths.")
        tmp = input(">")
        if(tmp != ""):
            dis = dis+[tmp]
        else:
            break
    scan(al,dis)

def k_near():
    global fData
    global pm
    print("Enter a file name to eval.")
    foo = input(">")
    print(k_nearest_neighbour.k_nearest_neighbour(foo,fData,pm,4))

def print_attr():
    global fData
    print("Enter a file.")
    foo = input(">")
    print(fData.get(foo).attributes)

def scan(allowed,disallowed,iNoteAdd = True):
    global fScanQ
    global ini
    for p in allowed:
        p = path.abspath(p)
        if(not p in disallowed and not path.basename(p).startswith('.')):
            if(iNoteAdd):
                ini.startWatch(p,recDir=False)
            cont = os.listdir(p)
            cont = [p+'/'+k for k in cont]
            allowed.extend([k for k in cont if path.isdir(k)])
            [fScanQ.add(k) for k in cont if not path.isdir(k)]            
            
allowed = config.get("Paths","allowed").split(":")
disallowed = config.get("Paths","disallowed").split(":")
scan(allowed,disallowed)
fScan.scan()

cmds = {
    'iscan': inote_scan,
    'fscan': fscan_scan,
    'addpath': path_add,
    'knear' : k_near,
    'pattr' : print_attr
}

cmdproc.cmd_loop(cmds)

config.set("Paths","allowed",':'.join(allowed))
config.set("Paths","disallowed",':'.join(disallowed))

f = open('./auditor_conf_tmp.cfg','w')
config.write(f)
f.close()
