dan=2
for kk in range(1,10):
    str1 = f'{dan} x {kk} = {dan*kk}'
    print(str1) // #1
    

    
f = open('text.txt','w')

dan = 2
for kk in range(1,10):
    str1 = f'{dan} x {kk} = {dan*kk}'
    print(str1) // #2
    f.write(str1+'\n')

f.close()

f = open('text.txt','r')  

print(f.read()) // #3

f.close()

f = open('text.txt','r') 

while True:
    line = f.readline()
    if not line: 
        break
    print(line,end='') // #4
    
f.close()

f = open('text.txt','r') 
lt = f.readlines() 

for kk in lt:    
    print(kk, end='')  

f.close()
    
print(lt[3]) // #5
             // lt = #6
f = open('text.txt','a') 

dan=3
for kk in range(1,10):
    str1 = f'{dan} x {kk} = {dan*kk}'
    print(str1)
    f.write(str1+'\n')

f.close()



f = open('text.txt','r')

for kk in f:    
    print(kk, end='')  // #7

f.close()

with open('text.txt','w') as f: 
    for kk in range(1,10):
        str1 = f'2 x {kk} = {2*kk}'
        print(str1)  // #8
        f.write(str1+'\n') 
        
with open('text.txt','r') as f: 
    lt = f.readlines() 

for kk in lt:    
    print(kk, end='')  

print(lt[3])   // #9       

import csv    

f = open('output.csv', 'w', encoding='utf-8')
wr = csv.writer(f, lineterminator='\n')
wr.writerow(["Bob", 95,60,70])
wr.writerow(["Robert", 85,55,43])
f.close()

import csv
 
f = open('output.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    print(line) // #10

f.close()

import pandas as pd

df1 = pd.read_csv('output.csv', header = None)  // df1 = #10
