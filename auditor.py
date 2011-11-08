import configparser

'''Init the config parser. Then load the default and current configs.'''
config = configparser.SafeConfigParser()
config.load(['~/.config/auditor/conf','./auditor_conf.cfg'])
