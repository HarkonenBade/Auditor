import imp

## Basic dynamic loading

name = input("Enter a module name:")
directory = input("Enter a directory to search:")

(file,path,desc) = imp.find_module(name,[directory])

m = imp.load_module(name,file,path,desc)



