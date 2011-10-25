import imp,os

## Folder based dynamic loading

plugin_dir = input("Enter the plugin directory:")

mod_names = [name for name in os.listdir(plugin_dir) if os.path.isdir(os.path.join(plugin_dir, name))]

print(mod_names)

modules = {}

for name in mod_names:
    (file,path,desc) = imp.find_module(name,[os.path.join(plugin_dir,name)])
    modules[name] = imp.load_module(name,file,path,desc)
    file.close()

print(modules)
