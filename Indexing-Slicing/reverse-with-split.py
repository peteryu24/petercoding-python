str1 = 'Hello Python World'
lt1 = str1.split()
lt2 = []

for kk in lt1:
   lt2.append(kk[::-1])

str2 = " ".join(lt2)
str2
