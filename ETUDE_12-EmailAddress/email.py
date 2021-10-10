# Elsie Sun 4468203
# fing the IPv4 regular expression from:
# https://www.jb51.net/article/162641.htm

import fileinput
import re

ip_v4 = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
domain_extensions = ["co.nz","com.au", "co.ca", "com", "co.us", "co.uk"]
at = "_at_"
dot = "_dot_"
symbol = [".","-","_"]

# determine whether or not the mailbox name is valid
def check_mailbox(email):
    if email[0] in symbol: return False
    for i in range(len(email)):
        if email[i].isalnum() == False and email[i] not in symbol:return False
        if email[i] in symbol and email[i-1] in symbol:return False
    return True

# determine whether or not the domain extension is valid
# if it is valid, return the domain extension
# otherwise, return false
def check_domain_extension(email):
    for i in domain_extensions:
        if email.endswith(i): return i
    return False

# determine whether or not the domain name is valid
# single dots are allowed
def check_domain(email, i):
    domain = email.split("@")[1].split(i)[0]
    if domain[0] == ".": return False
    for i in range(len(domain)):
        if domain[i].isalnum() == False and domain[i] != ".": return False
        if domain[i] == "." and domain[i-1] == ".": return False
    return True

# determine whether or not the IP address is valid
# considered as IPv4 addresses
def check_ip(email):
    if re.match(ip_v4, email) is not None: return True
    return False

# check the format of IP address
def address_check(domain):
    num = 0
    for i in domain:
        if i == "[": num += 1
        if i == "]": num += 1
    if num != 2 or dot in domain: return False
    return True

for line in fileinput.input():
    line = line.replace("\n","")
    email_address = line.lower()

    # check @ symbol
    if "@" not in email_address and at not in email_address:
        print("{} <- Missing @ symbol".format(line))
        continue
    
    if "@" not in email_address and at in email_address:
        index = email_address.rfind(at)
        length = len(at)
        email_address = email_address[:index]+"@"+email_address[(index+length):]

    if "@" in email_address:
        if email_address.find("@") != email_address.rfind("@"):
            print("{} <- There are more than one @ symbol in the entered email address".format(line))

        else:       
            mailbox_name = email_address.split("@")[0]
            domain_ip = email_address.split("@")[1]

            # check the mailbox name
            if check_mailbox(mailbox_name) == False:
                print("{} <- Mailbox name is invalid".format(line))
            else:
                # check the domain extension
                if check_domain_extension(email_address) == False:
                    if domain_ip[0] == "[" and domain_ip[-1] == "]":
                        if address_check(domain_ip) == False: print("{} <- Invalid extension".format(line))
                        else:     
                            domain_ip = domain_ip.replace("[", "").replace("]", "")
                            if check_ip(domain_ip) == True: print(email_address)
                            else: print("{} <- Invalid extension".format(line))
                    else: print("{} <- Invalid extension".format(line))
                else:
                    # check the domain name
                    email_address = email_address.replace(dot, ".")
                    extension = check_domain_extension(email_address)
                    if check_domain(email_address, extension) == False:
                        print("{} <- Invalid domain name".format(line))
                    else:
                        print(email_address)
 