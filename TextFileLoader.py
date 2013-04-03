#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime
class TextFileLoader:
    @staticmethod
    def load():
        spr_dir=os.path.join(os.getcwd(),'Spr')
        spr_dir=os.path.join(spr_dir,'samsonquery.txt')
        output = open(spr_dir, 'r')

        result=output.read()
        output.close()
        return result

