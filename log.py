import settings

verb_levels={0:"Error:",1:"",2:"Debug:"}

def log(level,msg):
    global verb_levels
    if(settings.VERBOSITY >= level):
        print(verb_levels[level] + msg)
