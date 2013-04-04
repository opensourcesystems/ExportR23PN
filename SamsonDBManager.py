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

    def getdata(self):
        #stmt=TextFileLoader.load()

        DBManager.executeSqlNonQuery(ConnectionsManager.samsonconn['export_proc'])
        query =DBManager.executeproc()


        return query
    def getSMO(self):
        stmt=u"""select infisCode,shortName from Organisation where id in (select insurer_id from clientpolicy
                      where insurer_id is not null
                      group by insurer_id)"""
        query = DBManager.executeSql(stmt)

        return query