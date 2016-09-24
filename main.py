import logging
import os

import webapp2
import jinja2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(jenv.get_template('layout/index.html').render({}))


class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(jenv.get_template('layout/about.html').render({}))


class AlumniPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(jenv.get_template('layout/alumni.html').render({}))


class DonatePage(webapp2.RequestHandler):
    def get(self):
        self.response.write(jenv.get_template('layout/donate.html').render({}))


class ExecPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(jenv.get_template('layout/exec.html').render({}))


class JoinPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(jenv.get_template('layout/join.html').render({}))


class TournamentsPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(jenv.get_template('layout/tournaments.html').render({}))




jenv = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/index.html', MainPage),
    ('/about.html', AboutPage),
    ('/alumni.html', AlumniPage),
    ('/donate.html', DonatePage),
    ('/exec.html', ExecPage),
    ('/join.html', JoinPage),
    ('/tournaments.html', TournamentsPage),

])