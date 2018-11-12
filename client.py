from socket import socket, AF_INET, SOCK_DGRAM
import sys
if __name__ == '__main__':
    if len(sys.argv) > 1:
        server_ip = sys.argv[1]
        server_port = sys.argv[2]
        #s = socket(AF_INET, SOCK_DGRAM)

    s = socket(AF_INET, SOCK_DGRAM)
    # dest_ip = '127.0.0.1'
    # dest_port = 12345
    msg = raw_input()
    while not msg == 'quit':
        s.sendto(msg, (server_ip, int(server_port)))
        data, sender_info = s.recvfrom(2048)
        print  data
        msg = raw_input()
    s.close()



    # msg = raw_input("Message to send: ")
    # while not msg == 'quit':
    #     s.sendto(msg, ('127.0.0.1', int(server_port)))
    #     data, sender_info = s.recvfrom(2048)
    #     print  data
    # msg = raw_input("Message to send: ")
    # s.close()
