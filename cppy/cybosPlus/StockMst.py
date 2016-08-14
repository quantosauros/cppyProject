# coding=utf-8
'''
Created on 2016. 8. 14.

@author: Jay
'''
from cppy.adaptor import CpRqRpClass


@CpRqRpClass('dscbo1.StockMst')
class StockMst(object):
    '''
    주식 종목의 현재가에 관련된 데이터
    '''
    class InputType(enumerate):
        StockCode = 0   #종목코드
    
    class OutputType(enumerate):        
        StockCode = 0   #종목코드
        StockName = 1   #종목명
        DaiShinCode = 2 #대신업종코드
        GroupCode = 3   #그룹코드
        Time = 4        #시간
        Gubun = 5       #소속구분(문자열)
        Size = 6        #대형,중형,소형
        UpperPrice = 8  #상한가
        LowerPrice = 9  #하한가
        PrevClosePrice = 10 #전일종가
        CurrentPrice = 11   #현재가
        NetChange = 12  #전일대비
        OpenPrice = 13  #시가
        HighestPrice = 14   #고가
        LowestPrice = 15    #저가
        AskPrice = 16   #매도호가
        BidPrice = 17   #매수호가
        CumulativeVolume = 18   #누적거래량
        CumulativeAmount = 19   #누적거래대금
        EPS = 20    #EPS
        RecordHighPrice = 21    #신고가
        DayOfRecordHighPrice = 22   #신고가일
        RecordLowPrice = 23 #신저가
        DayOfRecordLowPrice = 24    #신저가일
        PER = 28    #PER
        ListedAmount = 31   #상장주식수
        ForeignLimitVolume = 37 #외국인 한도수량
        ForeignLimitPercent = 38    #외국인 한도비율        
        PreviousDayVolume = 46  #전일거래량
        HighestPrice52wk = 47   #52주 최고가
        DayOfHighestPrice52wk = 48  #52주 최고일
        LowestPrice52wk = 49    #52주 최저가
        DayOfLowestPrice52wk = 50   #52주 최저일
        CreditBalancePercent = 64   #신용잔고비율
        Disignated = 66 #관리종목 코드(Y:관리종목, N:정상종목)
        Warned = 67  #투자경고구분(1:정상, 2:주의, 3:경고, 4:위험예고, 5:위험)
        Suspended = 68  #거래정지구분(Y:거래정지종목, N:정상종목)
    
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
        result = ""
        for j in range(0, len(self.outputTypes)) :
            value = com_obj.GetHeaderValue(self.outputTypes[j])
            result += str(value) + "; "
        print (result)
            
            
    