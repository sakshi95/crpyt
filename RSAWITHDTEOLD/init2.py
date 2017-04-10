from pyfilesec import SecFile
s = SecFile("creditcard.csv")
s.encrypt("pub_RSA.pem")

