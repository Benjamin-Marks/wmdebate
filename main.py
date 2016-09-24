import logging
import os

import webapp2
import jinja2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write(jenv.get_template('layout/index.html').render({}))




jenv = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/index.html', MainPage)
])