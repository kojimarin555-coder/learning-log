#把 num = 256 拆成百位、十位、个位并分别打印#
num = 256
gewei = num % 10
shiwei =num // 10 % 10
baiwei = num //100
print(baiwei,shiwei,gewei)

#fees = [150, 230, 300, 180, 400]
#找出第一个能被100整除的稿费打印出来并停止查找
fees = [150, 230, 300, 180, 400]
for x in fees:
    if x % 100 == 0:
        break
print(x)

#修改版
fees = [150, 230, 180, 400]
found = False


for x in fees:
    if x % 100 == 0:
            print(x)
            found =True
            break

if not found:
    print("没有找到整百的稿费哦")