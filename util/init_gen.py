import os

top_dir = input("Enter the directory to start scanning from.\n>")

dir_queue = [top_dir]

while(len(dir_queue) > 0):
    cur_dir = dir_queue.pop(0)
    print(cur_dir)
    contents = os.listdir(cur_dir)
    print(contents)
    pymod = []
    for f in contents:
        if(os.path.isdir(cur_dir+"/"+f)):
            dir_queue.append(cur_dir+"/"+f)
        else:
            if(f.endswith(".py") and not f.endswith("__init__.py")):
                pymod.append(f.replace(".py",""))
    print(dir_queue)
    print(pymod)
    with open(cur_dir+"/__init__.py",'w') as init_file:
        init_file.write("__all__ = ")
        init_file.write(pymod.__str__())
