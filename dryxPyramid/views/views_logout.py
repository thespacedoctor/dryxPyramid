import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults, forbidden_view_config
from pyramid.security import remember, forget
from dryxPyramid.security import USERS
from ..templates.responses import templates_logout
# from ..models.logout import models_logout_post, models_logout_put

# RESOURCE CONTEXT


@view_defaults(route_name='logout')
class logout_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'logout'' view")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'logout' resource")

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        logout = models_logout_put(
            log=self.log,
            request=self.request
        )
        responseContent = logout.put()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        logout = models_logout_post(
            log=self.log,
            request=self.request
        )
        responseContent = logout.post()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
    def get(self):
        logout = templates_logout(
            log=self.log,
            request=self.request
        )
        responseContent = logout.get()
        return Response(responseContent)
