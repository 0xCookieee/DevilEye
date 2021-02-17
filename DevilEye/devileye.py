#!/usr/bin/python3
import sys
sys.path.append('Modules')
import os
import time
import socket
import getpass
import time
from getpass import getpass
import namesearchus
from namesearchus import *
import namesearch
from namesearch import *
import phoneinfo
from phoneinfo import *
import tracer
from tracer import *
import colorama
from colorama import *
os.system('clear')
print(Fore.RED+'loading modules ...')
time.sleep(2)
print(Fore.GREEN+'modules loaded succesfully !')
time.sleep(1)
print(Fore.RED+'''
                              '....xxxxx...,'. '   
                           ..XXXXXXXXXXXXXXXXXXXXx.    
                        ..XXXXXXXXWWWWWWWWWWWWWWWWXXXX.  
                   ...XXXXXWWW"   W88N88@888888WWWWWXX.   
                 ...XXXXXXWWW"    M88N88GGGGGG888^8M "WMBX.    
               ..XXXXXXXXWWW"     M88888WWRWWWMW8oo88M   WWMX.    
           "XXXXXXXXXXXXWW"       WN8888WWWWW  W8@@@8M    BMBRX.        
          XXXXXXXX=MMWW":  .      W8N888WWWWWWWW88888W      XRBRXX.  
           ""XXXXXMM::::. .        W8@889WWWWWM8@8N8W      . . :RRXx.    
                   MMM::.:.  .      W888N89999888@8W      . . ::::"RXV    
                      MMMm::.  .      WW888N88888WW     .  . mmMMMMMRXx
                       ""MMmm .  .       WWWWWWW   . :. :,miMM"""  
                              ""MMMMmm . .  .  .   ._,mMMMM""" 
                                  ""MMMMMMMMMMMMM""" 
                                                    DevilEye Framework By Tetsu''')
print('\r')
print(Fore.RED+''' ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                              

''')
time.sleep(2)
def menu():
    os.system('clear')
    print(Fore.RED+'    ____            _ __')
    print('   / __ \___ _   __(_) /__  __  _____')
    print('  / / / / _ \ | / / / / _ \/ / / / _ \ '+Fore.BLUE)
    print(' / /_/ /  __/ |/ / / /  __/ /_/ /  __/')
    print('/_____/\___/|___/_/_/\___/\__, /\___/')
    print('                         /____/  FrameWork v1.01'+Style.RESET_ALL)
    print('------------------------------------------------------------------------------')
    print(Fore.BLUE+'''
    (1)--NameSearch--     (4)--NameSearchUs--(off)    
    
    (2)--ReversePhone--   
    
    (3)--IpInfo--               ~Made By Tetsu [Calamïty]~ '''+Fore.WHITE)
    print('\r')
    print('------------------------------------------------------------------------------')
    print('\r')
    try:
        choice = input(Fore.RED+"root"+Fore.WHITE+"☠"+Fore.RED+"Devileye"+Fore.RESET+": ")
        print('\r')
        if choice == "1":
            name_search()
            input('enter to main menu ...')
            menu()
        elif choice == "2":
            phone()
            input('enter to main menu ...')
            menu()
        elif choice == "3":
            ip()
            input('enter to main menu')
            menu()
        else:
            print('  incorrect choice ')
            print('\r')
            input('enter to main menu ...')
            menu()
    except KeyboardInterrupt:
            print('\n')
            sys.exit()
menu()
