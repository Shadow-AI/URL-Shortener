from scripts.gen import Generator


g=Generator()
g.validateURL('google.com')
print(g.linkMapper)
print(g.ageMapper)

#NOT USED