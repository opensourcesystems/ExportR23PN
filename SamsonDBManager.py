#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sqlalchemy import create_engine
from TextFileLoader import TextFileLoader
from DBManager import DBManager
from ConnectionsManager import ConnectionsManager

def recursion_cnt(fn):
    def func(self,arg2,arg3):
        if arg3>2:
            raise Exception('n>2')
        return fn(self,arg2,arg3)
    return func



class SamsonDBManager:

    def updatekladr(self,listspr):
        for spr in listspr:
            for row in spr:
                query=DBManager.executeSql(u"""select KOD_T_ST from kladr.SOCRBASE where SOCRNAME='{0}' and infisCode='{1}'""".format(spr[row],row))
                if len(query)>0:
                    continue
                else:
                    query=DBManager.executeSqlNonQuery(u"""update kladr.SOCRBASE set infisCode='{1}' where SOCRNAME='{0}'""".format(spr[row],row))





    def getdata(self):
        #stmt=TextFileLoader.load()
        DBManager.executeSqlNonQuery(u"""drop procedure if exists `ExportR23PN_proc`;""")
        DBManager.executeSqlNonQuery(ConnectionsManager.samsonconn['export_proc'])
        query =DBManager.executeproc()


        return query
    def getSMO(self):
        stmt=u"""select infisCode,shortName from Organisation where id in (select insurer_id from clientpolicy
                      where insurer_id is not null
                      group by insurer_id)"""
        query = DBManager.executeSql(stmt)

        return query