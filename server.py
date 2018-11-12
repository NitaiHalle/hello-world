import sys
from socket import socket, AF_INET, SOCK_DGRAM
#todo need to check this func
def ask_parent(data, parent_ip, parent_port):
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(data, (parent_ip, int(parent_port)))
    ip_for_data, sender_info = s.recvfrom(2048)
    return ip_for_data


if __name__ == '__main__':

    if len(sys.argv) > 1:
        my_port = sys.argv[1]
        parent_ip = sys.argv[2]
        parent_port = sys.argv[3]
        ips_file_name = sys.argv[4]
    else:
        print "need more parameters to start this server"
    ips = {}
    with open(ips_file_name,'r') as file:
        lines = file.readlines()
    for line in lines:
        split_line = line.split(',')
        ips.update({split_line[0]:split_line[1]})
    print ips

    s = socket(AF_INET, SOCK_DGRAM)
    source_ip = '0.0.0.0'
    source_port = int(my_port)
    s.bind((source_ip, source_port))
    while True:
        data, sender_info = s.recvfrom(2048)
        if data in ips:
            s.sendto(ips[data],sender_info)
        else:
            new_ip = ask_parent(data, parent_ip, parent_port)
            # with open(ips_file_name,'w') as file:
            #     file.write('{},{}/n'.format(data,new_ip))
            f = open(ips_file_name, 'a')
            f.write('\n{},{}'.format(data,new_ip))
            f.close()
            ips.update({data:new_ip})
            s.sendto(ips[data], sender_info)
        # print "Message: ", data, " from: ", sender_info
        # s.sendto(data.upper(), sender_info)
###################################################
