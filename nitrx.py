import random 
import string

dmd = "Betwee the number of codes"

print()
print("\n"	"Welcome To Nitrx")
print()

f = open('nitro_codes.txt', 'a')
print()
print(dmd)
amount = int(input())
fix = 1
while fix <= amount:
    code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    discord_url = "https://discordapp.com/gifts/"
    f.write(discord_url + code + '\n')
    discord_code = discord_url + code
    print(discord_code)
    fix += 1
    
print()    
print("Version Is 0.1")
print()
print("Created By Sanchez")
print()
print("Discord Support : https://discord.gg/2Ptw6HH")
