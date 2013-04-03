#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
class Logger:
    @staticmethod
    def log(stringtolog):
        spr_dir=os.path.join(os.getcwd(),'Spr')
        spr_dir=os.path.join(spr_dir,'log.txt')
        output = open(spr_dir, 'a')
        now = datetime.datetime.now()
        outstr=now.strftime("%d.%m.%Y %H:%M:%S")+u': '+stringtolog
        output.write(outstr.encode('cp1251')+'\r\n')
        output.close()
