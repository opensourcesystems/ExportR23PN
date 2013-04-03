#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ConnectionsManager:
    samsonconn={}
    @staticmethod
    def samsonconstr():
        return """mysql://{0}:{1}@{2}/{3}?charset=utf8""".format(ConnectionsManager.samsonconn['login'],ConnectionsManager.samsonconn['password'],ConnectionsManager.samsonconn['ip'],ConnectionsManager.samsonconn['db'])
