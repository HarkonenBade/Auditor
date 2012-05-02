#from auditor.perceptron import Perceptron
#from auditor.string_enc import enc_string_unit,enc_string_single
#import random

#def test_accuracy_numerical():
#    print(">Accuracy Testing V0.01")
#    p = Perceptron()
#    p.init_weights(1)
#    
#    print(">Creating training set.")
#    tr_set = [0]*100
#    tr_set = [[random.random()*100] for i in tr_set]
#    tr_cls = [1 if i[0]<50 else -1 for i in tr_set]
#    
#    print(">Creating classification set.")
#    chk_set = [random.random()*100 for i in tr_set]
#    chk_cls = [1 if i<50 else -1 for i in chk_set]
#    
#    for k in range(10):
#        print(">Pass " + str(k))
#        p.train(zip(tr_set,tr_cls))
#        
#        correct = 0
#        for i,j in zip(chk_set,chk_cls):
#            if(p.classify([i])==j):
#                correct = correct+1
#        print(">Accuracy = " + str(correct) + "%")
    
#test_accuracy_numerical()
