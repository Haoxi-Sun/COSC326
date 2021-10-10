Elsie Sun 4468203
----------------------------------------------------------------------------------------------------------------------------
Idea:
There are  conditions I need to consider:
Condition 1: Check "@", and "_at_" is allowed as well.
	     a)Check if there is "@" or "_at_";
	     b)The email address have replaced the "@" with "_at_";
	     c)Check for extra "@"

Condition 2: Replace "_dot_" via ".".

Condition 3: Determine whether or not the mailbox name is valid.
	     a) The mailbox name must be alphanumeric, and single hyphens and/or underscores are allowed.
	     b) If there are capital letters, should convert upper case to lower case.

Condition 4: Determine whether or not the domain extension is valid.
	     a) Only ["co.nz", "com.au", "co.ca", "com", "co.us", "co.uk"] are valid.
	     b) If the domain extension is invalid, IP address should be considered.

Condition 5: Determine whether or not the domain name is valid.
	     a) The domain name must be alphanumeric, and dots are allowed.

Condition 6: If there is an IP address
	     a) It is considered as IPv4 addresses.
	     b) Should have "[]".
----------------------------------------------------------------------------------------------------------------------------

If you want to run this program with a file, please input "python3 email.py < filename" in terminal.
Furthermore, I provided a test file called "TEST.txt" in the ETUDE_12, if you'd like to test, please input "python3 email.py < TEXT.txt" in the terminal.
----------------------------------------------------------------------------------------------------------------------------
TEST CASES:
aAGW0asf99@[415.15.415.41]
sCR8qsU.AyG@mr6LHpUClmKsnK7E6.co.uk
jiia_dot_asd.aLO@adda90IO.co.us
UHIU123_at_sot__dot@sdfOPO.co.nz
CEO@InsuroCorp.com
maffu@cs.otago.ac.nz
gerry_at_research.techies_dot_co.uk
bob.gmail.com
cath@[139.80.91.50]
AOcy123_at_gmail.com
Com.au
OIJ890@127.255.06.60
OIJ890@[127.255.06.60]
coallCALL_asd-asd@hotmail.ac.co.uk
asda21_211@asd@hasdl.co.ca
ASD0-as.sad!1@gasd.co.us
Asdij89asd!@asf.co.uk
._sad@asd.com.au
asf_afASFE=asf@sgsfdAF5263.co.ca
IMOAmiao,aa@hao.com
a4156AF_asd-asd.asd@gg.co.uk
asdfjio@[595.562.262.52]
cath@[139.80.91.50]]
cath@[[139.80.91.50]
cath@139.80.91.50
-Qfqewg.afsQWE_asf@asdasf.com
Qfqewg.afsQWE_asf@a..sdasf.com
Qfqewg.afsQWE_asf@.asdasf.com
sdfsd@[0.0.0.0]
aDSAS@[255.255.255.255]
dsasf@[256.12.100.2]
asfa@[150.2.105.50]
uiui@[45.125.20.56]
ASFjio-21@[175.226.162.172]
aasfIUG_as.asd@[135.25.15.88]
GYUBASF.asd.a@[108.10.200.16]
aa415a_s@[205.78.118.53]
HUI@[77.146.29.125]
GYUBASF.asd.a@[15.130.242.204]
cath@[0.130.16.247]
cath@[77.101.82.260]