#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from sqlalchemy import create_engine
import MySQLdb
import MySQLdb.cursors
from ConnectionsManager import ConnectionsManager
class DBManager:
    @staticmethod
    def executeSqlNonQuery(command):
        db = MySQLdb.connect(host=ConnectionsManager.samsonconn['ip'], user=ConnectionsManager.samsonconn['login'],
                             passwd=ConnectionsManager.samsonconn['password'], db=ConnectionsManager.samsonconn['db'], charset='utf8')
        # формируем курсор, с помощью которого можно исполнять SQL-запросы


        cursor = db.cursor()

        cursor.execute(command)
        while cursor.nextset() is not None: pass
        db.commit()

        # исполняем SQL-запрос

        #cursor.connection.commit()
        # применяем изменения к базе данных
        #db.commit()
        id=cursor.lastrowid
        # закрываем соединение с базой данных
        db.close()
        return id
       # engine = create_engine(constr)
       #result=engine.execute(command)
    @staticmethod
    def executeproc():
        db = MySQLdb.connect(host=ConnectionsManager.samsonconn['ip'], user=ConnectionsManager.samsonconn['login'],
                             passwd=ConnectionsManager.samsonconn['password'], db=ConnectionsManager.samsonconn['db'], charset='utf8',
                             cursorclass=MySQLdb.cursors.DictCursor)
        cursor = db.cursor()
        proc=cursor.callproc( "ImportR23PN_proc", () )
        result=cursor.fetchall()

        cursor.close()
        db.close()
        return result



    @staticmethod
    def executeSql(command):
        db = MySQLdb.connect(host=ConnectionsManager.samsonconn['ip'], user=ConnectionsManager.samsonconn['login'],
                             passwd=ConnectionsManager.samsonconn['password'], db=ConnectionsManager.samsonconn['db'], charset='utf8',
                             cursorclass=MySQLdb.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute(command)
        return  cursor.fetchall()
        # engine = create_engine(constr)
        # result=engine.execute(command)
        # return  result.fetchall()