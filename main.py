#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
from PyQt4 import QtCore,QtGui
from UI_ExportR23PN import  Ui_Dialog
from ExportConfig import ImportConfig,ExportConfig
from SamsonManager import SamsonManager
from ConnectionsManager import ConnectionsManager
from Logger import Logger
class CImportPN(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.progressBar.setFormat('%p%')
        self.progressBar.setValue(0)
        # ic=()
        #datafromsamson={'FAM': u'surname', 'IM': u'firstname', 'OT': u'parentname'}
        #todbf={}



        ImportConfig.parse()
        # samsmgr=SamsonManager()
        # samsmgr.ManageRawKmivcData(KmivcManager.Getrawkmivcdata())
        #for n in range(0,50,1):
        #    itme=QtGui.QListWidgetItem('test'+str(n))
         #   self.listWidget.addItem(itme)
        self.samsonadr.setText(ConnectionsManager.samsonconn['ip'])
        self.samsonbd.setText(ConnectionsManager.samsonconn['db'])
        self.samsonlogin.setText(ConnectionsManager.samsonconn['login'])
        self.samsonpassword.setText(ConnectionsManager.samsonconn['password'])

        #connect(lineEdit,SIGNAL(textChanged(QString)),this,SLOT(textChangedSlot(QString)));
        QtCore.QObject.connect(self.samsonadr, QtCore.SIGNAL("textChanged(QString)"), self.on_samsonadr_changed)
        QtCore.QObject.connect(self.samsonbd, QtCore.SIGNAL("textChanged(QString)"), self.on_samsonbd_changed)
        QtCore.QObject.connect(self.samsonlogin, QtCore.SIGNAL("textChanged(QString)"), self.on_samsonlogin_changed)
        QtCore.QObject.connect(self.samsonpassword, QtCore.SIGNAL("textChanged(QString)"), self.on_samsonpassword_changed)
        Logger.log(u'Программа запущена')
        #smanager=SamsonManager()
        #res=smanager.createClient({'fam':u'Кулябко3','im':u'Николай3','ot':u'Федорович3','dr':u'1927-12-13','ss':u'09983168236'})
        #v="sdfs"
        #res+=v



    def on_radioButton_2_released(self):
        self.miacreturned=None
        self.miacreturned = QtGui.QFileDialog.getOpenFileName(self, u'Укажите файл с данными', self.lineEdit.text(), u'Файлы DBF (*.dbf)')
        if self.miacreturned == '' or self.miacreturned is None:
            QtGui.QMessageBox.information(None,'Warning',u'Выберите dbf файл',QtGui.QMessageBox.Ok)
        smgr=SamsonManager()
        smgr.splitbySMO(self.miacreturned)

    def on_samsonadr_changed(self,txt):
        ConnectionsManager.samsonconn['ip']=str(txt)
    def on_samsonbd_changed(self,txt):
        ConnectionsManager.samsonconn['db']=str(txt)
    def on_samsonlogin_changed(self,txt):
        ConnectionsManager.samsonconn['login']=str(txt)
    def on_samsonpassword_changed(self,txt):
        ConnectionsManager.samsonconn['password']=str(txt)

    @QtCore.pyqtSignature('')
    def on_pushButton_clicked(self):
        #self.mssqqlTest()

        fileName = QtGui.QFileDialog.getExistingDirectory(self, u'Укажите папку для экспорта с данными')
        if fileName != '':
            self.lineEdit.setText(str(fileName.replace("/", os.path.sep)))

    @QtCore.pyqtSignature('')
    def reject(self):
        ExportConfig.export()
        sys.exit(self)

    @QtCore.pyqtSignature('')
    def on_pushButton_2_clicked(self):
        path=str(self.lineEdit.text())
        if len(path)==0:

            QtGui.QMessageBox.information(None,'Warning',u'Выберите dbf файл',QtGui.QMessageBox.Ok)
            return
        samsmgr=SamsonManager()
        #dirname, filename = os.path.split(os.path.abspath(path))
        item = QtGui.QListWidgetItem(u'Работаю ждите............')
        self.listWidget.addItem(item)
        QtGui.qApp.processEvents()
        samsmgr.updatekladr()



        samsmgr.ExportPN(self.progressBar,path)
        item = QtGui.QListWidgetItem(u'Готово!!')
        self.listWidget.addItem(item)
        QtGui.qApp.processEvents()
        #samsmgr.ManageRawKmivcData(KmivcManager.Getrawkmivcdata(),self.tableWidget,self.progressBar)
        # for i in range(5):
        #     self.tableWidget.setItem(1, i, QtGui.QTableWidgetItem('G'))
        #self.tableWidget.setRowCount(5)
        # for m in range(5):
        #
        #     for n in range(5):
        #         newitem = QtGui.QTableWidgetItem('G')
        #         self.tableWidget.setItem(m, n, newitem)
        # ExportConfig.export()
        # if self.lineEdit.text() == '':
        #     QtGui.QMessageBox.information(None,'Warning',u'Выберите dbf файл',QtGui.QMessageBox.Ok)
        #     return
        # self.startImport()

def main():
    app = QtGui.QApplication(sys.argv)
    dlg = CImportPN()
    #.exec_()
    sys.exit(dlg.exec_())

if __name__ == "__main__":
    main()