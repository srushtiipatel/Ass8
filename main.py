# =====================
# IMPORTS
# =====================
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


# =====================
# HOME PAGE
# =====================
class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write("Home Page")


# =====================
# ADD FUNCTION
# =====================
class AddHandler(webapp.RequestHandler):
    def get(self):
        a = int(self.request.get('a', 0))
        b = int(self.request.get('b', 0))
        self.response.out.write("Sum = " + str(a + b))


# =====================
# ROUTING
# =====================
def main():
    application = webapp.WSGIApplication([
        ('/', MainHandler),
        ('/add', AddHandler)
    ], debug=True)

    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()