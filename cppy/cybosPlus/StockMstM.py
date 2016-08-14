# coding=utf-8
'''
Created on 2016. 8. 14.

@author: Jay
'''
from cppy.adaptor import CpRqRpClass


@CpRqRpClass('dscbo1.StockMstM')
class StockMstM(object):
    '''
    주식 복수 종목에 대해 간단한 내용을 일괄 조회 요청하고 수신한다
    '''
    class InputType(enumerate):
        StockCodes = 0  #다수의 종목코드
    
    class OutputType(enumerate):        
        StockCode = 0   #종목코드
        StockName = 1   #종목명        
        NetChange = 2   #대비        
        NetChangeGubunCode = 3  #대비구분코드        
        CurrentPrice = 4    #현재가
        AskPrice = 5    #매도호가        
        BidPrice = 6    #매수호가        
        Volume = 7  #거래량
    
    def setInputValue(self, inputTypes, inputValues):
        self.inputTypes = inputTypes
        self.inputValues = inputValues
        
    def setOutputValue(self, outputTypes):
        self.outputTypes = outputTypes        
        
    def request(self, com_obj):        
        for i in range(len(self.inputTypes)) :
            com_obj.SetInputValue(self.inputTypes[i], self.inputValues[i])
        com_obj.Request()

    def response(self, com_obj):
        num = com_obj.GetHeaderValue(0)
        for i in range(0, num) :
            result = ""
            for j in range(0, len(self.outputTypes)) :
                value = com_obj.GetDataValue(self.outputTypes[j], i)
                result += str(value) + "; "
            print (result)
            
            
    