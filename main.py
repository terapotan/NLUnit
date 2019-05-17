import unittest
import tests.numtest
# import [フォルダ名].[ファイル名]
# [インスタンス変数] = [フォルダ名].[ファイル名].[クラス名]
# クラス名を忘れがち。大抵ファイル名とクラス名は一緒にするので余計分かりにくい。
# 結構悩んだ。pythonのimportってめんどくさい。







class mainTest(unittest.TestCase):
    def test_calltests(self):
        inst = tests.numtest.numtest()
        self.assertEqual(inst.retNum,1)


if __name__ == "__main__":
    unittest.main()
