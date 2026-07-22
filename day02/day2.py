total = 0
fees =[150,200,180,220,150,300,250,180]
for i in fees:
    total += i
print(f'累计稿费是:{total}')

huazhi = 5000
total = 0
while huazhi >= 3:
    huazhi -= 3
    total += 1
print(f'总共接了{total}单,剩余{huazhi}张纸')

for i in [1,2,3,4,5]:
    if i == 3:
        break
    print(i)

total = 0
for n in [5, 2, 8]:
    total += n
    if n < 3:
        break
print(total)

total = 0
for n in [5, 2, 8]:
    if n < 3:
        break
    total += n
print(total)

total = 0
qian = [200, 180, 220, 90, 150, 300]
for i in qian:
    if i<100:
        break
    total += i
print(total)

total = 0
fees = [200, 180, 220, 90, 150, 300]
for i in fees:
    if i<100:
        continue
    total += i
print(total)