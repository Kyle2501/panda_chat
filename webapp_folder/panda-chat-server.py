#!/usr/bin/env python





  # - System
import os
import cgi
import urllib
import wsgiref.handlers
import datetime
import json, ast
import sys,imp
  # - Appengine
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.api import images
from urlparse import urlparse
  # -
from google.appengine.ext import ndb
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp.util import run_wsgi_app





class publicSite(webapp2.RequestHandler):
    def get(self):
      # - URL Parse
        page_address = self.request.uri
        uri = urlparse(page_address)
        path = uri[2] # - uri.path
        layers = path.split('/')
        path_layer = layers[1]
        base = os.path.basename(page_address)
      # - user
        user = users.get_current_user()
        if users.get_current_user(): # - logged in
          login_key = users.create_logout_url(self.request.uri)
          gate = 'Sign out'
          user_name = user.nickname()
        else: # - logged out
          login_key = users.create_login_url(self.request.uri)
          gate = 'Sign in'
          user_name = 'No User'
      # - app data
      
        html_file = 'main_layout.html'

      # - template
        objects = {

            'login_key': login_key,
            'gate': gate,
            'user_name': user_name,
        

        }
      # - render
        path = os.path.join(os.path.dirname(__file__), 'html_files/%s' %html_file)
        self.response.out.write(template.render(path, objects))



app = webapp2.WSGIApplication([    # - Pages
    ('/', publicSite),

    

], debug=True)


