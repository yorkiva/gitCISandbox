import sys, os

f_chkd = "CheckedFiles.txt"
this_f = open(f_chkd, "w")

_files = os.listdir('files')
checks_passed = True

for _file in _files:
    f = open('files/' + _file, "r")
    l = f.readlines()
    if len(l) == 1:
        print("Checks passed for file: " + _file)
        this_f.write(_file + '\n')
        f.close()
    else:
        print("Checks failed for file: " + _file)
        f.close()
        checks_passed = False

this_f.close()

if not checks_passed:
    sys.exit(1)
