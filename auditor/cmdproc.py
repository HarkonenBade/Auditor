import threading,time,queue

cmds = {}
cmds['help'] = lambda x: print('This is a help string.')
cmds['lower'] = lambda x: print(x.lower())
cmds['upper'] = lambda x: print(x.upper())


class CMDThread(threading.Thread):
    def __init__(self,prompt,quitstr,q,l):
        self.queue = q
        self.lock = l        
        self.prompt=prompt
        self.quitstr=quitstr
        threading.Thread.__init__(self)
        self.daemon=True
    
    def run(self):
        running = True    
        while running:
            inp = input(self.prompt)
            (c,_,a) = inp.partition(" ")
                    
            if(c == self.quitstr):
                running=False
            else:
                self.lock.acquire()
                self.queue.put_nowait((c,a))
                self.lock.release()

class ThreadedCmdLoop():
    def __init__(self,cmds,prompt=">",quitstr="q"):
        self.cmds = cmds        
        self.prompt = prompt
        self.queue = queue.Queue()
        self.lock = threading.Lock()
        self.cmd_gather = CMDThread(prompt,quitstr,self.queue,self.lock)
    
    def start(self):
        self.cmd_gather.start()
    
    def gather_live(self):
        return self.cmd_gather.is_alive()
    
    def run_commands(self,n=1):
        self.lock.acquire()
        for t in range(n):
            try:
                c,a = self.queue.get_nowait()
                if(c in self.cmds):                
                    self.cmds[c](a)
                elif(c != ''):
                    print("%s is not a valid command."%c)
            except queue.Empty:
                self.lock.release()
                return t
        self.lock.release()
        return n

def cmd_loop(cmds,prompt=">",quitstr="q"):
    running = True    
    while running:
        inp = input(prompt)
        (c,_,a) = inp.partition(" ")
                
        if(c == quitstr):
            running=False
        elif(c in cmds):
            cmds[c](a)
        else:
            print("%s is not a valid command"%c)
        
if __name__=="__main__":
	#cmd_loop(cmds)
    foo=ThreadedCmdLoop(cmds)
    def k():
        foo.start()
        while foo.gather_live():
            foo.run_commands(10)
            time.sleep(0.01)
