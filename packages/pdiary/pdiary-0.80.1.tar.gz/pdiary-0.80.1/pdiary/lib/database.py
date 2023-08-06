#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2018 Valter Nazianzeno <manipuladordedados at gmail dot com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import peewee
from playhouse.sqlcipher_ext import SqlCipherDatabase

# Default directory for config files and db file
CONFIG_DIR_PATH = os.path.expanduser("~")+"/.config/pdiary/"
DB_FILE = CONFIG_DIR_PATH+"data.db"

db = SqlCipherDatabase(None)

# Main table
class Entry(peewee.Model):
    title = peewee.CharField()
    date = peewee.CharField()
    content = peewee.CharField()

    class Meta:
        database = db

class dbManager(object):
    def __init__(self, password):
        # Create the config folder if it doesn't already exists
        if not os.path.exists(CONFIG_DIR_PATH):
            os.mkdir(CONFIG_DIR_PATH)
        db.init(DB_FILE, passphrase=password, kdf_iter=64000)
        db.create_tables([Entry])

    def add(self, t, d, c):
        Entry.create(title=t, date=d, content=c)

    def view(self, _id):
        # Create a list with each item's ids, the content stored in the database
        # is based on the position of these ids.
        ids = [pk.id for pk in Entry.select(Entry.id)]
        query = Entry.select().where(Entry.id == ids[_id])
        for q in query:
            return q.id, q.title, q.date, q.content

    def list_entries(self):
        entries_list = []
        for entry in Entry.select(Entry.title, Entry.date):
            entries_list.append(entry.date + " "*5 + entry.title)
        return entries_list

    def edit(self, _id, title, date, content):
        entry = Entry.get(Entry.id == self.view(_id)[0])
        entry.title = title
        entry.date = date
        entry.content = content
        entry.save()

    def remove(self, _id):
        entry = Entry.get(Entry.id == self.view(_id)[0])
        entry.delete_instance()
