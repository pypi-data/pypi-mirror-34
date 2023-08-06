# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from Analyze_xml import Analyze_xml
import os.path
import random


def roc(standard_path="truth",test_path="test",result_roc='result_roc',image='image'):
    db=[]
    db,pos=Analyze_xml(standard_path,test_path)
    #print db
    for i in range(len(db)):
        a=random.random()
        db[i][2]=round(a, 5)
    db = sorted(db, key=lambda x:x[2], reverse=True)#sorted() 
    
  
    xy_arr = []
    score =[]
    tp,fp = 0., 0.		
    for i in range(len(db)):
        tp += db[i][1]#wrong
        fp += db[i][0]#creat
        xy_arr.append([tp,fp/pos])
        score.append(db[i][2])
   
    #print score
    auc = 0.			
    prev_x = 0
    for x,y in xy_arr:
	    if x != prev_x:
		    auc += (x - prev_x) * y
		    prev_x = x     
    
    print db      
    x = [_a[0] for _a in xy_arr]
    y = [_a[1] for _a in xy_arr]
    z = [_a for _a in score]
    #print z
    result_roc+='.txt'
    image+='.png'
    plt.title("ROC (AUC = %.4f)" % (auc))
    plt.xlabel("False Count")
    plt.ylabel("True Positive Rate")
    plt.plot(x, y)
    plt.plot(x, z)
    plt.savefig(image)
    plt.show()
    
    with open(result_roc, 'w') as fp:
        for i in range(len(db)):
            fp.write("%d %f %f \n" % (x[i], y[i],z[i]))
    
if __name__ == '__main__':
    roc()