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
        - ~~クラス内に存在する関数を全てリストアップする~~
        - ~~クラス内に存在する関数をすべて実行する(numtestのみ)~~
        - ~~クラス内に存在する関数をすべて実行する(testsフォルダに存在するすべてのクラス)~~
        - ~~クラス内に存在する関数が呼び出されたときに、それぞれ自身の関数名を表示するようにする。~~
    - executeTestCasesInMyClassの重複を排除する
        - ~~nlunitClassクラスを作成する~~
        - ~~numtest,test1,test2はnlunitClassクラスを継承する。~~
        - ~~executeTestCasesInMyClass()の実装をnlunitClassクラスで追加。~~
        - ~~重複を排除。~~

# UML
```plantuml
class mainTest{
}
class numtest{
    + test1()
    + test2()
}
class test1{
    + test1()
    + test2()

}
class test2{
    + test1()
    + test2()

}

class nlunitClass{
    + executeTestCaseInMyClass
}
numtest <-- mainTest
test1 <-- mainTest
test2 <-- mainTest
nlunitClass <|-- numtest
nlunitClass <|-- test1
nlunitClass <|-- test2

```