Slack向けの絵文字を作成するプログラムです。
現在開発中で、local環境で動作する状態です。

動作確認環境
macOS: Big Sur Ver 11.6.4
Python: 3.11

使用方法
src/main.pyのmainメソッドに与える引数を任意の文字列に変更してください。
改行も入れた場合、改行込みでSlackの絵文字用のサイズの絵文字が作成され、
save/ ディレクトリ配下に出力されます。