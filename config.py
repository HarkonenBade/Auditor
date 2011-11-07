'''Wrapper class to hold a ConfigParser object responsible for the config files of the program'''

import os,configparser

parser = configparser.SafeConfigParser()


def load_config(filenames):
    '''Loads a list of config files.'''
    parser.read(filenames)

def save_config(filename):
    '''Saves the current config to the specified file.'''
    with open(filename,'w') as configfile:
        parser.write(configfile)

def get_value(section,name):
    '''Retrieves a given value from the config file.'''
    parser.get(section,name)

def add_section(section):
    '''Adds a new section to the config file.'''
    parser.add_section(section)

def set_value(section,name,value):
    '''Sets a value in the config file.'''
    parser.set(section,name,value)

