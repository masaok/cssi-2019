import webapp2

# the handler section
class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!') #the response

class CecePage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<p>HELLO, CECE!!!!</p>')

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/cece', CecePage),
], debug=True)