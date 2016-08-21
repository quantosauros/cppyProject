# coding=utf-8
'''
Created on 2016. 8. 14.

@author: Jay
'''
from cppy.adaptor import CpSubPubClass


@CpSubPubClass('dscbo1.StockJpBid')
class StockCur(object):
    '''
    주식/ETF/ELW 종목 매도, 매수에 관한 1차~10차 호가/LP호가 및 호가잔량 수신
    '''
    class InputType(enumerate):
        StockCode = 0
    
    class OutputType(enumerate):        
        StockCode = 0   #종목코드
        Time = 1    #시간
        Volume = 2  #거래량
        SellPrice1 = 3   #1차 매도호가
        BuyPrice1 = 4   #1차 매수호가
        SellRemain1 = 5  #1차 매도잔량
        BuyRemain1 = 6  #1차 매수잔량
        SellPrice2 = 7   #2차 매도호가
        BuyPrice2 = 8   #2차 매수호가
        SellRemain2 = 9  #2차 매도잔량
        BuyRemain2 = 10  #2차 매수잔량
        SellPrice3 = 11   #3차 매도호가
        BuyPrice3 = 12   #3차 매수호가
        SellRemain3 = 13  #3차 매도잔량
        BuyRemain3 = 14  #3차 매수잔량
        SellPrice4 = 15   #4차 매도호가
        BuyPrice4 = 16   #4차 매수호가
        SellRemain4 = 17  #4차 매도잔량
        BuyRemain4 = 18  #4차 매수잔량
        SellPrice5 = 19   #5차 매도호가
        BuyPrice5 = 20   #5차 매수호가
        SellRemain5 = 21  #5차 매도잔량
        BuyRemain5 = 22  #5차 매수잔량
        TotalSellRemain = 23 #총 매도잔량
        TotalBuyRemain = 24 #총 매수잔량
        TotalSellRemainOut = 25 #시간외 총 매도잔량
        TotalBuyRemainOut = 26 #시간외 총 매수잔량
        SellPrice6 = 27   #6차 매도호가
        BuyPrice6 = 28    #6차 매수호가
        SellRemain6 = 29  #6차 매도잔량
        BuyRemain6 = 30   #6차 매수잔량
        SellPrice7 = 31   #7차 매도호가
        BuyPrice7 = 32    #7차 매수호가
        SellRemain7 = 33  #7차 매도잔량
        BuyRemain7 = 34   #7차 매수잔량
        SellPrice8 = 35   #8차 매도호가
        BuyPrice8 = 36    #8차 매수호가
        SellRemain8 = 37  #8차 매도잔량
        BuyRemain8 = 38   #8차 매수잔량
        SellPrice9 = 39   #9차 매도호가
        BuyPrice9 = 40    #9차 매수호가
        SellRemain9 = 41  #9차 매도잔량
        BuyRemain9 = 42   #9차 매수잔량
        SellPrice10 = 43   #10차 매도호가
        BuyPrice10 = 44    #10차 매수호가
        SellRemain10 = 45  #10차 매도잔량
        BuyRemain10 = 46   #10차 매수잔량
        
    def setInputValue(self, inputTypes, inputValues):
        self.inputTypes = inputTypes
        self.inputValues = inputValues
        
    def setOutputValue(self, outputTypes):
        self.outputTypes = outputTypes        
    
    def setEventProc(self, eventProc):
        self.eventProc = eventProc
        #self.eventProc.add_observer(['cls_*'], self.echo)
        
    def setEcho(self, keyPattern, callableFunction):
        self.eventProc.add_observer(keyPattern, callableFunction)

    def subscribe(self, com_obj):
        com_obj.Unsubscribe()
        for i in range(len(self.inputTypes)) :
            com_obj.SetInputValue(self.inputTypes[i], self.inputValues[i])
        com_obj.Subscribe()
    
    def publish(self, com_obj):
        result = []
        resultStr = ""
        for i in range(len(self.outputTypes)):
            result[i] = com_obj.GetHeaderValue(self.outputTypes[i])
            resultStr += str(result[i]) + "; "
        
        self.eventProc.push('cls_%s'%(self.inputValues[0]), resultStr);
            
    