# coding: utf-8
from cybosPlus.StockMst import StockMst

__author__ = 'lhw'

if __name__ == '__main__':

    instance1 = StockMst()
    
    inputTypes = [StockMst.InputType.StockCode]
    inputValues = ["A005930"]    
    instance1.setInputValue(inputTypes, inputValues)    
    
    outputTypes = [
                   StockMst.OutputType.StockCode, 
                   StockMst.OutputType.StockName,
                   StockMst.OutputType.NetChange,
                   StockMst.OutputType.CurrentPrice,
                   StockMst.OutputType.EPS,
                   StockMst.OutputType.Suspended,
                   StockMst.OutputType.DayOfRecordHighPrice                   
                   ]
    
    instance1.setOutputValue(outputTypes)
    
    instance1.request()

    import pythoncom, time
    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.01)