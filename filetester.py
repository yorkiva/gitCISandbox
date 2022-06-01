import sys, os

checks_passed = True
fname_added = "added.txt"
fname_mod = "modified.txt"

try:
    f_mod = open(fname_mod, "r")
except:
    print("{} is not found!".format(fname_mod))
    sys.exit(1)
    
modfiles = []
if len(f_mod.readlines()) > 0:
    for f in f_mod.readlines():
        modfiles += f.strip().split(',')
for _file in modfiles:
    print("Modified file: " + _file)
    if _file.beginswith('files/'):
        print("Pre-existing file {} modified".format(_file))
        checks_passed = False
try:        
    f_added = open(fname_added, "r")
except:
    print("{} is not found!".format(fname_added))
    sys.exit(1)

addedfiles = []
if len(f_added.readlines()) > 0:
    for f in f_added.readlines():
        addedfiles += f.strip().split(',')
for _file in addedfiles:
    print("Added file: " + _file)

for _file in addedfiles:
    f = open('files/' + _file, "r")
    l = f.readlines()
    if len(l) == 1:
        print("Checks passed for file: " + _file)
        f.close()
    else:
        print("Checks failed for file: " + _file)
        f.close()
        checks_passed = False

if not checks_passed:
    sys.exit(1)
