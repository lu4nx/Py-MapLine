# coding=utf-8

import socket

socket.timeout = 10


def host2ip(host):
    return socket.gethostbyname(host)


def foreach(host):
    host = host.strip()
    try:
        print("%s\t%s" % (host, host2ip(host)))
    except Exception as err:
        print(err)


if __name__ == '__main__':
    # test self
    print(host2ip("www.qq.com"))
