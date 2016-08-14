# coding: utf-8
from cybosPlus.StockChart import StockChart
__author__ = 'lhw'

if __name__ == '__main__':

    instance = StockChart()
    
    inputTypes = [StockChart.InputType.StockCode,
                  StockChart.InputType.Gubun,
                  StockChart.InputType.Number,
                  StockChart.InputType.Unit];                  
    inputValues = ['A005930', ord('2'), 100, ord('D')]    
    instance.setInputValue(inputTypes, inputValues)
    
    outputTypes = [StockChart.OutputType.Date,
                   StockChart.OutputType.Time,
                   StockChart.OutputType.ClosePrice,
                   StockChart.OutputType.Volume,
                   StockChart.OutputType.Amount,
                   StockChart.OutputType.ForeignHoldPercent,
                   StockChart.OutputType.NetBuyingAgency,
                   ]
    
    instance.setOutputValue(outputTypes)
    instance.request()

    import pythoncom, time
    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.01)