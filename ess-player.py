#!/bin/env python
# -*- coding: utf-8 -*-

# Set default encoding to UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import json
import config
import os
import time

class ESSPlayer():

	def __init__(self):
		values = { 'name': config.NAME,'description': config.DESCRIPTION }
		req = urllib2.Request('%s/player' % config.SERVER)
		req.add_data(json.dumps(values))
		req.add_header('Content-Type', 'application/json')
		u = urllib2.urlopen(req)
		u.close()

	def get_current(self):
		req = urllib2.Request('%s/playlist/%s/current' % (
			config.SERVER, config.NAME))
		req.add_header('Accept', 'application/json')
		u = urllib2.urlopen(req)
		song = json.loads(u.read())
		u.close()
		return song.get('id')

	def play(self, sid):
		os.system('mplayer %s/song/%s' % (config.SERVER, sid))


	def run(self):
		while True:
			sid = self.get_current()
			if sid is None:
				time.sleep(1)
			else:
				self.play(sid)

if __name__ == '__main__':
	ESSPlayer().run()
