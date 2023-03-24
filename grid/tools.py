h = int(input("請輸入身高(公分)"))
w = int(input("請輸入體重(公斤)"))

bmi = w/((h/100)**2)

print("您的BMI值為:%.4f" % bmi)
print("您的體重")

if bmi <18.5:
    print("太輕")
elif 25 > bmi >18.5:
    print("正常")
elif 30 > bmi >25:
    print("過重")
elif bmi > 30:
    print("肥胖")