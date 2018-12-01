#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import paho.mqtt.client as mqtt
import requests

HOSTNAME = 'api.beebotte.com'
PORT = 1883
TOKEN = os.getenv('TOKEN')
TOPIC = os.getenv('TOPIC')

AIR_URL = os.getenv('AIR_URL')
TV_URL = os.getenv('TV_URL')

def air(cmd):
	requests.post(AIR_URL, {'c': cmd})
	
def tv(cmd):
	requests.post(TV_URL, {'c': cmd})

def on_connect(self, client, data, rc):
	print('status {0}'.format(rc))
	self.subscribe(TOPIC, 1)

def on_message(client, data, msg):
	payload = str(msg.payload)
	print(msg.topic + ' ' + payload)
	if 'ON' in payload:
		print('ON')
		air('on')
	elif 'OFF' in payload:
		print('OFF')
		air('off')
	elif 'TV' in payload:
		print('TV')
		tv('power')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set('token:%s'%TOKEN)
client.connect(HOSTNAME, PORT, 60)

client.loop_forever()
