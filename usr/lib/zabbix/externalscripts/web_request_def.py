#!/usr/bin/python
# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
import re
from StringIO import StringIO
import requests
import argparse
from random import randint
from time import sleep

__author__ = "Yan Bogush"
__copyright__ = "Copyright 2019, Yan Bogush"


s = requests.Session()
parser = argparse.ArgumentParser()
parser.add_argument('--auth_url', help='Страница с авторизацией', type=str)
parser.add_argument('--csrf_url', help='Страница с токеном', type=str)
parser.add_argument('--count_url', help='Страница с данными', type=str)
parser.add_argument('--regex_csrf', help='Регулярка для изъятия токена (в одинарных кавычках)', type=str)
parser.add_argument('--regex_count', help='Регулярка для изъятия числа оставшихся запросов (в одинарных кавычках)', type=str)
parser.add_argument('--login', help='Логин', type=str)
parser.add_argument('--passw', help='Пароль', type=str)
parser.add_argument('--name_login', help='Имя поля для ввода логина', type=str)
parser.add_argument('--name_passw', help='Имя поля для ввода пароля', type=str)
parser.add_argument('--name_csrf', help='Имя класса для изъятия токена csrf', type=str)

args = parser.parse_args()
auth_url = args.auth_url
csrf_url = args.csrf_url
count_url = args.count_url
regex_csrf = r"{}".format(args.regex_csrf)
regex_count = r"{}".format(args.regex_count)
login = args.login
passw = args.passw
name_login = args.name_login
name_passw = args.name_passw
name_csrf = args.name_csrf

def getcount():
	if csrf_url:
	    csrf_key = s.get(csrf_url)
	    matches = re.findall(regex_csrf, csrf_key.text, re.MULTILINE | re.IGNORECASE | re.DOTALL)
	    data_auth = {
		name_login: login,
		name_passw: passw,
		name_csrf: matches[0]
	    }
	else:
	    data_auth = {
		name_login: login,
		name_passw: passw
	    }

	sleep(1)
	auth_data_post = s.post(auth_url, data=data_auth, headers=dict(Referer=auth_url))
	sleep(1)
	count_url_get = s.get(count_url)
	data_count = re.findall(regex_count, count_url_get.text.encode('utf-8'), re.MULTILINE | re.IGNORECASE | re.DOTALL)
	
	if not data_count:
		return 0
	else:
		result = re.sub(r'[^\d,]+', '', data_count[0])
		result = re.sub(',', '.', result)
		return result
sleep(randint(1,5))
print(getcount())
