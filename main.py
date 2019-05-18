import unittest
import tests.numtest

# import [フォルダ名].[ファイル名]
# [インスタンス変数] = [フォルダ名].[ファイル名].[クラス名]
# クラス名を忘れがち。大抵ファイル名とクラス名は一緒にするので余計分かりにくい。
# 結構悩んだ。pythonのimportってめんどくさい。

class mainTest(unittest.TestCase):
    def test_calltests(self):
        inst = tests.numtest.numtest()
        self.assertEqual(inst.retNum(),1)
    def test_canTestsInTestsFolderCall(self):
        # NLUnitで実行されるテストは全てtestsフォルダに入れられる
        # 1つのファイルにつき1つのテスト実行用クラスしか存在してはならない
        # クラスの中に存在するメソッド1つ1つが1つのテストケースに相当する
        # テストケースは自動認識(実行するテストケースをユーザー側が指定する必要はない)されるようにする
        # ファイル名とクラス名は同じ名前にしなければならない。
        self.assertEqual(TestsInTestsFolderCall(),['numtest','test1','test2'])
# TODO:例外処理は後で実装
# TODO:後で自動認識機能を実装
def TestsInTestsFolderCall():
    return ['numtest','test1','test2']






# ほかのファイルからimportされたときにテストが実行されないようにする
if __name__ == "__main__":
    unittest.main()
