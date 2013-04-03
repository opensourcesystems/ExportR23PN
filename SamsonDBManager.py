#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sqlalchemy import create_engine
from TextFileLoader import TextFileLoader
from DBManager import DBManager
#from ConnectionsManager import ConnectionsManager

def recursion_cnt(fn):
    def func(self,arg2,arg3):
        if arg3>2:
            raise Exception('n>2')
        return fn(self,arg2,arg3)
    return func



class SamsonDBManager:

    def getdata(self):
        stmt=TextFileLoader.load()
        ert=u"""
                        SELECT
                  client.id as ID ,
                  if (Organisation.infisCode is null,'',Organisation.infisCode) as SMO,
                  case Clientpolicy.policyKind_id
                    when '3' then 'П'
                    when '2' then 'С'
                    when '1' then 'В'
                    else ''
                  end as DPFS,
                   if (Clientpolicy.`serial` is null,'',Clientpolicy.`serial`) as DPFS_S,
                   if (Clientpolicy.number is null,'',Clientpolicy.number) as DPFS_N,
                   if (Client.lastName is null,'',Client.lastName) as FAM,
                   if (Client.firstName is null,'',Client.firstName) as IM,
                   if (Client.patrName is null,'',Client.patrName) as OT,
                   if (Client.birthDate is null,'',DATE_FORMAT(Client.birthDate, '%d.%m.%Y')) as DATR,
                   if (rbDocumentType.regionalCode is null,'',rbDocumentType.regionalCode) as DOC,
                   if (ClientDocument.`serial` is null,'',ClientDocument.`serial`) as DOC_S,
                   if (ClientDocument.number is null,'',ClientDocument.number) as DOC_N,
                   if (curorg.infisCode is null,'',curorg.infisCode) as CODE_MO,
                   '1' as PRIK,
                   if (clientattach.begDate is null,'',DATE_FORMAT(clientattach.begDate, '%d.%m.%Y')) as PRIK_D,
                   if (clientattach.endDate is null,'',DATE_FORMAT(clientattach.endDate, '%d.%m.%Y')) as OTKR_D,
                   if (orgstructure.name is null,'',orgstructure.name) as UCH,
                   '' as R_NAME,
                   'Город где ЛПУ' as C_NAME,
                   if (socrrkld.infisCODE is null,'0',socrrkld.infisCODE ) as Q_NP,
                   if (kld.NAME is null,'',kld.NAME) as NP_NAME,
                   if (socrrkldstr.infisCODE is null,'0',socrrkldstr.infisCODE) as Q_UL,
                   if (kldstr.NAME is null,'',kldstr.NAME) as UL_NAME,
                   if (addresshouse.number is null,'',addresshouse.number) as DOM,
                   if (addresshouse.corpus is null,'',addresshouse.corpus) as KOR,
                   if (address.flat is null,'',address.flat) as KV,
                   '' as SMORES,
                   '' as MIACRES,
                   if (clientaddress.freeInput is null,'',clientaddress.freeInput) as freeInput
                  from Client
                  left join Clientpolicy on client.id=Clientpolicy.client_id
                  left join Organisation on Clientpolicy.insurer_id = Organisation.id
                  left join ClientDocument on client.id=ClientDocument.client_id
                  left join rbDocumentType on ClientDocument.documentType_id=rbDocumentType.id
                  left join Organisation as curorg on ( SELECT organisation_id FROM orgstructure WHERE parent_id IS NULL LIMIT 1 )=curorg.id
                  left join clientattach on client.id=clientattach.client_id
                  left join clientaddress on client.id=clientaddress.client_id
                  left join address on clientaddress.address_id=Address.id
                  left join addresshouse on Address.house_id=addresshouse.id
                  left join orgstructure_address on addresshouse.id=orgstructure_address.house_id
                  left join orgstructure on orgstructure_address.master_id=orgstructure.id
                  left join kladr.kladr as kld on addresshouse.KLADRCode=kld.CODE
                  left join kladr.street as kldstr on addresshouse.KLADRStreetCode=kldstr.CODE
                  left join kladr.socrbase as socrrkld on kld.SOCR=socrrkld.SCNAME
                  left join kladr.socrbase as socrrkldstr on kldstr.SOCR=socrrkldstr.SCNAME
                  group by ID

                  limit 10
                 """
        query = DBManager.executeSql(unicode(stmt,'cp1251'))

        return query
    def getSMO(self):
        stmt=u"""select infisCode,shortName from Organisation where id in (select insurer_id from clientpolicy
                      where insurer_id is not null
                      group by insurer_id)"""
        query = DBManager.executeSql(stmt)

        return query