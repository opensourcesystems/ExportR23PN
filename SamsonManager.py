#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SamsonDBManager import SamsonDBManager
import datetime
from Logger import Logger
from PyQt4 import QtGui
from Utils import *
import os
from DbfManager import DbfManager
class SamsonManager:
   def ExportPN(self,progressBar,path):
    dbfmgr=DbfManager()


    mgr = SamsonDBManager()
    data=mgr.getdata()
    pathh=os.path.join(path,u'PRIK'+str(data[0]['CODE_MO']))
    dbfmgr.CreateToDbf(pathh)
    progressBar.setMaximum(len(data)-1)
    cnt=0
    for row in data:
        QtGui.qApp.processEvents()
        row['IDSTR']=cnt
        row['DATR']=datetime.datetime.strptime(row['DATR'], '%d.%m.%Y')
        row['ID']=int(row['ID'])
        row['Q_UL']=int(row['Q_UL'])
        row['Q_NP']=int(row['Q_NP'])
        if row['freeInput']!='':
            splt=row['freeInput'].split(u'.')
            if len(splt)>0: row['NP_NAME']=splt[0].rstrip()
            if len(splt)>1: row['UL_NAME']=splt[1].rstrip()
            if len(splt)>2: row['DOM']=splt[2].rstrip()
            if len(splt)>=3: row['KV']=splt[3].rstrip()
        dbfmgr.createRecord(row)
        progressBar.setValue(cnt)
        cnt+=1
    dbfmgr.closedbf()
    dbfmgr.CreateZip(pathh)
    #
    #
    #
    #     map(lambda x:,)






    def definePolicyKind(self,kmivcid):
       res= {1:  2,2: 1,3:3,4:  3,5: 3,None:'null'}[kmivcid]
       return res
   def getSMO(self):
       mgr = SamsonDBManager()
       return mgr.getSMO()
   def splitbySMO(self,path):
       sdbf=DbfManager()
       sdbf.LoadDbf(path)




