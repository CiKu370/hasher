#! usr/bin/python

"""
                             0={  HAI STALKER }=0

"""
import sys
import hashlib
import time
import os

B = "\033[34m"; Y = "\033[33m"; G = "\033[32m"; W = "\033[0m";R = "\033[31m";


def banner():
	print (G+"   __ __         __           "+W+"|    "+R+"Hash Cracker")
	print (G+"  / // /__ ____ / /  ___ ____ "+W+"|")
	print (G+" / _  / _ `(_-</ _ \/ -_) __/ "+W+"| "+B+"[=]"+W+" Author : Ci Ku")
	print (G+"/_//_/\_,_/___/_//_/\__/_/    "+W+"| "+B+"[=] "+W+"I LOVE YOU "+R+":*\n"+W)

try:
        from tqdm import *
except ImportError:
        banner()
	time.sleep(0.5)
        print (B+"["+W+"="+B+"] "+G+"installing module "+R+"tqdm"+W)
        os.system("pip2 install tqdm")
	print (B+"["+W+"="+B+"] "+G+"install success , run program again")
        sys.exit()

def cek():
	banner()
	hash_str = raw_input(B+"["+W+"?"+B+"]"+G+" Hash : "+W)
	if hash_str == '':
		time.sleep(0.5)
		print (B+"["+R+"!"+B+"] "+G+"Hash error")
		sys.exit()
	print (B+"["+W+"="+B+"] "+G+"Cek Hash Type ...")
	time.sleep(1)

	# jangan di utak atik cok

	SHA512='dd0ada8693250b31d9f44f3ec2d4a106003a6ce67eaa92e384b356d1b4ef6d66a818d47c1f3a2c6e8a9a9b9bdbd28d485e06161ccd0f528c8bbb5541c3fef36f'
	md5 = 'ae11fd697ec92c7c98de3fac23aba525'
	sha1 = '4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333'
	sha224 ='e301f414993d5ec2bd1d780688d37fe41512f8b57f6923d054ef8e59'
	sha384 = '3b21c44f8d830fa55ee9328a7713c6aad548fe6d7a4a438723a0da67c48c485220081a2fbc3e8c17fd9bd65f8d4b4e6b'
	sha256 = '2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e'

	if len(hash_str)==len(SHA512) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
	        print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"sha512")
		hash = "SHA512"

	if len(hash_str)==len(md5) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"md5")
		hash = 'md5'

	if len(hash_str)==len(sha1) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"sha1")
		hash = 'sha1'


	if len(hash_str)==len(sha224) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"SHA224")
		hash = "SHA224"

	if len(hash_str)==len(sha384) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"SHA384")
		hash = "SHA384"

	if len(hash_str)==len(sha256) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"sha256")
		hash = 'sha256'

	print (B+"["+W+"="+B+"] "+G+"cek wordlist..")
	time.sleep(1)
	try:
		w = open("wordlist.txt","r").readlines()
		x = len(w)
	except IOError:
		print (R+"["+W+"="+B+"]"+G+" wordlist not found\n")
		sys.exit()
	date = time.asctime()
	time.sleep(0.3)
	print (B+"["+R+"="+B+"] "+G+"load "+W+"{}"+G+" word in "+W+"wordlist.txt").format(x)
	print (B+"["+W+"*"+B+"] "+G+"start ..\n")
	time.sleep(1)
	print (B+"["+W+"{}"+B+"] "+G+"Cracking..."+Y).format(date)
	try:

	        for line in tqdm(w):
			line = line.strip()
	                h = hashlib.new(hash)
	                h.update(line)
			time.sleep(0)
			if "=== selesai ===" in line:
				print (B+"["+W+"{}"+B+"]"+G+" password not found\n").format(date)
				sys.exit()
			if h.hexdigest() == hash_str:
				print (B+"\n["+W+"{}"+B+"] "+G+"Stopped...\n").format(date)
				time.sleep(0.3)
				print (B+"["+W+"="+B+"]"+G+" password found ")
                        	print (B+"["+W+"+"+B+"] "+W+hash_str+G+" 0={==> "+W+line)
				sys.exit()
	except UnboundLocalError:
		print (R+"\n["+W+"!"+R+"] "+G+"Error Hash Type Not Supported\n")
		sys.exit()
	except IOError:
                print (B+"["+W+"!"+R+"]"+G+" I cannot load this file:"+W+hash)
		sys.exit()

if __name__ == "__main__":
	cek()

