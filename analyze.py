import pstats
import subprocess

with open("semifractal.py.log") as f:
    cmd = ['python', '-m', 'cProfile', 'semifractal.py']
    subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=f, shell=True)
with open("semifractal.py.log", "w") as f:
    lines = f.split('\n')
    lines = lines[1:]
    f.write('\n'.join(lines))
    

