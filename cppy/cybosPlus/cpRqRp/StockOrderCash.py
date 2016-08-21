# coding=utf-8
'''
Created on 2016. 8. 14.

@author: Jay
'''
from cppy.adaptor import CpRqRpClass
import win32com.client


@CpRqRpClass('CpTrade.CpTd0311')
class StockOrderCash(object):
    '''
    장내주식/코스닥주식/ELW 주문(현금주문) 데이터를 요청하고 수신한다.
    '''
    def __init__(self):
        self.instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")
    
    class InputType(enumerate):
        SellOrBuy = 0   #주문종류코드 (1: 매도, 2:매수)
        AccountNumber = 1   #계좌번호        
        StockCode = 3   #종목코드
        OrderNumber = 4 #주문수량
        OrderPrice = 5  #주문단가
        
    
    class OutputType(enumerate):    
        AccountNumber = 1   #계좌번호
        StockCode = 3   #종목코드
        OrderNumber = 4 #주문수량
        OrderPrice = 5  #주문단가
    
    def setInputValue(self, inputTypes, inputValues):
        self.inputTypes = inputTypes
        self.inputValues = inputValues
        
    def setOutputValue(self, outputTypes):
        self.outputTypes = outputTypes        
        
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
            
            
    