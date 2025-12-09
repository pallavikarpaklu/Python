import os

def list_processes():
    processes = os.popen(' ps aux | head -n 10').read()
    print(processes)

if __name__ == '__main__':
    list_processes()
