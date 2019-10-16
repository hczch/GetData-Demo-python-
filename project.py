#!/usr/bin/env python3

# -*- coding: UTF-8 -*-

from socket import *

from influxdb import  InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)  # 初始化

client.create_database('Zhc_db')

client.get_list_database()  # 客户端的功能检查数据库是否在那里

client.switch_database('Zhc_db')  # 将客户端设置为使用此数据库

result = client.query('select * from smart;')

print("Result: {0}".format(result))

host = ''  # 监听所有的ip

port = 12000  # 接口必须一致

bufsize = 1024

addr = (host, port)

udpServer = socket(AF_INET, SOCK_DGRAM)

udpServer.bind(addr)  # 开始监听

while True:

    print('Waiting for connection...')
   
    data, addr = udpServer.recvfrom(bufsize)  # 接收数据和返回地址
    print(addr)
    # 处理数据

    # data  = data.decode(encoding='utf-8').upper()

    # data = "at %s :%s"%(ctime(),data)

    # udpServer.sendto(data.encode(encoding='utf-8'),addr)

    # 发送数据

    if not data:

       continue

    else:

       print(data)
    
       temperature = float(data[0:3])

       humidity = float(data[4:7])

       print(temperature)

       print(humidity)

       json_body = [

            {

                "measurement": "Temperature",

                "tags":

                    {

                        "user": "温度"

                        #  "brushId": "001"

                    },

                # "time": "2018-03-28T8:01:00Z",

                "fields": {

                    "DATA": temperature

                }

            }

        ]

       client.write_points(json_body)

       json_body = [

            {

                "measurement": "Humidity",

                "tags": {

                    "user": "湿度"

                    # "brushId": "001"

                },

                # "time": "2018-03-28T8:01:00Z",

                "fields": {

                    "DATA": humidity

                }

            }

        ]

       client.write_points(json_body)

       udpServer.close()
