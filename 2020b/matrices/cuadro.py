n = int ( input("Tamaño del cuadro?") )

ncol = n
nren = n

a = [ [0] * ncol for i in range(nren) ]

col = n // 2
ren = 0

for x in range(1,n*n+1) :
   a[ren][col] = x
   if x % n == 0 :
      ren = ren + 1
   else :
      ren = ren - 1
      col = col + 1

      if ren < 0 :
         ren = n - 1
   
      if col == n :
         col = 0

for ren in range(n) :
   for col in range(n):
      print ("%5d"%(a[ren][col]), end='')
   print()
