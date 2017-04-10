from pyfilesec import SecFile




def Close():
    	s = SecFile("fruitcsv.csv")
	s.encrypt("pub_RSA.pem")

def Open():
	s = SecFile("fruitcsv.enc")
	r = raw_input("Enter phrase: ")
	s.decrypt("priv_RSA.pem",r)


