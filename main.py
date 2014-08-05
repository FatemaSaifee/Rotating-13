#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2

cipher_form="""
<form method="post">
    Enter some text to ROT13:
    <br>
    <textarea name="text" style="height: 100px; width: 400px;">%(text)s</textarea>
    <br>
    <input type="submit" name="rot">
    
</form>
"""

def rot13(text):
    output=''
    for i in text:
        for c in i:
            if ord(c)<=ord('z') and ord(c)>=ord('a'):
                for i in range(13):
                    if ord(c)==ord('z'):
                        c='a'
                    else:
                        c=chr(ord(c)+1)
                    
            elif ord(c)<=ord('Z') and ord(c)>=ord('A'):
                for i in range(13):
                    if ord(c)==ord('Z'):
                        c='A'
                    else:
                        c=chr(ord(c)+1)
            output=output+c
    return output

class MainHandler(webapp2.RequestHandler):
    def cipher_form(self, text=""):
        self.response.out.write(cipher_form % {"text": text})

    
    def get(self):
        self.cipher_form()
        #self.write_form()    

    def post(self):
        result = ''
        res = self.request.get("text")
        result = rot13(res)
        
        self.cipher_form(result)




class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks! That's a totally valid day! :D ")
    
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler)    
], debug=True)
