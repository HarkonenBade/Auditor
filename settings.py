import configparser

DEFAULT_CONFIG_PATH = "./auditor_conf.cfg"
USER_CONFIG_PATH = "~/.config/auditor.cfg"
VERBOSITY = 2 #Debug=2,Verbose=1,None=0

cfg = None
PLUGIN_DIRECTORY = ""
CACHE_DIRECTORY = ""
TREE_LOC = ""
ALLOWED_PATHS = []
DISALLOWED_PATHS = []

def load_config():
    global PLUGIN_DIRECTORY
    global CACHE_DIRECTORY
    global TREE_LOC
    global ALLOWED_PATHS
    global DISALLOWED_PATHS
    global cfg

    cfg = configparser.SafeConfigParser()
    cfg.read([DEFAULT_CONFIG_PATH,USER_CONFIG_PATH,'./auditor_conf_tmp.cfg'])    
    PLUGIN_DIRECTORY = cfg.get("Plugins","plugin_dir")
    CACHE_DIRECTORY = cfg.get("Plugins","cache_dir")
    TREE_LOC = cfg.get("Paths","db_loc")
    ALLOWED_PATHS = cfg.get("Paths","allowed").split(":")
    DISALLOWED_PATHS = cfg.get("Paths","disallowed").split(":")

def store_config():
    cfg.set("Paths","allowed",':'.join(ALLOWED_PATHS))
    cfg.set("Paths","disallowed",':'.join(DISALLOWED_PATHS))
    cfg.set("Paths","db_loc",TREE_LOC)
    cfg.set("Plugins","plugin_dir",PLUGIN_DIRECTORY)
    cfg.set("Plugins","cache_dir",CACHE_DIRECTORY)    
    
    f = open('./auditor_conf_tmp.cfg','w')
    cfg.write(f)
    f.close()

