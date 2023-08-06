# -*- coding: utf-8 -*-
import os
import os.path
import matplotlib.pyplot as plt

cnames = ('aliceblue','antiquewhite','aqua','aquamarine','azure','beige','bisque','black','blanchedalmond','blue',
          'blueviolet','brown','burlywood','cadetblue','chartreuse','chocolate','coral','cornflowerblue','cornsilk',
          'crimson','cyan','darkblue','darkcyan','darkgoldenrod','darkgray','darkgreen','darkkhaki','darkmagenta',
          'darkolivegreen','darkorange','darkorchid','darkred','darkseagreen','darkslateblue','darkslategray',
          'darkturquoise','darkviolet','deeppink','deepskyblue','dimgray','firebrick','floralwhite','forestgreen',
          'fuchsia','gainsboro','ghostwhite','gold','goldenrod','gray','green','honeydew','hotpink','indianred',
          'indigo','ivory','khaki','lavender','lavenderblush','lawngreen','lemonchiffon','lime','limegreen','linen',
          'magenta','maroon','mintcream','mistyrose','moccasin','navajowhite','navy','oldlace','olive','olivedrab',
          'orange','orchid','palegoldenrod','paleturquoise','palevioletred','papayawhip','peachpuff','peru','pink',
          'plum','purple','red','sienna','silver','skyblue','slateblue','slategray','snow','springgreen','steelblue',
          'tan','teal','thistle','turquoise','violet','wheat','yellow')

def conRoc(pre_file='file',image='image',titlestr='roc'):
    
    data=[]
    ab=[]
    aa=[]
    files1 =os.listdir(pre_file)
    for File in files1:#每个txt文件
        aa.append(File)
        tt=File[-4:]
        if tt!='.txt':
            break
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
        plt.title(titlestr)
        plt.plot(x, y,color=cnames[i%100],label=aa[i][:-4])
        plt.plot(x, z,color=cnames[i%100])
    image+='.jpg'
    plt.legend(loc=0)
    plt.savefig(image)
    plt.show() 
    print "yes"
        


if __name__ == '__main__':
    conRoc()
