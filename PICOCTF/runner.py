import sys, subprocess


DETACHED_PROCESS = 0x00000008
for x in xrange(0,256):  
    pid = subprocess.Popen(['cmd.exe', "xor encrypt encrypted out"+str(x)+".txt "+bin(x)],
                       creationflags=DETACHED_PROCESS)
stderr = pid.communicate('C:\\Users\\pc1\\Documents\\GitHub\\Python\\PICOCTF')
