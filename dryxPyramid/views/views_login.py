import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults, forbidden_view_config
from pyramid.security import remember, forget
from dryxPyramid.security import USERS
from ..templates.responses import templates_login
# from ..models.login import models_login_post, models_login_put

# RESOURCE CONTEXT


@view_defaults(route_name='login')
class login_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'login'' view")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'login' resource")

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        login = models_login_put(
            log=self.log,
            request=self.request
        )
        responseContent = login.put()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        login = models_login_post(
            log=self.log,
            request=self.request
        )
        responseContent = login.post()
        if "redirectURL" in self.request.params:
            url = self.request.params["redirectURL"]
            return HTTPFound(location=url)
        else:
            return Response(responseContent)

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
    def get(self):
        login = templates_login(
            log=self.log,
            request=self.request,
            mainCssFileName="main_marshall.css",
            jsFileName="main-ck.js",
            pageTitle="Marshall Login",
            iconPath="/static/images/pessto_icon.png"
        )
        responseContent = login.get()
        return Response(responseContent)
