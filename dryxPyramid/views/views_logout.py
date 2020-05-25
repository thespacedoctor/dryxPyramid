# @review clean me

import logging
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults, forbidden_view_config
from pyramid.security import remember, forget

# RESOURCE CONTEXT


@view_config(route_name='logout',  permission="view_everyone")
def logout(request):
    referrer = request.url
    logout_url = request.route_url('logout')
    # never use the logout as came_from
    if logout_url in referrer:
        referrer = 'index'

    came_from = request.params.get('came_from', referrer)
    headers = forget(request)
    return HTTPFound(location=request.route_url(came_from),
                     headers=headers)
