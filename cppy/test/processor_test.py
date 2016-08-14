# coding=utf-8
from cppy.adaptor import CpRqRpClass, CpSubPubClass
from cppy.processor import EventProcessor

evntproc = None

@CpRqRpClass('CpSysDib.StockChart')
class StkChart(object):
    def __init__(self):
        self.itm_cod = itm_cod
    
    def setInputValue(self, inputType, inputValue):
        self.inputType = inputType
        self.inputValue = inputValue
    
    def request(self, com_obj):
        com_obj.SetInputValue(0, self.itm_cod)
        com_obj.SetInputValue(1, ord('2'))
        com_obj.SetInputValue(4, 100)
        com_obj.SetInputValue(5, [0,5,8,9])
        com_obj.SetInputValue(6, ord('D'))

        com_obj.Request()

    def response(self, com_obj):
        cnt = com_obj.GetHeaderValue(3) #  수신개수
        for i in range(cnt):
            if i == 98:
                # 98번째에 show_series라는 키를 전달
                evntproc.push('show_series', self.itm_cod)

            if i == 0:
                evntproc.push('show_start', 'start')

            # 키와 값을 인자로 하여 이벤트처리기에 전달
            evntproc.push(self.itm_cod + '_clpr', com_obj.GetDataValue(0,i))



def echo(serieses, key, dat):
    print ('key:%s, dat:%s'%(key, dat))


def show_series(serieses, key, dat):
    if dat == 'start':
        print ('start')

    if dat == 'A003540':
        for val in serieses['A003540_clpr']:
            print (val)


# 윈도우의 경우 multiprocessing 사용시 (EventProcessor)
# if __name__ == "__main__" 에서 사용해야함
# https://docs.python.org/2/library/multiprocessing.html
if __name__ == "__main__":

    itm_cod = "A005930"

    # 이벤트처리기 구동
    evntproc = EventProcessor()
    # 옵저버를 등록함, A003540으로 시작하는 키가 도착하면 echo 를 수행함
    evntproc.add_observer([itm_cod + '*'], echo)
    # 옵저버를 등록함, show으로 시작하는 키가 도착하면 show_series를 수행
    evntproc.add_observer(['show*'], show_series)
    evntproc.start()

    # 차트 데이터 요청 (비동기)
    stkchart = StkChart()
    stkchart.request()


    import pythoncom, time
    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.01)
