import sys

cnt = 0
for str in sys.argv:
  #1つ目の引数は実行ファイル名なのでキャンセル
  if 0 < cnt:  
    print(str)
  cnt = cnt + 1 
