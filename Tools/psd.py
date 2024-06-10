# necessary imports
import secrets
import string
from datetime import datetime, date

# define the alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

# fix password length
pwd_length = 16

# generate a password string
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

# catch a current time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
day = today.strftime("%b-%d-%Y")

print(pwd)

file1 = open("psds.txt", "a")
file1.write(pwd +" ("+current_time +" "+  day + ") " +'\n')
file1.close()
