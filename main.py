import unittest
import tests.numtest
import os
import importlib

# import [フォルダ名].[ファイル名]
# [インスタンス変数] = [フォルダ名].[ファイル名].[クラス名]
# クラス名を忘れがち。大抵ファイル名とクラス名は一緒にするので余計分かりにくい。
# importのパスは最初に実行したファイル(今回の場合だとmain.py)起点で決まるらしい。
# 結構悩んだ。pythonのimportってめんどくさい。

class mainTest(unittest.TestCase):
    def test_canTestsInTestsFolderCall(self):
        # NLUnitで実行されるテストは全てtestsフォルダに入れられる
        # 1つのファイルにつき1つのテスト実行用クラスしか存在してはならない
        # クラスの中に存在するメソッド1つ1つが1つのテストケースに相当する
        # テストケースは自動認識(実行するテストケースをユーザー側が指定する必要はない)されるようにする
        # ファイル名とクラス名は同じ名前にしなければならない。
        # クラスにはexecuteTestCasesInMyClass_[クラス名]という名前の関数を必ず入れる
        # その関数でクラス中に存在するテストケースを全て呼び出すようにする。

        # FIXME:testsに存在するファイル名を確かめるだけでは意図した通りテストされていない
        self.assertEqual(callTestsInTheTestsFolder(),set(['numtest','test1','test2']))

# TODO:例外処理は後で実装
# FIXME:テストを実行するたびにファイルをimportしている。これは明らかに無駄であるため将来的にテストを複数回実行するとき修正が必要だろう。
def callTestsInTheTestsFolder():
    fileNameListInTestsFolder_noext = [os.path.splitext(fileName)[0] 
                                        for fileName
                                        in os.listdir("./tests/") 
                                        if os.path.isfile(os.path.join("./tests/",fileName))]

    # testsフォルダ内のファイルを全てimportする
    for importFileName in fileNameListInTestsFolder_noext:
        importlib.import_module("tests."+importFileName)

    for testCaseClassName in fileNameListInTestsFolder_noext:

        # 右辺一つ目のtestCaseClassNameはクラスが入っているファイルの名前である。
        classAbsolutePathName_nolastdot = 'tests.' + testCaseClassName + '.' + testCaseClassName
        
        testCaseClassInstance = eval(classAbsolutePathName_nolastdot+'()')
        testCaseClassInstance.executeTestCasesInMyClass()

    return set(fileNameListInTestsFolder_noext)





# ほかのファイルからimportされたときにテストが実行されないようにする
if __name__ == "__main__":
    unittest.main()

