def capital(txt):
	return txt.upper()

def small(txt):
	return txt.lower()


#used in line 15 """"multi line text"""


def sms(msg):
	# storing the function in a variable
    message = msg("""Hi, I am created by a function
					passed as an argument.""")
    print (message)

def main():
    sms(small)
    sms(capital)
    print(capital.__name__)

if __name__=='__main__': main()