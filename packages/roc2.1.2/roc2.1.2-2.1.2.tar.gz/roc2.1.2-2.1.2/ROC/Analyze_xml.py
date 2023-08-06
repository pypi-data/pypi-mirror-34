# -*- coding: utf-8 -*-
import xml.dom.minidom 
import os.path
from read import read
from IOU import IOU
import os


def Analyze_xml(standard_path,test_path):

    wrong,creat,pos=0,0,0
    ratio=0.
    list1=[]
    Reframe=GTframe=[]
    path1=standard_path
    path2=test_path
    files1 = os.listdir(path2)
    
    for xmlFile in files1:
        
        testpath_xml=os.path.join(path2,xmlFile)
        standpath_xml=testpath_xml.replace(path2,path1)
        
        if os.path.isfile(standpath_xml):
            dom_test=xml.dom.minidom.parse(testpath_xml)
            dom_stand=xml.dom.minidom.parse(standpath_xml)
            root1=dom_test.documentElement
            root2=dom_stand.documentElement
            Reframe=read(root1)
            GTframe=read(root2)
            pos+=len(GTframe)
            
            if len(GTframe)>len(Reframe):
                for i in range(len(GTframe)-len(Reframe)):
                    list1.append([0,1,0])
                    
            for i in range(len(Reframe)):
                wrong=creat=0
                for j in range(len(GTframe)):
                    ratio=IOU(Reframe[i],GTframe[j])
                    if ratio>=0.5:
                        creat=1
                        list1.append([creat,wrong,0])
                        break
                if creat==0:
                    wrong=1
                    list1.append([creat,wrong,0])
                
        else:
            creat=wrong=0
            dom_test=xml.dom.minidom.parse(testpath_xml)
            root1=dom_test.documentElement
            Reframe=read(root1)
            for i in range(len(Reframe)):
                ratio=0
                wrong=1
                list1.append([creat,wrong,0])
    return list1,pos
            
        