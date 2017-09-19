# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import random

from datastore_manager import DatastoreManager

FLIP_THRESH = 0.5

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Welcome to random generator!')


class CoinFlip(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('- - - Coin Flip - - -\n\n')
        
        id = self.request.path.split('/')[-1]
        
        datastore = DatastoreManager(id)
        
        flip = random.random() < FLIP_THRESH
        if flip:
        	self.response.write('HEADS!')
        else:
        	self.response.write('TAILS!')
        	
        self.response.write('\n\nHistory:\n')
        
        if datastore.has_id():
        	self.response.write('\tabc...\n')
        else:
        	self.response.write('\tno other flips yet :)\n')


app = webapp2.WSGIApplication([
    ('/', MainPage), ('/flip/.*', CoinFlip)
], debug=True)
