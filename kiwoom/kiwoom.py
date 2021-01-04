from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()

        print("Kiwoom class")

        # eventLoop 모음
        self.login_event_loop = None
        ###############

        # 변수 모음
        self.account_num = None
        ##########

        self.get_ocx_instance()
        self.event_slots()

        self.signal_login_commConnect()
        self.get_account_info()

    def get_ocx_instance(self):
        self.setControl('KHOPENAPI.KHOpenAPICtrl.1')

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot)

    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")

        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def login_slot(self, errCode):
        print(errCode)
        print(errors(errCode))


        self.login_event_loop.exit()

    def get_account_info(self):
        account_list = self.dynamicCall("GetLoginInfo(String)", "ACCNO")

        self.account_num = account_list.split(';')[0] # '12312323;' TO [12312323]
        print('나의 보유 계좌번호 %s ' % self.account_num)
