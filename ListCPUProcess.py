import os
import sys

limit = 10


def list_processes(limit):
    ps_cmd = "ps aux "
    ps_result = os.popen(ps_cmd).read()
    lines = ps_result.split("\n")
    lines.pop(0)  # removing entry with labels (First record)
    process_list = []

    for line in lines:
        record = []
        word_list = list(filter(None, line.split(" ")))
        if len(word_list) > 3:
            record.append(word_list[0])  # processName
            record.append(int(word_list[1]))  # processId
            record.append(float(word_list[2]))  # CPU_PERC
            process_list.append(record)

    sorted_list = sorted(process_list, key=lambda x: x[2], reverse=True)  # sort by CPU_PERC

    for i in range(limit):
        rec = sorted_list[i]
        print("{0},{1},{2}".format(rec[0], rec[1], rec[2]))


if __name__ == '__main__':
    # First argument is filename
    # Second and more argument is variables to function

    if len(sys.argv) == 1:
        list_processes(limit)  # Passing default value
    elif len(sys.argv) == 2:
        limit = sys.argv[1]
        list_processes(int(limit))  # Passing prompt value
    else:
        print("Invalid arguments. Instead run as 'python3 ListCPUProcess.py <number>' ")
        exit()
