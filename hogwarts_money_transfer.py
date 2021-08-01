import time
question1 = input("您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？\n")
if question1 == '需要':
    question2 = input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询\n')
    if question2 == '2':
        print("十二的留言:不要真的把钱付给我了哦~")
        time.sleep(1)
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        time.sleep(1)
        money = float(input("请问您需要兑换多少金加隆呢？\n"))
        time.sleep(0.5)
        print("好的，我知道了，您需要兑换" + str(money) + "金加隆。")
        time.sleep(1)
        print("那么，您需要付给我" + str(float(money*51.3)) + "人民币。")
        time.sleep(0.5)
        print('请选择付款方式——')
        payment = input('1.微信 2.支付宝(可使用花呗) 3.银联 4.财付通\n')
        if payment == '1':
            print('正在为您生成微信付款二维码，请稍等……')
            time.sleep(1)
            print("您的专属微信付款二维码正在打印中,由于微信方面服务与魔法世界的连接不稳定,请手动输入金额并在稍后回填交易单号~")
            time.sleep(0.5)
            print("Error!请复制链接 http://transfer.hogwarts.asia/wechat.html 前往兑换~") # 其实这里是想收款码转字符画然后一行一行print出来的，但生成出来太太太大了……
            time.sleep(1.5)
            paid = input("请回填单号:")
            time.sleep(1.5)
            print("正在上报您的单号:" + paid + ",若单号正确,金加隆将会自动到账~")
        elif payment == '2':
            print('正在为您生成支付宝付款二维码，请稍等……')
            time.sleep(1)
            print("您的专属支付宝付款二维码正在打印中,由于阿里方面服务与魔法世界的连接不稳定,请手动输入金额并在稍后回填交易单号~")
            time.sleep(0.5)
            print("Error!获取失败咯~请复制链接 http://transfer.hogwarts.asia/alipay.html 前往兑换~")
            time.sleep(1.5)
            paid = input("请回填单号:")
            time.sleep(1.5)
            print("正在上报您的单号:" + paid + ",若单号正确,金加隆将会自动到账~")
        elif payment == '3':
            print('请使用微信或支付宝绑定银行卡支付哦~麻烦重新排队吧!')
        elif payment == '4':
            print("暂不支持QQ支付哦,请尝试其他兑换方式!麻烦重新排队吧~")
        else:
            print("听不懂你在说什么哦,不过我知道你需要重新排队啦!")
    elif question2 == '1':
        print("推荐你去存取款窗口哦")
        time.sleep(0.5)
        print(input("如果没有其他问题,输入任意内容即可退出~"))
        quit()
    elif question2 == '3':
        print("推荐你去咨询窗口哦")
        time.sleep(0.5)
        print(input("如果没有其他问题,输入任意内容即可退出~"))
    else:
        print("听不懂你在说什么哦,有需要再来找我吧~")
        time.sleep(0.5)
        print(input("如果没有其他问题,输入任意内容即可退出~"))
        quit()
elif question1 == '不需要':
    print('好的，再见。')
    time.sleep(1)
    print(input("输入任意内容退出~"))
    quit()
else:
    print("听不懂你在说什么哦,有需要再来找我吧~")

time.sleep(1)
print("业务办理完成啦,如果有需要可以重新排队哦~")
time.sleep(1)
print(input("输入任意内容退出……"))
quit()
