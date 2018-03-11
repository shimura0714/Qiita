import sys

var1 = sys.argv[1]
var2 = sys.argv[2]

if var1 < var2:
  print ("%s < %s" %(var1,var2))
else:
  print ("Err")

var3 = 0
var4 = 10
while var3 < var4:
  print (var3)
  var3 += 1;

for var5 in range(5):
  print (var5) 

for var5 in range(0, 10):
  print (var5) 

for argv in sys.argv:
  print (argv) 