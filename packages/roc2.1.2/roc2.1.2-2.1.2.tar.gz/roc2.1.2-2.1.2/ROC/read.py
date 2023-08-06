# -*- coding: utf-8 -*-
#import xml.dom.minidom 

def read(root):
    """
    读取一个xml文件的所有标签
    """
    Reframe=[]
    #filename=root.getElementsByTagName('filename')
    xmin=root.getElementsByTagName('xmin')
    xmax=root.getElementsByTagName('xmax')
    ymin=root.getElementsByTagName('ymin')
    ymax=root.getElementsByTagName('ymax')
    rectnum = len(xmin)
    #n0=filename[0]
    #Name = n0.firstChild.data
    #Reframe.append(Name)
    for i in range(0,rectnum):#一个文件的多个框
        n1=xmin[i]
        n2=xmax[i]
        n3=ymin[i]
        n4=ymax[i]
        Xmin=Ymin=Xmax=Ymax=0
        Xmin = int(n1.firstChild.data)
        Xmax = int(n2.firstChild.data)
        Ymin = int(n3.firstChild.data)
        Ymax = int(n4.firstChild.data)
        Reframe.append([Xmin,Ymin,Xmax,Ymax])
    return Reframe
               