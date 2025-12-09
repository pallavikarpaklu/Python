import os

def list_processes():
    processes = os.popen(' ps aux | sort -k2 -r | head -n 100').read()
    print(processes)

if __name__ == '__main__':
    list_processes()
