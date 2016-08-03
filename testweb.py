import web

render = web.template.render('')

urls = ( '/', 'index')

class index:
        def GET(self):
                i = web.input(name=None)
                return render.testindex(i.name)

if __name__ == "__main__":
        app = web.application(urls, globals())
        app.run()
