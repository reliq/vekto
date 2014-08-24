###
#	Vekto. by ReliQ
#	A simple chatango bot.
###


## Imports
import ch
import os
import random


## Vars
prefix 	= ";" 				# watch phrase / command prefix
botname	= "vekto";			# chatango username
botpass	= "";				# chatango password
rooms 	= ["z-spot", "watchanimenet"]


## Core
class lexBot(ch.RoomManager):

	def onConnect(self, room):
		print("- Connected to " + room.name)
		#room.message("I have connected")

	def onReconnect(self, room):
		print("- Reconnected to " + room.name)

	def onDisconnect(self, room):
		print("- Disconnected from " + room.name)

	def onFloodWarning(self, room):
		room.reconnect()

	def getAccess(self, user):
		if user.name.lower() == "vek7": return 1
		else: return 0

	def onMessage(self, room, user, message):
		
		# Grab each message and output
		print(user.name +": "+message.body)

		# Disect the message
		msg_data = message.body.split(" ", 1)
		if len(msg_data) > 1:
			cmd, args = msg_data[0], msg_data[1]
		else:
			cmd, args = msg_data[0], ""
		cmd = cmd.lower()

		# Test each message for prefix, 
		# if prefix is not present let it slide.
		if len(cmd) > 0:
			if cmd[0] == prefix:
				used_prefix = True
				cmd = cmd[1:]
			else:
				used_prefix = False
		else:
			return

		
		
		## The commands:

		# Say
		if used_prefix and cmd == "say":
			if args:
				room.message(args)
			else:
				print("Nothing to say...")				
		elif cmd[:2] == "v:":
			room.message(message.body[2:])
		# Announcements
		elif used_prefix and cmd == "anc" and len(args) > 0:
			if self.getAccess(user) == 1:
				for _room in self.rooms:
					_room.message("Announcement from "+user.name.capitalize()+": "+args)
			else:
				room.message("No permissions!")
		# What room
		elif cmd=="whatroom":
			room.message("<b>%s</b> this is <b>http://%s.chatango.com</b>" % (user.name, room.name), True)
		# Bye 
		elif used_prefix and cmd == "bye":
				room.message("awww bye " + user.name + " =(")




if __name__ == "__main__":
	os.system("clear")
	print("; "+botname+" ====")
	lexBot.easy_start(rooms, botname, botpass)
