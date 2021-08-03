#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-05-13 17:49:23
# @Author  : Sun Yan (suxiaobaisy@163.com)
# @Link    : https://github.com/suxiaobai
# @Version : $Id$

import os
import sys
import time
import paho.mqtt.client as mqtt


#### 发送消息
client_id = "baymax1@1NQ1E9"

client = mqtt.Client(client_id=client_id)
client.username_pw_set("mqtt", "YWMtIJDtIvEfEeu8fkf-kOMZXYRsAgdFB0jzldZaf0gApRFJUsnA65wR648SlZQt1taPAwMAAAF69unObgBPGgCNVACrGokw8DlJH8gP19D0s2uxPLBWux9weDkoyiiA2A")
client.connect("mqtt-ejabberd-hsb.easemob.com", 2883, 60)

client.publish("event/" + str(time.time()))




#### 接受消息

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("event/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    mess = (msg.topic+" ")
    print(msg.topic)
    send_time = mess.split("/")[1]
    recive_time = time.time()
    if float(recive_time) - float(send_time) <= 2:
        sys.exit(0)
    else:
        sys.exit(1)

client_id = "baymax2@1NQ1E9"
client = mqtt.Client(client_id=client_id)
client.username_pw_set("mqtt1", "YWMtEkxG-PEfEeujKc-Es2W3rIRsAgdFB0jzldZaf0gApRFNZ2eg65wR642PfWIAvzocAwMAAAF69ulw7ABPGgAho1eIkgBBjgaUeKF34rafUFcK-nSO2kf9nnRJjFvX9A")
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt-ejabberd-hsb.easemob.com", 2883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()