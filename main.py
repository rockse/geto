import web

urls = (
  '/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"