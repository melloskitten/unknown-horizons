# ###################################################
# Copyright (C) 2008 The OpenAnno Team
# team@openanno.org
# This file is part of OpenAnno.
#
# OpenAnno is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################

import game.main
class BuySellWidget(object):

	def __init__(self, slots):
		self.slots = {}
		self.widget = game.main.fife.pychan.loadXML('content/gui/buysellmenu/buysellmenu.xml')
		self.widget.position=(200,200)
		self.add_slots(slots)
		self.add_ressource(4, 1)

	def hide(self):
		self.widget.hide()

	def show(self):
		self.widget.show()


	def add_slots(self, num):
		"""Adds num amount of slots to the buysellmenu.
		@param num: amount of slots that are to be added."""
		content = self.widget.findChild(name="content")
		assert(content is not None)
		for num in range(0,num):
			slot = game.main.fife.pychan.loadXML('content/gui/buysellmenu/single_slot.xml')
			self.slots[num] = slot
			slot.name = num
			content.addChild(slot)
		self.widget._recursiveResizeToContent()

	def add_ressource(self, res_id, slot):
		icon = self.slots[slot].findChild(name="icon")
		icon.image = game.main.db("SELECT icon FROM resource WHERE rowid=?", res_id)[0][0]
		self.slots[slot].findChild(name="amount").text = "0t"
