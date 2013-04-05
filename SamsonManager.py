#!/usr/bin/env python
# -*- coding: utf-8 -*-

from SamsonDBManager import SamsonDBManager
import datetime,traceback,sys
from Logger import Logger
from PyQt4 import QtGui
from Utils import *
import os
from DbfManager import DbfManager
class SamsonManager:
   def ExportPN(self,progressBar,path):
    dbfmgr=DbfManager()


    mgr = SamsonDBManager()
    try:
        data=mgr.getdata()
    except Exception as s:
        type_, value_, traceback_ = sys.exc_info()
        tb='\n'.join(traceback.format_exception(type_, value_, traceback_))
        Logger.log(str(s)+u' traceback='+tb)
        QtGui.QMessageBox.information(None,'Warning',s.message,QtGui.QMessageBox.Ok)
        return  None

    pathh=os.path.join(path,u'PRIK'+str(data[0]['CODE_MO']))
    dbfmgr.CreateToDbf(pathh)
    progressBar.setMaximum(len(data)-1)
    cnt=0
    for row in data:
        try:
            QtGui.qApp.processEvents()
            row['IDSTR']=cnt
            row['DATR']=datetime.datetime.strptime(row['DATR'], '%d.%m.%Y')
            row['ID']=int(row['ID'])
            if row['Q_UL'] ==u'' or row['Q_NP']==u'':
                QtGui.QMessageBox.information(None,'Warning',u'В кладр не заполнено поле infisCode таблицы SOCRBASE, загрузите справочники spr44, spr45',QtGui.QMessageBox.Ok)
                return None
            row['Q_UL']=int(row['Q_UL'])
            row['Q_NP']=int(row['Q_NP'])
            row['PRIK_D']='' if row['PRIK_D'] ==u'' else datetime.datetime.strptime(row['PRIK_D'], '%d.%m.%Y') #row['PRIK_D']
            row['OTKR_D']='' if row['OTKR_D']== u''  else datetime.datetime.strptime(row['OTKR_D'], '%d.%m.%Y') #row['OTKR_D']

            dbfmgr.createRecord(row)
            progressBar.setValue(cnt)
            cnt+=1
        except Exception as s:
            type_, value_, traceback_ = sys.exc_info()
            tb='\n'.join(traceback.format_exception(type_, value_, traceback_))
            Logger.log(str(s)+u' traceback='+tb)
            QtGui.QMessageBox.information(None,'Warning',s.message,QtGui.QMessageBox.Ok)
            return  None
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
   def updatekladr(self):

       mgr=SamsonDBManager()

       mgr.updatekladr(DbfManager.loadSprs())




