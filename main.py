import os,argparse,settings,string
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
settings.load_config()
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

def inote_scan(a):
    print("iNotify Scanning...")
    ini.scan()
    print("iNotify Scan Complete.")
inote_scan.desc = "Forces an iNotify update."

def fscan_scan(a):
    print("File Scanning..")
    fScan.scan()
    print("File Scan Complete.")
fscan_scan.desc = "Forces a file scan queue update."

def k_near(a):
    try:
        i = a.rindex(" ")
        f = a[:i]
        k = a[i+1:]
        k = int(k)
    except ValueError:
        print("USAGE: knear path k")
    if(path.isfile(f)):
        print("Scanning.")
        print(k_nearest_neighbour.k_nearest_neighbour(f,fData,pm,k))
    else:
        print("USAGE: knear path k")
k_near.desc = "Performs a k-nearest-neighbour scan on a file."

def info(a):
    f = fData.get(a)    
    if(f):
        print("Name: %s"%f.name)
        print("Last Scanned: %s"%str(f.last_scanned))
        print("Type: %s"%f.type)
        if(f.type == "folder"):
            print("Children: %s"%str(f.children))
        else:
            print("Attributes: %s"%str(f.attributes))
    else:
        print("USAGE: info path")
info.desc = "Prints data on a file."

def reload_plugins(a):
    print("Unloading existing plugins.")
    pm.deinit()
    print("Updating directories.")
    pm.__init__(settings.PLUGIN_DIRECTORY,settings.CACHE_DIRECTORY)
    print("Loading new plugins.")
    pm.loadAll()
reload_plugins.desc = "Updates plugin related directories and reloads all plugins."

def change_plugin_dir(a):
    if(path.isdir(a)):
        print("Plugin directory changed to: %s"%a)
        settings.PLUGIN_DIRECTORY = a
    else:
        print("USAGE: chpdir path")
change_plugin_dir.desc = "Changes the plugin directories location."

def change_cache_dir(a):
    if(path.isdir(a)):
        print("Cache directory changed to: %s"%a)
        settings.CACHE_DIRECTORY = a
    else:
        print("USAGE: chcdir path")
change_cache_dir.desc = "Changes the plugin cache directories location."

def help_print(a):
    for k in cmds:
        print("%s: %s"%(k,cmds[k].desc))
help_print.desc = "Prints out this help message."

cmds = {
    'help': help_print,
    'iscan': inote_scan,
    'fscan': fscan_scan,
    'knear' : k_near,
    'info' : info,
    'chpdir': change_plugin_dir,
    'chcdir': change_cache_dir,
    'reload_plugins': reload_plugins
}

cmdproc.cmd_loop(cmds)

fData.save(settings.TREE_LOC)
log(1,"File tree saved.")

settings.store_config()
log(1,"Config saved.")
