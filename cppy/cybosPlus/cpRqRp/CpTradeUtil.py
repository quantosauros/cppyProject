# coding=utf-8
'''
Created on 2016. 8. 14.

@author: Jay
'''
from cppy.adaptor import CpRqRpClass
import win32com.client


@CpRqRpClass('CpTrade.CpTdUtil')
class CpTradeUtil(object):
    '''    
    '''
#     def __init__(self):
#         self.com_obj.TradeInit()
    
    def getAccountNumber(self):
        self.com_obj.TradeInit()
        self.com_obj.AccountNumber()

    def request(self, com_obj):     
        self.instCpTdUtil.TradeInit()   
        for i in range(len(self.inputTypes)) :
            com_obj.SetInputValue(self.inputTypes[i], self.inputValues[i])
        
        #계좌번호
        accountNumber = self.instCpTdUtil.AccountNumber[0]
        com_obj.SetInputValue(1, accountNumber)
            
        com_obj.Request()

    def response(self, com_obj):                
        result = ""
        for j in range(0, len(self.outputTypes)) :
            value = com_obj.GetHeaderValue(self.outputTypes[j])
            result += str(value) + "; "
        print (result)
            
            
    