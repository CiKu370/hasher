import random , sys

# Color
B = "\033[34m"; Y = "\033[33m"; G = "\033[32m"; W = "\033[0m";R = "\033[31m";C = "\033[36m";P = "\033[46m";

# Random color
x = ("\033[")
rand = (x+"31m",x+"32m",x+"34m",x+"35m",x+"36m",x+"0m")
P = random.choice(rand)


def ban_1():

	print (Y+"\n 0{==================================================}0")
	print (Y+" | "+P+"   __ __         __            "+R+"Hash Cracker "+W+"2.3.6"+Y+"  |")
	print (Y+" | "+P+"  / // /__  ___ / /  ___ ____  "+Y+"                    |")
	print (Y+" | "+P+" / _  / _ `(_-</ _ \/ -_) __/  "+B+"["+W+"="+B+"]"+W+" Author : Ci Ku"+Y+"  |")
	print (Y+" | "+P+"/_//_/\_,_/___/_//_/\__/_/     "+B+"["+W+"="+B+"] "+W+"Team   : ??"+Y+"     |")
	print (Y+" |                                                    |")
	print (Y+" |        "+B+"  ["+R+"+"+B+"] "+W+"python2 "+sys.argv[0]+" --info "+B+"["+R+"+"+B+"]"+Y+"            |")
	print (Y+" 0{==================================================}0\n")

def ban_2():
	print (R+'\n                Hash Cracker'+W+' 2.3.6')
	print (W+'    -------------------------------------------')
	print (P+'    88  88    db    .dP"Y8 88  88 888888 88""Yb ')
	print (P+'    88  88   dPYb   `Ybo." 88  88 88__   88__dP ')
	print (P+'    888888  dP__Yb  o.`Y8b 888888 88""   88"Yb  ')
	print (P+'    88  88 dP""""Yb 8bodP  88  88 888888 88  Yb ')
	print (W+'    -------------------------------------------')
	print (W+'    Author : Ci Ku                    Team : ??\n')

def info():

	print (Y+"\n 0{======================"+W+" INFO "+Y+"=======================}0")
	print (Y+" |"+B+" ["+R+"="+B+"] "+W+"Name     "+C+":"+W+" Hasher"+Y+"                               |")
	print (Y+" |"+B+" ["+R+"="+B+"] "+W+"Code     "+C+":"+W+" python"+Y+"                               |")
	print (Y+" |"+B+" ["+R+"="+B+"] "+W+"Version  "+C+":"+W+" 2.3.6 (beta)"+Y+"                         |")
	print (Y+" |"+B+" ["+R+"="+B+"] "+W+"Author   "+C+":"+W+" debby anggraini ~ Ci Ku"+Y+"              |")
	print (Y+" |"+B+" ["+R+"="+B+"] "+W+"Email    "+C+":"+W+" XnVer404@gmail.com"+Y+"                   |")
	print (Y+" |"+B+" ["+R+"="+B+"] "+W+"Github   "+C+":"+W+" https://github.com/ciku370"+Y+"           |")
	print (Y+" |"+B+" ["+R+"="+B+"] "+W+"Date     "+C+":"+W+" 23 - 02 - 2018"+Y+"                       |")
	print (Y+" |"+B+" ["+R+"="+B+"] "+W+"Team     "+C+":"+W+" ??"+Y+"                                   |")
	print (Y+" 0{===================================================}0\n")
	print (B+" ["+R+"="+B+"] "+W+"python2 "+sys.argv[0]+" -u           to update wordlist "+B+"["+R+"="+B+"]")
	print (B+"\n ["+R+"="+B+"] "+W+"list hash supported : "+Y+"["+W+"01"+Y+"] "+C+"md4")
	print (Y+"                           ["+W+"02"+Y+"] "+C+"md5")
	print (Y+"                           ["+W+"03"+Y+"] "+C+"sha1")
	print (Y+"                           ["+W+"04"+Y+"] "+C+"sha224")
	print (Y+"                           ["+W+"05"+Y+"] "+C+"sha256")
	print (Y+"                           ["+W+"06"+Y+"] "+C+"sha384")
	print (Y+"                           ["+W+"07"+Y+"] "+C+"sha512")
	print (Y+"                           ["+W+"08"+Y+"] "+C+"ripemd160")
	print (Y+"                           ["+W+"09"+Y+"] "+C+"whirlpool\n"+W)

def ban_3():
	print (R+"\n                     Hash Cracker"+W+" 2.3.6")
	print (P+"   ___       ___       ___       ___       ___       ___   ")
	print (P+"  /\__\     /\  \     /\  \     /\__\     /\  \     /\  \  ")
	print (P+" /:/__/_   /::\  \   /::\  \   /:/__/_   /::\  \   /::\  \ ")
	print (P+"/::\/\__\ /::\:\__\ /\:\:\__\ /::\/\__\ /::\:\__\ /::\:\__\ ")
	print (P+"\/\::/  / \/\::/  / \:\:\/__/ \/\::/  / \:\:\/  / \;:::/  /")
	print (P+"  /:/  /    /:/  /   \::/  /    /:/  /   \:\/  /   |:\/__/ ")
	print (P+"  \/__/     \/__/     \/__/     \/__/     \/__/     \|__|  \n")

def banner():
	angka = ("1","2"," 3")
	rand = random.choice(angka)
	if rand == "1":
		ban_1()
	elif rand == "2":
		ban_2()
	elif rand == " 3":
		ban_3()
