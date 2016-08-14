# coding: utf-8
from cybosPlus.StockMstM import StockMstM
__author__ = 'lhw'

if __name__ == '__main__':

    instance1 = StockMstM()
    
    inputTypes = [StockMstM.InputType.StockCodes]
    inputValues = ["A005930A008770"]    
    instance1.setInputValue(inputTypes, inputValues)    
    
    outputTypes = [
                   StockMstM.OutputType.StockCode, 
                   StockMstM.OutputType.StockName,
                   StockMstM.OutputType.NetChange,
                   StockMstM.OutputType.CurrentPrice,
                   StockMstM.OutputType.Volume
                   ]
    
    instance1.setOutputValue(outputTypes)
    
    instance1.request()

    import pythoncom, time
    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.01)