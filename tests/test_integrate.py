import unittest
from auditor import *
from auditor.plugins import *

#class TestIntegrate(unittest.TestCase):
 #   def test_integration(self):
  #      iNote = inotify_interface.INotifyInterface(100)
   #     fData = file_data_tree.FileDataTree()
    #    fScanQ = file_scan_queue.FileScanQueue()
     #   pMan = plugin_manager.PluginManager("./test_plugins","./test_cache")
      #  evHan = event_handler.EventHandler(fScanQ,fData)
       # fScan = file_scanner.FileScanner(fScanQ,fData,pMan)
        #
#        iNote.setHandler(evHan.process)
#        iNote.startWatch("./testbed")
#        
#        pMan.loadAll()
        

if __name__=="__main__":
    unittest.main(verbosity=3)
