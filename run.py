#!/usr/bin/env python3

###########################################
#
# Requirements
#
# A file named 'credentials' needs to exist with the API key, username and
# password. See credentials.sample
#

import insteon
import configparser
config = configparser.ConfigParser()
config.read('credentials')
username = config['credentials']['user']
password = config['credentials']['pass']
apikey = config['credentials']['key']

i = insteon.Insteon(username, password, apikey)

#for o in i.devices:
#    print(o.DeviceName)
#    print(o.DeviceID)

#print(i.devices[15].DeviceName)
#i.devices[15].send_command('on')

#print(i.devices[15].DeviceName)
#print(i.devices[15].HouseID)

#print(i.scenes[3].SceneName)
#print(i.scenes[3].DeviceList)

#for o in i.scenes:
#    print(o.SceneName)
#    print(o.DeviceList)


#print(i.scenes[3].SceneName)
#i.scenes[3].SceneName='TESTING'
#print(i.scenes[3].SceneName)

#i.scenes[3].save
#i.scenes[3].reload_details

#print(i.scenes[3].SceneName)

#print(i.devices[15].DeviceName)
#i.devices[15].DeviceName='testdevice'
#print(i.devices[15].DeviceName)
#i.devices[15].save

#for o in i.rooms:
#print(i.rooms[1].RoomName)
#i.rooms[1].RoomName='testroomname2'
#print(i.rooms[1].RoomName)
#i.rooms[1].save

#i.room.RoomName="TestRoom"
#print(i.devices[15].DeviceName)
#i.devices[15].DeviceName='testdevice'
#print(i.devices[15].DeviceName)


#print(i.devices[1].DeviceName)
#i.devices[1].DeviceName='testdevice1'
#print(i.devices[1].DeviceName)
#i.devices[1].save()
