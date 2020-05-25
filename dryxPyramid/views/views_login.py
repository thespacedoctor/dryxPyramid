from builtins import object
import logging
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults, forbidden_view_config
from pyramid.security import remember, forget
from passlib.hash import sha256_crypt
from dryxPyramid.security import get_users_and_groups
from dryxPyramid.templates.responses import templates_login

# RESOURCE CONTEXT


@forbidden_view_config()
def forbidden(request):
    login = login_view(request)
    login.referrer = "/"
    if request.method == "GET" or ("method" in request.params and request.params["method"] == "get"):
        login.message = "You do not have the correct permissions to view this page"
    else:
        login.message = "You do not have the correct permissions to perform this action"
    # href = request.route_path('login')
    return login.login()


@view_defaults(route_name='login', permission="view_everyone")
class login_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'login' view")
        self.USERS, self.GROUPS = get_users_and_groups(request)
        self.message = ""
        self.referrer = request.url

    @view_config(route_name='login', permission="view_everyone")
    def login(self):
        # Some Varibales
        request = self.request
        login_url = request.route_url('login')
        referrer = self.referrer
        message = self.message
        login = ''
        password = ''

        # never use the login form itself as came_from
        if login_url in referrer or "/" == referrer:
            href = request.route_path('index')
            referrer = href
        came_from = request.params.get('came_from', referrer)

        # test post method parameter to see if user can login
        if 'login' in request.params and (('method' in request.params and request.params["method"] == "post") or request.method == "POST"):
            login = request.params['login']
            login = login.replace("@pessto.org", "")
            password = request.params['password']
            if login not in self.USERS:
                message = 'incorrect username or password'
            else:
                if sha256_crypt.verify(password, self.USERS.get(login)):
                    headers = remember(request, login)
                    return HTTPFound(location=came_from,
                                     headers=headers)
                else:
                    message = 'incorrect username or password'

        # If wrong details added, or GET method used, return login page
        loginPage = templates_login(
            log=self.log,
            request=request,
            mainCssFilePath=self.request.registry.settings[
                "main css filepath"],
            jsFilePath=self.request.registry.settings["main js filepath"],
            pageTitle="Login",
            iconPath=self.request.registry.settings["path to webapp icon"],
            message=message,
            came_from=came_from
        )
        responseContent = loginPage.get()
        return Response(responseContent)
