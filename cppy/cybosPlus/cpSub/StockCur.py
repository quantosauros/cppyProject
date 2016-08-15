# coding=utf-8
'''
Created on 2016. 8. 14.

@author: Jay
'''
from cppy.adaptor import CpSubPubClass


@CpSubPubClass('dscbo1.StockCur')
class StockCur(object):
    '''
    주식/업종/ELW 시세 데이터를 수신합니다.
    '''
    class InputType(enumerate):
        StockCode = 0
    
    class OutputType(enumerate):        
        StockCode = 0   #종목코드
        StockName = 1   #종목명
        NetChange = 2  #전일대비
        Time = 3       #시간
        OpenPrice = 4  #시가
        HighestPrice = 5   #고가
        LowestPrice = 6   #저가
        AskPrice = 7   #매도호가
        BidPrice = 8   #매수호가
        CumulativeVolume = 9   #누적거래량
        CumulativeAmount = 10   #누적거래대금
        CurrentPrice = 13   #현가
        StateOfTrade = 14   #체결 상태(1:매수, 2:매도)
        CumulativeSellVolume = 15   #누적체결매도수량(체결가방식)
        CumulativeBuyVolume = 16    #누적체결매수수량(체결가방식)
        InstantaneousTradeVolume = 17
        MarketState = 20    #장 구분 플래그(1:장전예상체결, 2:장중, 3:장전시간외, 4:장후시간외, 5:장후 예상체결)
        GubunNetChange = 22 #대비부호(1:상한, 2:상승, 3:보합, 4:하한, 5:하락, 6:기세상한, 7:기세상승, 8:기세하한, 9:기세하락)
        
    
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
            
    