#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-05-13 17:49:23
# @Author  : Sun Yan (suxiaobaisy@163.com)
# @Link    : https://github.com/suxiaobai
# @Version : $Id$

import os
import time
import paho.mqtt.client as mqtt

client_id = "baymax1@1NQ1E9"

client = mqtt.Client(client_id=client_id)
client.username_pw_set("mqtt", "YWMtIJDtIvEfEeu8fkf-kOMZXYRsAgdFB0jzldZaf0gApRFJUsnA65wR648SlZQt1taPAwMAAAF69unObgBPGgCNVACrGokw8DlJH8gP19D0s2uxPLBWux9weDkoyiiA2A")
client.connect("mqtt-ejabberd-hsb.easemob.com", 2883, 60)

print("event/" + str(time.time()))
client.publish("event/" + str(time.time()))
