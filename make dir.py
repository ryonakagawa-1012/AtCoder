import subprocess
import shutil


def Process(cmd):
    return (subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]).decode('utf-8')


cmd = 'ls ABC'

process = Process(cmd)

dir_lst = list(map(int, process.split()))

mk_dir = max(dir_lst) + 1

subprocess.call(f"mkdir ABC/{mk_dir}", shell=True)

new_file_names = ["A.py", "B.py", "C.py", "D.py"]

for new_file_name in new_file_names:
    shutil.copy2('template.py', f'ABC/{mk_dir}/{new_file_name}')
