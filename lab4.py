#!/usr/bin/python3
import os
import sys
from time import sleep

forks = int(sys.argv[1])
iterations = int(sys.argv[2])
message = sys.argv[3]
    
child_pids = []
bash = os.getppid()

for i in range(1, forks + 1):
    pid = os.fork()
    if (pid == 0):
        for j in range(iterations * i):
            if(os.getppid() == bash): exit(-1)
            print(f'fork_id = {i}', f'iter_id = {j}', f'msg = {message}', sep='\t')
            sleep(1)
        exit(0)
    else:
        child_pids.append(pid)
        
for pid in child_pids:
    os.waitpid(pid, 0)
