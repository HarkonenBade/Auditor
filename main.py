import configparser,os,argparse,settings
from auditor import *
from os import path
from log import log

def parse_args():
    parser = argparse.ArgumentParser(description="A program to organise your file system.")
    parser.add_argument("-c","--config",nargs=1,help="Location of config file.")
    parser.add_argument("-v",action='store_true',help="Verbose output.")
    parser.add_argument("-vv",action='store_true',help="Debug output.")
    
    args=parser.parse_args()
    
    if(args.v):
        settings.VERBOSITY=1
    
    if(args.vv):
        settings.VERBOSITY=2
    
    if(args.config != None):
        settings.USER_CONFIG_PATH=args.config
        log(2,"Config path set to :"+args.config)

def load_config():
    config = configparser.SafeConfigParser()
    config.read([settings.DEFAULT_CONFIG_PATH,settings.USER_CONFIG_PATH,'./auditor_conf_tmp.cfg'])
    
    settings.PLUGIN_DIRECTORY = config.get("Plugins","plugin_dir")
    settings.CACHE_DIRECTORY = config.get("Plugins","cache_dir")
    settings.TREE_LOC = config.get("Paths","db_loc")
    settings.ALLOWED_PATHS = config.get("Paths","allowed").split(":")
    settings.DISALLOWED_PATHS = config.get("Paths","disallowed").split(":")
    return config

def store_config(config):
    config.set("Paths","allowed",':'.join(settings.ALLOWED_PATHS))
    config.set("Paths","disallowed",':'.join(settings.DISALLOWED_PATHS))
    
    f = open('./auditor_conf_tmp.cfg','w')
    config.write(f)
    f.close()
    
def scan(allowed,disallowed,iNoteAdd = True):
    global fScanQ
    global ini
    pathlist = []
    pathlist.extend(allowed)
    for p in pathlist:
        p = path.abspath(p)
        if(not p in disallowed and not path.basename(p).startswith('.')):
            if(iNoteAdd):
                ini.startWatch(p,recDir=False)
            cont = os.listdir(p)
            #print(cont)
            cont = [path.join(p,k) for k in cont]
            for k in cont:
                if path.isdir(k):
                    #print(k)
                    pathlist.extend([k])
                else:
                    #print(k)
                    f = fData.get(k)
                    if(f==None or f.last_scanned < os.stat(k).st_ctime):
                        fScanQ.add(k,"attrib_update") 

        
'''Parse any command line arguments.'''
parse_args()
log(1,"Parsed command line arguments.")

'''Init the config parser. Then load the default and current configs.'''
cfg = load_config()
log(1,"Config data loaded.")


pm = plugin_manager.PluginManager(settings.PLUGIN_DIRECTORY,settings.CACHE_DIRECTORY)
log(1,"Plugin manager loaded.")
ini = inotify_interface.INotifyInterface(100)
log(1,"iNotify interface initialised.")
fData = file_data_tree.FileDataTree()
fScanQ = file_scan_queue.FileScanQueue()
fScan = file_scanner.FileScanner(fScanQ,fData,pm)
evHan = event_handler.EventHandler(fScanQ,fData)
log(1,"File data chain loaded.")

ini.setHandler(evHan.process)
pm.loadAll()
log(1,"Plugins loaded.")

fData.load(settings.TREE_LOC)
log(1,"Tree data loaded from file.")

scan(settings.ALLOWED_PATHS,settings.DISALLOWED_PATHS)
fScan.scan()
log(1,"File data updated for edits since last load.")

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

def save_tree():
    global fData
    print("Enter a file to save to.")
    foo = input(">")
    fData.save(foo)

def load_tree():
    global fData
    print("Enter a file to load from.")
    foo = input(">")
    fData.load(foo)


cmds = {
    'iscan': inote_scan,
    'fscan': fscan_scan,
    'addpath': path_add,
    'knear' : k_near,
    'pattr' : print_attr,
    'savetree': save_tree,
    'loadtree': load_tree
}

cmdproc.cmd_loop(cmds)

fData.save(settings.TREE_LOC)
log(1,"File tree saved.")

store_config(cfg)
log(1,"Config saved.")
