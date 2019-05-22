# DoingList
- ~~(testsフォルダに入ったソースコードに書かれている)retNum関数が1を返せるようにする~~
- testsフォルダに存在するテストケースがすべて実行される(testsフォルダにA,B,Cがあったら、A,B,Cに存在するテストすべてが実行される。)
    - ~~仮実装完了~~
    - ~~testsフォルダに存在するファイル名(拡張子は除く、.py以外のファイルはリストアップしない)をリスト形式で返す。~~
        - ~~仮実装完了~~
        - ~~testsフォルダに存在するファイル名をリストアップ(拡張子あり、.py以外のファイルもリストアップする)~~
        - ~~testsフォルダ内にあるファイルを全てimportする処理を実装~~
    - 全テストケース(メソッド)を実行することが出来る
        - ~~いくつかのクラスのsetupメソッドだけ実行できるようにする~~

# UML
```plantuml
class mainTest{

}
class numtest{
    + executeTestCasesInMyClass_numtest
}
class test1{
    + executeTestCasesInMyClass_test1
}
class test2{
    + executeTestCasesInMyClass_test2
}

numtest <-- mainTest
test1 <-- mainTest
test2 <-- mainTest
```