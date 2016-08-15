# coding=utf-8
'''
Created on 2016. 8. 14.

@author: Jay
'''
from cppy.adaptor import CpRqRpClass


@CpRqRpClass('CpSysDib.StockChart')
class StockChart(object):
    '''
    주식, 업종, ELW의 차트데이터를 수신합니다
    '''
    class InputType(enumerate):
        StockCode = 0   #종목코드
        Gubun = 1   #요청구분(1:기간으로 요청, 2:개수로 요청)
        EndDate = 2   #요청종료일
        StartDate = 3   #요청시작일
        Number = 4  #요청개수
        Field = 5
        Unit = 6    #데이터 단위('D':일, 'W':주, 'M':월, 'm':분, 'T':틱)
            
    class OutputType(enumerate):   
        Date = 0    #날짜
        Time = 1    #시간(hhmm)
        OpenPrice = 2  #시가
        HighestPrice = 3   #고가
        LowestPrice = 4    #저가
        ClosePrice = 5  #종가
        NetChange = 6  #전일대비 (대비부호(37)과 반드시 같이 요청)
        Volume = 8 #거래량
        Amount = 9 #거래대금
        CumulativeSellVolume = 10   #누적체결매도수량(분/틱 요청일때만 제공)
        CumulativeBuyVolume = 11    #누적체결매수수량(분/틱 요청일때만 제공)
        ListedAmount = 12   #상장주식수
        MarketCaptalization = 13    #시가총액
        ForeignLimitVolume = 14    #외국인 주문 한도 수량
        ForeignOrderableVolume = 15 #외국인 주문 가능 수량
        ForeignHoldVolume = 16  #외국인 현 보유 수량
        ForeignHoldPercent = 17 #외국인 현 보유 비율
        AdjustedStockPriceDate = 18 #수정주가일자
        AdjustedPriceRatio = 19 #수정주가비율
        NetBuyingAgency = 20    #기관 순매수
        CumulativeNetBuyingAgency = 21    #기관 누적 순매수
        TurnoverRatio = 25  #주식 회전율
        RatioOfDeals = 26   #거래성립률
        GubunNetChange = 37 #대비부호(1:상한, 2:상승, 3:보합, 4:하한, 5:하락, 6:기세상한, 7:기세상승, 8:기세하한, 9:기세하락)
            
    def setInputValue(self, inputTypes, inputValues):
        self.inputTypes = inputTypes
        self.inputValues = inputValues
        
    def setOutputValue(self, outputTypes):
        self.outputTypes = outputTypes        
        
    def request(self, com_obj):        
        for i in range(len(self.inputTypes)) :
            com_obj.SetInputValue(self.inputTypes[i], self.inputValues[i])
        
        com_obj.SetInputValue(StockChart.InputType.Field, self.outputTypes)
        
        com_obj.Request()

    def response(self, com_obj):      
        stockCode = com_obj.GetHeaderValue(0) # 종목코드
        cnt = com_obj.GetHeaderValue(3) #  수신개수
        fieldNum = com_obj.GetHeaderValue(1)    #필드겟수
        fieldNames = com_obj.GetHeaderValue(2)  #필드명 배열
        lastUpdatedTime = com_obj.GetHeaderValue(21) #최근갱신 시간
        
        fieldNameStr = "종목코드; "
        for j in range(0, fieldNum) :
            fieldNameStr += fieldNames[j] + "; "
        print (fieldNameStr)
        
        for i in range(cnt):            
            result = stockCode + "; "
            for j in range(0, fieldNum) :                
                value = com_obj.GetDataValue(j, i)
                result += str(value) + "; "            
            print (result)
            
            
    