
try:
  i = int(input())
  y = int(input())
  ans = ((i * y) / 2)
  print(ans)
except ValueError:
  print('数値以外が入力されました。')
except NameError:
  print('計算が正常にされませんでした。')
