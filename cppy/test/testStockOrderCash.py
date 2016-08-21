# coding: utf-8
import win32com.client

instCpTdUtil = win32com.client.Dispatch("CpTrade.CpTdUtil")

instCpTdUtil.TradeInit()

print (instCpTdUtil.TradeInit(0))
accountNumber = instCpTdUtil.AccountNumber[0]

#     instanceCpTradeUtil = CpTradeUtil()
#     accountNumber = instanceCpTradeUtil.getAccountNumber()
print (accountNumber)


# __author__ = 'lhw'
# 
# if __name__ == '__main__':

    


#     instance1 = StockOrderCash()
#     
#     inputTypes = [
#                   StockOrderCash.InputType.SellOrBuy,                  
#                   StockOrderCash.InputType.StockCode,
#                   StockOrderCash.InputType.OrderNumber,
#                   StockOrderCash.InputType.OrderPrice
#                   ]
#     inputValues = [
#                    1, 
#                    "A005930",
#                    10,
#                    10000000
#                    ]    
#     instance1.setInputValue(inputTypes, inputValues)    
#     
#     outputTypes = [
#                    StockOrderCash.OutputType.StockCode,                   
#                    ]
#     
#     instance1.setOutputValue(outputTypes)
#     
#     instance1.request()
# 
#     import pythoncom, time
#     while True:
#         pythoncom.PumpWaitingMessages()
#         time.sleep(0.01)