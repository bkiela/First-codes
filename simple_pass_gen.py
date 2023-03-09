import random as rnd
import string


pass_length = int(input("Enter the length of your password: "))

lcase = list(string.ascii_lowercase)
hcase = list(string.ascii_uppercase)
num = list(string.digits)
special = list(string.punctuation)

all_characters = lcase + hcase + num + special
rnd.shuffle(all_characters)

gen_pass = []

while len(gen_pass) < pass_length:
    indx = rnd.randrange(0, len(all_characters))
    sel_symb = all_characters[indx]
    gen_pass.append(sel_symb)
    generated_password = "".join(gen_pass)



print(f"Generated password of length {pass_length} is {generated_password}")
