from pyfilesec import SecFile



def Close():
    	s = SecFile("creditcard.csv")
	s.encrypt("pub_RSA.pem")

def Open():
	s = SecFile("creditcard.enc")
	r = raw_input("Enter phrase: ")
	s.decrypt("priv_RSA.pem",r)

