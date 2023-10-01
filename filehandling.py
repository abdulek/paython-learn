s = 'abdul is a good boy \n'
# using contact manager
with open('test.txt','a') as f:
    f.write(s)
    f.close()
# end contact manage
s = '\n'+s
# custom
fp = open('test.txt', 'r')
txt = fp.read()
print(txt)
#fp.write(s)
fp.close()
