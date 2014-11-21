import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults, forbidden_view_config
from pyramid.security import remember, forget
from dryxPyramid.security import USERS
from dryxPyramid.templates.responses import templates_login

# RESOURCE CONTEXT


@view_defaults(route_name='login')
class login_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'login'' view")

    @view_config(route_name='login')
    @forbidden_view_config()
    def login(self):
        # Some Varibales
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        message = ''
        login = ''
        password = ''

        # never use the login form itself as came_from
        if login_url in referrer:
            referrer = '/'

        came_from = request.params.get('came_from', referrer)

        # test post method parameter to see if user can login
        if ('method' in request.params and request.params["method"] == "post") or request.method == "POST":
            login = request.params['login']
            password = request.params['password']
            if login not in USERS:
                message = 'incorrect username or password'
            else:
                if USERS.get(login) == password:
                    headers = remember(request, login)
                    return HTTPFound(location=came_from,
                                     headers=headers)
                else:
                    message = 'incorrect username or password'

        # If wrong details added, or GET method used, return login page
        loginPage = templates_login(
            log=self.log,
            request=request,
            mainCssFileName=self.request.registry.settings["main css filename"],
            jsFileName=self.request.registry.settings["main js filename"],
            pageTitle="Login",
            iconPath=self.request.registry.settings["path to webapp icon"],
            message=message,
            came_from=came_from
        )
        responseContent = loginPage.get()
        return Response(responseContent)
