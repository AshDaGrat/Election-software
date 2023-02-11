import json

data = (json.load(open("data/recd_data.json")))['data']

usn = []
splb = []
splg = []
asplb = []
asplg = []
csb = []
csg = []
acsb = []
acsg = []
scb = []
scg = []
ascb = []
ascg = []

for i in data:
    usn.append(i['USN'])
    splb.append(i['splb'])
    splg.append(i['splg'])
    asplb.append(i['asplb'])
    asplg.append(i['asplg'])
    csb.append(i['csb'])
    csg.append(i['csg'])
    acsb.append(i['acsb'])
    acsg.append(i['acsg'])
    scb.append(i['scb'])
    scg.append(i['scg'])
    ascb.append(i['ascb'])
    ascg.append(i['ascg'])

print("SPL - Boys")
for i in set(splb):
    print(f'{i} - {splb.count(i)}')
print()

print("SPL - Girls")
for i in set(splg):
    print(f'{i} - {splg.count(i)}')
print()

print("ASPL - Boys")
for i in set(asplb):
    print(f'{i} - {asplb.count(i)}')
print()


print("ASPL - Girls")
for i in set(asplg):
    print(f'{i} - {asplg.count(i)}')
print()

print("CS - Boys")
for i in set(csb):
    print(f'{i} - {csb.count(i)}')
print()

print("CS - Girls")
for i in set(csg):
    print(f'{i} - {csg.count(i)}')
print()

print("ACS - Boys")
for i in set(acsb):
    print(f'{i} - {acsb.count(i)}')
print()

print("ACS - Girls")
for i in set(acsg):
    print(f'{i} - {acsg.count(i)}')
print()

print("SC - Boys")
for i in set(scb):
    print(f'{i} - {scb.count(i)}')
print()

print("SC - Girls")
for i in set(scg):
    print(f'{i} - {scg.count(i)}')
print()

print("ASC - Boys")
for i in set(ascb):
    print(f'{i} - {ascb.count(i)}')
print()

print("ASC - Girls")
for i in set(ascg):
    print(f'{i} - {ascg.count(i)}')
print()
