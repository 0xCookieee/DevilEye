import sys
import os
import requests
import colorama
from colorama import *
import terminaltables
from terminaltables import SingleTable
from bs4 import BeautifulSoup

def ip():
	ip=input('type ip here : ')
	api_ip_connect = f"http://ip-api.com/json/{ip}"
	content = requests.get(api_ip_connect)
	data = content.json()
	try:
		query=data['query']
	except KeyError:
		query='None'
	try:
		country=data['country']
	except KeyError:
		contry='None'
	try:
		countryCode=data['countryCode']
	except KeyError:
		countryCode='None'
	try:
		region=data['region']
	except KeyError:
		region='None'
	try:
		regionName=data['regionName']
	except KeyError:
		regionName='None'
	try:
		city=data['city']
	except KeyError:
		city='None'
	try:
		timezone=data['timezone']
	except KeyError:
		timezone='None'
	try:
		isp=data['isp']
	except KeyError:
		isp='None'
	try:
		org=data['org']
	except KeyError:
		org='None'
	try:
		ias=data['ias']
	except KeyError:
		ias='None'
	try:
		zip=data['zip']
	except KeyError:
		zip='None'
	print('\r')
	print('----------------------------------')
	print('ip 	    : ' +query)
	print('----------------------------------')
	print('country	    : ' +country)
	print('----------------------------------')
	print('contryCode  : ' +countryCode)
	print('----------------------------------')
	print('region      : ' +region)
	print('----------------------------------')
	print('region name : ' +regionName)
	print('----------------------------------')
	print('city        : ' +city)
	print('----------------------------------')
	print('zip         : ' +zip)
	print('----------------------------------')
	print('timezone    : ' +timezone)
	print('----------------------------------')
	print('isp         : ' +isp)
	print('----------------------------------')
	print('organisation: ' +org)
	print('----------------------------------')
	print('association : ' +ias)
	print('----------------------------------')
	print('\r')
	
    
