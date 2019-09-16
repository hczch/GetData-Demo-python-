#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from socket import *

from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)  # 初始化

client.create_database('Zhc_db')  # 创建一个名为Shaw_and_Pegy_4+ 存储数据的新数据库

client.get_list_database()  # 客户端的功能检查数据库是否在那里

client.switch_database('Zhc_db')  # 将客户端设置为使用此数据库

result = client.query('select * from smart;')

print("Result: {0}".format(result))

host = ''  # 监听所有的ip

port = 13014  # 接口必须一致

bufsize = 1024

addr = (host, port)

udpServer = socket(AF_INET, SOCK_DGRAM)

udpServer.bind(addr)  # 开始监听

while True:

    print('Waiting for connection...')

    data, addr = udpServer.recvfrom(bufsize)  # 接收数据和返回地址

# 处理数据
# data  = data.decode(encoding='utf-8').upper()

# data = "at %s :%s"%(ctime(),data)

# udpServer.sendto(data.encode(encoding='utf-8'),addr)

# 发送数据

    print(data)

    a = float(data)

if a != 0 and a != 1:

    json_body = [

    {

        "measurement": "Temperature",

        "tags":
            {

                "user": " ",

                "brushId": "001"

            },

        # "time": "2018-03-28T8:01:00Z",

        "fields": {

            "DATA": a

        }
    }
]
    client.write_points(json_body)
else:
    json_body = [
    {
        "measurement": "Humidity",
        "tags": {
            "user": " ",
            "brushId": "001"
        },
        # "time": "2018-03-28T8:01:00Z",
        "fields": {
            "DATA": a
        }
    }
]
    client.write_points(json_body)

    udpServer.close()