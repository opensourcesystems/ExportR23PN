#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
from xml.dom.minidom import parseString
from ConnectionsManager import ConnectionsManager
class ImportConfig:
    @staticmethod
    def parse():
        #spr_dir=os.getcwd()+'\\Spr\\exportconfig.xml'
        spr_dir=os.path.join(os.getcwd(), 'Spr')
        spr_dir=os.path.join(spr_dir, 'exportconfig.xml')
        file= codecs.open(spr_dir,'rb','utf-8')

        #Конвертим его в string
        data = file.read()
        #Тут понятно
        file.close()

        xml = parseString(data.encode('utf-8'))
        name = xml.getElementsByTagName('dbfschema')
        samsoncon=xml.getElementsByTagName('samson')
        query=xml.getElementsByTagName('export_proc')
        ConnectionsManager.samsonconn['export_proc']=query[0].firstChild.data

        #smo_infis=xml.getElementsByTagName('smo_infis')
        #ConnectionsManager.samsonconn['smo_infis']=smo_infis[0].nodeValue
        for node in samsoncon:
            ConnectionsManager.samsonconn['ip']=node.getAttribute('ip')
            ConnectionsManager.samsonconn['db']=node.getAttribute('db')
            ConnectionsManager.samsonconn['login']=node.getAttribute('login')
            ConnectionsManager.samsonconn['password']=node.getAttribute('password')


class ExportConfig:
    @staticmethod
    def export():
        spr_dir=os.path.join(os.getcwd(),'Spr')
        spr_dir=os.path.join(spr_dir, 'exportconfig.xml')

        file = open(spr_dir)
        #Конвертим его в string
        data = file.read()
        #Тут понятно
        file.close()

        xml = parseString(data)
        xml.toprettyxml(encoding='utf-8')
        samsoncon=xml.getElementsByTagName('samson')
        smo_infis=xml.getElementsByTagName('smo_infis')
        #smo_infis.setValue(ConnectionsManager.samsonconn['smo_infis'])
        for node in samsoncon:
            node.setAttribute('ip',ConnectionsManager.samsonconn['ip'])
            node.setAttribute('db',ConnectionsManager.samsonconn['db'])
            node.setAttribute('login',ConnectionsManager.samsonconn['login'])
            node.setAttribute('password',ConnectionsManager.samsonconn['password'])
#.encode('cp1251')
        file = open(spr_dir,'wb')

        file.writelines(xml.toxml('utf-8'))
        file.close()
