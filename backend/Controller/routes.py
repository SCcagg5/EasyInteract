from .routesfunc import *

def setuproute(app, call):
    @app.route('/',                 ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])                       )
    @app.route('/login/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([login])                  )
    @app.route('/add/model/',    	['OPTIONS', 'POST'],        lambda x = None: call([verify, addmodel])       )
    @app.route('/ask/money/',    	['OPTIONS', 'POST'],        lambda x = None: call([verify, askmoney])       )
    def base():
        return
