fenshu = int(input("请输入您的分数成绩:"))

if fenshu >= 90:
    print(f'分数:{fenshu}→等级:A ')
elif 80 <= fenshu <=89:
    print(f'分数:{fenshu}→等级:B')
elif 70 <= fenshu <=79:
    print(f'分数:{fenshu}→等级:C')
elif 60 <= fenshu <=69:
    print(f'分数:{fenshu}→等级:D')
elif 0 <= fenshu < 60:
    print(f'分数:{fenshu}→等级:E')
else :
    print("输入错误了,你这分数是人能考出来的吗?")