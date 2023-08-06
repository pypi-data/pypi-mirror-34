import sys
import os
from termcolor import cprint, colored
import argparse
from DrMoriaty.sherlock.libs import load_and_run_test
from DrMoriaty.sherlock.libs import search_in_db
from DrMoriaty.sherlock.test import load, ls_mod

from DrMoriaty.utils.log import gprint, lprint, rprint
from DrMoriaty.searcher.fofa_search import Fofa

from DrMoriaty.masscan.masscan import Masscan, MasscanDaemon

proxy= False
def masscan_do(args):
    if len(args.search) > 0:
        target = args.search[0]
        ports = []
        if len(args.search) > 1:
            ports = args.search[1:]

        mas = Masscan(target, *ports)
        return mas.run()
    return []

def db_do(args):
    if args.use == 'db':
        k = args.search[0]
        options = args.search[1:]
        return search_in_db(k, *options)

def fofa_do(args):

    if args.login:
        fofa = Fofa(proxy=args.proxy)
        e,p = fofa.login()
        u = {'username':e, 'password':p}
        
    else:
        fofa = Fofa(proxy=args.proxy)
        fofa.load_session_login()

    if len(args.search) % 2 ==0:
        keys = []
        for i in range(0,len(args.search), 2):
            keys.append("%s=\"%s\"" % (args.search[i],args.search[i+1]) ) 
        gprint(str(keys))
        return fofa.search(key=" && ".join(keys), page=args.page)
    else:
        return fofa.search(key=args.search[0], page=args.page)

def main():
    global proxy
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--search', nargs='*',help='search key : -s ')
    parser.add_argument('--use', default="db", help="can use fofa | masscan | db ")
    parser.add_argument('-l', '--list', action='store_true', default=False, help='list local db.')

    parser.add_argument('-p', '--page', type=int, default=4, help='set page to search in web')
    parser.add_argument('-P', '--proxy', action='store_true', default=False, help='set proxy')
    parser.add_argument('-t', '--test', nargs='*', help='use test module to test result')
    parser.add_argument('--login', action='store_true', default=False, help='login in fofa')
    
    parser.add_argument('--ls-mod', action='store_true', default=False, help='list module to use:')
    parser.add_argument('--masServer', action='store_true', default=False, help='list module to use:')
    
    args = parser.parse_args()
    prepare_test_info = []
    proxy = False
    
    if args.page == 1:
        page = None
    else:
        page = args.page

    if args.proxy:
        proxy = 'socks5://127.0.0.1:1080'
    else:
        proxy = False
    
    if args.masServer:
        ma = MasscanDaemon("/tmp/MasscanDaemon.pid")
        gprint("-- Start Masscan Report Service --")
        ma.start()

    if args.list:
        prepare_test_info = search_in_db()
        sys.exit(0)


    if args.search:
        if args.use == "fofa":
            prepare_test_info = fofa_do(args)
        elif args.use == "masscan":
            prepare_test_info = masscan_do(args)
        elif args.use == "db":
            prepare_test_info = db_do(args)

    if args.ls_mod:
        ls_mod()

    if args.test and len(args.test)> 0:
        gprint("Test -- > %s " % " ".join(args.test))
        load_and_run_test(prepare_test_info,*args.test)

if __name__ == '__main__':
    main()