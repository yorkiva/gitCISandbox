import sys, os

print("="*10 + "Running Repo Checker" + "="*10)
checks_passed = True
fname_added = "added.txt"
fname_mod = "modified.txt"

try:
    f_mod = open(fname_mod, "r")
except:
    print("{} is not found!".format(fname_mod))
    sys.exit(1)
    
modfiles = []
f_mod_lines = f_mod.readlines()
if len(f_mod_lines) > 0:
    for f in f_mod_lines:
        modfiles += f.strip().split(',')
for _file in modfiles:
    print("Modified file: " + _file)
    if _file.startswith('files/'):
        print("Pre-existing file {} modified".format(_file))
        checks_passed = False
f_mod.close()

try:        
    f_added = open(fname_added, "r")
except:
    print("{} is not found!".format(fname_added))
    sys.exit(1)

addedfiles = []
f_added_lines = f_added.readlines()
if len(f_added_lines) > 0:
    for f in f_added_lines:
        addedfiles += f.strip().split(',')
for _file in addedfiles:
    print("Added file: " + _file)
f_added.close()

for _file in addedfiles:
    f = open(_file, "r")
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
