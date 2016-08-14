# coding: utf-8
__author__ = 'lhw'



from cppy.adaptor import CpRqRpClass

@CpRqRpClass('dscbo1.StockWeek')
class StkMstM(object):
    def request(self, com_obj):
        com_obj.SetInputValue(0, 'A005930')
        com_obj.Request()

    def response(self, com_obj):
        num = com_obj.GetHeaderValue(1)
        for i in range(0, num) :
            print (com_obj.GetDataValue(0, i), com_obj.GetDataValue(1, i), com_obj.GetDataValue(4, i), com_obj.GetDataValue(7, i))



if __name__ == '__main__':

    stkmst = StkMstM()
    stkmst.request()

    import pythoncom, time
    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.01)