# coding: utf-8
from cybosPlus.cpSub.StockCur import StockCur
from cppy.processor import EventProcessor

__author__ = 'lhw'

def cls_echo(serieses, key, dat):
    print ('key:%s, dat:%s'%(key,dat))

if __name__ == '__main__':

    eventProc = EventProcessor()
    eventProc.start()
    
    instance = StockCur()    
    inputTypes = [StockCur.InputType.StockCode]
    inputValues = ["A005930"]    
    instance.setInputValue(inputTypes, inputValues)
    outputTypes = [
                   StockCur.OutputType.StockCode, 
                   StockCur.OutputType.StockName,
                   StockCur.OutputType.NetChange,
                   StockCur.OutputType.CurrentPrice,               
                   ]
    instance.setOutputValue(outputTypes)    
    instance.setEventProc(eventProc)    
    instance.setEcho(['cls_*'], cls_echo)
    instance.subscribe()

    import pythoncom, time
    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.01)