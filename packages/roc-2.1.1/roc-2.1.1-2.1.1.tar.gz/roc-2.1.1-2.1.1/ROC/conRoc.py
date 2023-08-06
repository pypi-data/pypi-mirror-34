# -*- coding: utf-8 -*-
import os
import os.path
import matplotlib.pyplot as plt

cnames = ('peru','dodgerblue','brown','darkslategray','lightsalmon','orange','black','springgreen',
          'fuchsia','burlywood','burlywood','cadetblue','chartreuse','chocolate','coral')

def conRoc(pre_file='file',image='image'):
    
    data=[]
    ab=[]

    files1 =os.listdir(pre_file)
    for File in files1:#每个txt文件
        path=os.path.join(pre_file,File)
        f = open(path)              
        line = f.readline()    
        db=[]        
        while line:
            data=line.split()
            if data==[]:
                break
            data[0]=float(data[0])
            data[1]=float(data[1])
            data[2]=float(data[2])
            db.append(data) 
            line = f.readline() 
        db = sorted(db, key=lambda x:x[2], reverse=True)
        ab.append(db)
        

    for i in range(len(ab)):
        x = [_a[0] for _a in ab[i]]
        y = [_a[1] for _a in ab[i]]
        z = [_a[2] for _a in ab[i]]       
        plt.xlabel("False Count")
        plt.ylabel("True Positive Rate")
        plt.plot(x, y,color=cnames[i])
        plt.plot(x, z,color=cnames[i])
    image+='.jpg'
    plt.savefig(image)
    plt.show() 
    print "yes"
        


if __name__ == '__main__':
    conRoc()