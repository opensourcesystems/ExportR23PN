#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbfpy.dbf import *
from zipfile import *
import os
class DbfManager:
    def createRecord(self,data):
        dbfRecord = self.dbf.newRecord()
        vnt=0
        for fieldname in dbfRecord.dbf.fieldNames:
            typecod=dbfRecord.dbf.fieldDefs[vnt].typeCode
            # if typecod=='C':
            #      dbfRecord[fieldname]=data[fieldname].decode('cp1251')
            # else:
            dbfRecord[fieldname]= data[fieldname]
            vnt+=1

        dbfRecord.store()
    def closedbf(self):
        self.dbf.close()

    def CreateToDbf(self,path):
        self.dbfpath=path+u'.dbf'
        self.dbf = Dbf(self.dbfpath, new=True, encoding='cp866')

        self.dbf.addField(
        ('ID', 'N' , 7, 0),
         ('SMO'	, 'C' ,	4),
         ('DPFS', 'C' , 1),
         ('DPFS_S', 'C' , 12),
         ('DPFS_N', 'C' , 20),
         ('FAM', 'C' , 40),
         ('IM', 'C' , 40),
         ('OT', 'C' , 40),
         ('DATR', 'D'),
         ('DOC', 'C' , 2),
         ('DOC_S', 'C' , 10),
         ('DOC_N', 'C' , 15),
         ('CODE_MO', 'C' , 5),
         ('PRIK', 'C' , 1),
         ('PRIK_D', 'D'),
         ('OTKR_D', 'D'),
         ('UCH', 'C' , 5),
         ('R_NAME', 'C' , 30),
         ('C_NAME', 'C' , 30),
         ('Q_NP', 'N' , 2, 0),
         ('NP_NAME', 'C' , 40),
         ('Q_UL', 'N' , 2, 0),
         ('UL_NAME', 'C' , 40),
         ('DOM', 'C' , 7),
         ('KOR', 'C' , 5),
         ('KV', 'C' , 5),
         ('SMORES', 'C' , 40),
         ('MIACRES', 'C' , 40),
         ('IDSTR', 'N' , 10, 0))
    def CreateZip(self,path):
        dirname, filename = os.path.split(os.path.abspath(self.dbfpath))
        zippath=path+u'.zip'
        zf = ZipFile(zippath, 'w', allowZip64=True)
        zf.write(self.dbfpath,filename,compress_type=ZIP_DEFLATED)
        zf.close()
        os.remove(self.dbfpath)
    def LoadDbf(self,path):
        path=str(path).replace("/", os.path.sep)
        returned_dbf = Dbf(path, readOnly=True, encoding='cp866')
        dirname, filename = os.path.split(os.path.abspath(path))
        dbfFields = returned_dbf.fieldNames
        smos={}

        for row in returned_dbf:
            if row['SMO'] not in smos:
                smos[row['SMO']]=[dict(zip(row.dbf.fieldNames,row.fieldData))]
            else :
                smos[row['SMO']].append(dict(zip(row.dbf.fieldNames,row.fieldData)))

        for smo in smos:
            npath=os.path.join(dirname,filename.replace(u'PRIK',u'PRIK'+str(smo)+u'_'))
            self.CreateToDbf(npath)
            for row in smos[smo]:
                self.createRecord(row)
            self.closedbf()
            self.CreateZip(npath)
        a='dfdf'

