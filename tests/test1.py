import inspect
class test1:
    def test1(self):
        print("call test1::test1.")
    def test2(self):
        print("call test1::test2.")
    def executeTestCasesInMyClass(self):
        for testCaseFunctionName in inspect.getmembers(self,inspect.ismethod):

            # 下の行を消すと自分の関数を永遠に呼び出し続けてしまう(再起無限ループ)
            if testCaseFunctionName[0] == 'executeTestCasesInMyClass':
                continue
            eval('self.'+testCaseFunctionName[0]+'()')