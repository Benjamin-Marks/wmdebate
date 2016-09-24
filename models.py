"""Datastore modules for the debate website

TODO: documentation
"""

from google.appengine.ext import ndb

class Exec(ndb.Model):
	name = ndb.StringProperty()
	position = ndb.StringProperty()
	ranking = ndb.IntegerProperty(indexed=True)
	year = ndb.IntegerProperty()
	image = ndb.BlobProperty()
	description = ndb.StringProperty()


class Tournament(ndb.Model):
	name = ndb.StringProperty()
	ranking = ndb.IntegerProperty(indexed=True)

class Post(ndb.Model):
	# TODO: Think about how to structure this more
	content = ndb.StringProperty()

class Page(ndb.Model):
	#TODO: Think about how to structure these. Auto-created, undeletable?
	name = ndb.StringProperty()
	content = ndb.StringProperty()

class SliderImage(ndb.Model):
	image = ndb.BlobProperty()
	order = ndb.IntegerProperty(indexed=True)
