

infor = {}
print(infor)

addr = '996'
id = 1
infor[addr] = {'id':id, 'x':200}
print(infor['996'])
print(infor['996']['id'])

addr = '997'
id = 2
infor[addr] = {'id':id, 'x':200}
print(infor['997']['id'])


for key in infor:
    print(key)
# for key in :
    # print(key,"aaaa")

for key in infor:
    print(infor[key])
    if infor[key]['id']==1:
        print('aaaaaaaaaaaaaa')

del infor['996']
print(infor)