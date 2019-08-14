try:
	import cpp
	import socket
	import socketserver
	import nano
	import data
	import sql
	import os, sys
	import http, http.server, http.client
	import time, datetime
	import html
	import request, requests, mechanize
	import pyautogui
	import pyscreenshot
	import internet, connection
	import lib
	import wave
	import numpy
	import math
	import lanscan
	import visa
	import subprocess
	import multiprocess
	import pathlib
	import copy
	import cmd
	import json
	import site
	import encoders
	import array
	import io
	import errno
	import getopt
	import colorsys
	import abc
	import dill
	from MSFLib import *
except ModuleNotFoundError:
	print('\033[1;31;40m[-]\033[1;37;40m Please hit pip install -r requirement.txt')
	print()
	exit()

l='\033[4;4;5m'
w='\033[1;37;40m'
r='\033[1;31;40m'
g='\033[1;32;40m'
b='\033[1;34;40m'
y='\033[1;33;40m'
c='\033[1;36;40m'
n='\033[0;0;0m'

ri=r+'[-]'+w+' '
gi=g+'[+]'+w+' '
bi=b+'[*]'+w+' '
yi=y+'[!]'+w+' '

host=[]
port=[]
session=[]
protocol=[]

if sys.version_info < (3,0):
	print(ri,'crashed system')
	print(yi,'please hit: chmod +x *\n./main_installer')
	
else:
	print(gi,'started msf_console')
	print()
	while 1:
		try:
			msf=input(l+'msf'+n+w+' > ')
			if msf=='help' or msf=='?':
				print(bi,'help: ')
				print()
				print('\thelp																									to need the help')
				print()
				print('\texploit																							to start attacking with a public ip')
				print('\ttcp_exploit																					to start attacking using tcp protocol with a public ip')
				print('\ttcp4_exploit																					to start attacking using tcp protocolwith public IPv4')
				print('\ttcp6_exploit																					to start attacking using tcp protocolwith public IPv6')
				print('\tudp_exploit																					to start attacking using udp protocol with public ip')
				print('\tudp4_exploit																					to start attacking using udp protocol with public IPv4')
				print('\tudp6_exploit																					to start attacking using udp protocol with public IPv6')
				print('\tlocal exploit																				to start attacking using set protocol with private IPv4')
				print('\exploit_room																					to start attacking using a virtual room with multi ip type')
				print()
				print('use + option																						to use the option from MajorSploitFramework Modules')
				print('mkf + option																						to make a virus_name from MajorSploitFramework Modules')
				print()
				print('\tconnect																							to connect to the Major SimpleServer')
				print('\tlisten																								to listen to the trijans')
				print()
				print('\tset + option + valule																to done a valule to an option')
				print('\tset remove + option																	to remove the valule of set option')
				print()
				print('\tcheck																								is a simple update and upgrade installer and checker')
				print('\tupdate																								to check for updates and install it')
				print('\tupgrade																							to check for upgrades and install it')
				print('\tinstall update																				to install the update')
				print('\tinstall upgrade																			to install the upgrade')
				print()
				print('\tpublic ifconfig.me																		to get your public ip')
				print('\tbanner																								to show a banner')
				print('\tcbanner																							to clear the win and shoz a banner')
				print()
				print('\treboot																								to relaunch the system')
				print('\texit																									to exit')
				print('\tcExit																								to clear the win and exit')
				print()
				print('\toriginal system command															if the command not found it is use the termux command')
				
			elif 'set host ' in msf or 'set HOST ' in msf:
				valule=msf.split()[-1]
				host.append(valule)
				if host==[]:
					print(bi,'conf: ')
					print('host None')
					
				else:
					print(bi,'conf: ')
					print('host '+valule)
				
			elif 'set port ' in msf or 'set PORT ' in msf:
				valule=msf.split()[-1]
				port.append(valule)
				if port==[]:
					print(bi,'conf: ')
					print('port None')
					
				else:
					print(bi,'conf: ')
					print('port '+valule)
				
			elif 'set session ' in msf or 'set SESSION ' in msf:
				valule=msf.split()[-1]
				session.append(valule)
				if session==[]:
					print(bi,'conf: ')
					print('session None')
					
				else:
					print(bi,'conf: ')
					print('session '+valule)
					
					
			elif 'set protocol ' in msf or 'set proto ' in msf:
				valule=msf.split()[-1]
				protocol.append(valule)
				if protocol==[]:
					print(bi,'conf: ')
					print('protocol None')
					
				else:
					print(bi,'conf: ')
					print('protocol '+valule)
				
			elif 'set remove ' in msf or 'set REMOVE ' in msf:
				option=msf.split()[-1]
				if option=='host' or option=='HOST':
					host.remove(host[0])
					if host!=[]:
						for i in len(host):
							host.remove(host[0])
							
						print(bi,'removed host')
						print('host None')
						
					else:
						print(bi,'removed host')
						print('host None')
						
				elif option=='port' or option=='PORT':
					port.remove(port[0])
					if port!=[]:
						for i in len(port)
							port.remove(port[0]) 
						
						print(bi,'removed host')
						print('host None')
						
					else:
						print('removed port')
						print('port None')
						
				elif option=='session' or option=='SESSION':
					session.remove(session[0])
					if session!=[]:
						for i in len(session):
							session.remove(session[0])
							
						print(bi,'removed host')
						print('host None')
						
					else:
						print(bi,'removed host')
						print('host None')
						
				elif option=='protocol' or option=='proto' or option=='PROTOCOL' or option=='PROTO':
					protocol.remove(protocol[0])
					if protovol!=[]:
						for i in len(protocol):
							protocol.remove(protocol[0])
							
						print(bi,'removed host')
						print('host None')
						
					else:
						print(bi,'removed host')
						print('host None')
						
				else:
					print(bi,'error cannot removing this option')
					print()
					continue
			elif 'use ' in msf:
				lib=msf.split()[-1]
				importlib.import_module(lib)
				
			else:
				os.system(msf)
				print()

		except KeyboardInterrupt:
			print(bi+'exiting .......')
			print(yi+'all processings are killed')
			exit()
			
		except EOFError:
			print(bi+'exiting .......')
			print(yi+'all processings are killed')
			exit()
			
		except IndexError:
			print(bi,'no valule to remove it')
			continue
			
		except ModuleNotFoundError:
			print('option not found')
			continue
		except:
			print(bi+'not foundet attribut')
			conf=input(yi+'wold like to exit[Y/n]: ')
			if conf=='y' or conf=='Y' or conf=='\n':
				print(bi+'exiting .......')
				print(yi+'all processings are killed')
				exit()
				
			elif conf=='n' or conf=='N':
				print(bi+'cansled exiting ')
				continue
				
			else:
				print(bi+'cansled exiting ')
				continue
