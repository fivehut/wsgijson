import simplejson
from webob import Response
from webob.dec import wsgify


class JsonResponse(Response):
    def __init__(self, r):
        Response.__init__(self,
                          content_type='application/json',
                          body=simplejson.dumps(r))


class JsonService(object):
    ''' sub-classes should implement call method '''
    @wsgify
    def __call__(self, req):
        return JsonResponse(self.call(simplejson.loads(req.body)))
