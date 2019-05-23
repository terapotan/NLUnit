import inspect
class numtest:
    def retNum(self):
        print("abc")
        return 1
    def executeTestCasesInMyClass(self):
        for testCaseFunctionName in inspect.getmembers(self,inspect.ismethod):

            # 下の行を消すと自分の関数を永遠に呼び出し続けてしまう(再起無限ループ)
            if testCaseFunctionName[0] == 'executeTestCasesInMyClass':
                continue
            eval('self.'+testCaseFunctionName[0]+'()')
