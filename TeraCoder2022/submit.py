from subprocess import run

lst = list("ABCDEFGHI")

for LST in lst:
    print(LST)
    run("touch {0}_submit.txt".format(LST), shell=True)
    run("{0}.txt < python {0}.py > {0}_submit.txt".format(LST, LST, LST), shell=True)
