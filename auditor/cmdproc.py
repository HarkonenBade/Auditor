cmds = {}
cmds['help'] = lambda : print('This is a help string.')



def cmd_loop(cmds,prompt=">",quitstr="q"):
    inp = input(prompt)
    while inp != quitstr:
        if(inp in cmds):
            cmds[inp]()
        else:
            print("That is not a valid command")
        inp = input(prompt)

if __name__=="__main__":
	cmd_loop(cmds)
