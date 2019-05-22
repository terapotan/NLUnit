# DoingList
- ~~(testsフォルダに入ったソースコードに書かれている)retNum関数が1を返せるようにする~~
- ~~testsフォルダに存在するテストケースがすべて実行される(testsフォルダにA,B,Cがあったら、A,B,Cに存在するテストすべてが実行される。)~~
    - ~~仮実装完了~~
    - ~~testsフォルダに存在するファイル名(拡張子は除く、.py以外のファイルはリストアップしない)をリスト形式で返す。~~
        - ~~仮実装完了~~
        - ~~testsフォルダに存在するファイル名をリストアップ(拡張子あり、.py以外のファイルもリストアップする)~~
        - ~~testsフォルダ内にあるファイルを全てimportする処理を実装~~
    - ~~いくつかのクラスのsetupメソッドだけ実行できるようにする~~
    - クラス内のすべての関数が実行されるようにする
        - ~~setupメソッドが実行されない問題を解消する~~
            - ~~インスタンス変数を使った形で関数を呼び出すようにする~~
        - クラス内に存在する関数を全てリストアップする

# UML
```plantuml
class mainTest{

}
class numtest{
    + executeTestCasesInMyClass
}
class test1{
    + executeTestCasesInMyClass
}
class test2{
    + executeTestCasesInMyClass
}

numtest <-- mainTest
test1 <-- mainTest
test2 <-- mainTest
```