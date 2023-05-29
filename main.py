import okx.Funding as Funding
import time
import random
import sys

#交易模式
flag = "0"  # live trading: 0, demo trading: 1

#API服务器
domain = 'https://www.okx.com'

#DEBUG模式
debug = False 

#===========================相当重要！================================

#密钥信息
api_key = "aaaaaaaaa"
secret_key = "aabbbbbbbb"
passphrase = "cccccccccbb"

#延迟时间范围
min_seconds = 5      #最低
max_seconds = 10     #最高

#提币数量随即范围
min_amt = 5     #最低
max_amt = 10    #最高s
digits=4   #小数位精度（保留几位小数）


#提币币种
ccy = 'USDT' 
fee = '0.0000' #参考交易所
chan = 'USDT-OKTC' #链
#=====================================================================


fundingAPI = Funding.FundingAPI(api_key, secret_key, passphrase, False, flag,domain,debug)


#地址列表
addr=[
'0xaaaaaaaaaaaaaaaaaaa',#派生A1
'0xnnnnnnnnnnnnnnnnnnnnn,#派生A2
]





total= len(addr)
i=0

for toAddr in iter(addr):
    sleepTime=random.randint(min_seconds,max_seconds)
    print('*******************************')
    print(f"随机延迟【{sleepTime}】秒开始循环任务")
    time.sleep(sleepTime)
    print('-------------------------------')
    i=i+1
    amt = round(random.uniform(min_amt,max_amt),digits)
    print(f"当前任务{i},总任务数{total}")
    print(f"发送提币任务至OKEX\n地址：【{toAddr}】\n网络：【{chan}】\n币种：【{ccy}】\n数量：【{amt}】\n费用：【{fee}】")
    print('-------------------------------')
    result = fundingAPI.withdrawal(ccy,amt,4,toAddr,fee,chan)
    #print(result)
    code_value = result.get('code')
    if code_value == '0':
        print(f"成功提现至【{toAddr}】")
        print('*******************************')
        print('')
        print('')

    else:
        print(f"服务器返回错误代码【{code_value}】")
        print('')
        print('-------------------------------')
        print('---------脚本退出运行-----------')
        print('-------------------------------')
        sys.exit()
print('###############################')
print('全部任务已成功提交')
print('###############################')




