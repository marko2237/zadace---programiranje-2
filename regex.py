import re

mail = input("Unesi e-mail (fpmoz): ")
eduid = input("Unesi eduID: ")

regex_mail = "^[a-z]+\\.[a-z]+@fpmoz\\.sum\\.ba$"

regex_eduid = "^[a-z]+[0-9]*@sum\\.ba$"

if re.match(regex_mail, mail):
    print("E-mail je točan.")
else:
    print("E-mail je netočan.")

if re.match(regex_eduid, eduid):
    print("eduID je točan.")
else:
    print("eduID netočan.")