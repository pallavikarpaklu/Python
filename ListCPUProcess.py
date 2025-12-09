import os
import sys

limit = 10

def list_processes(limit):
    list_cmd = "ps aux | sort -k3 -r | head -n " + limit
    processes = os.popen(list_cmd).read()
    print(processes)

if __name__ == '__main__':
    #First argument is filename
    #Second and more argument is variables to function

    if len(sys.argv) == 1:
        list_processes(str(limit)) # Passing default value
    elif len(sys.argv) == 2:
       limit = sys.argv[1]
       list_processes(limit) #Passing prompt value
    else:
        print("Invalid arguments. Instead run as 'python3 ListCPUProcess.py <number>' ")
        exit()
