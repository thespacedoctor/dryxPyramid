import logging
import pyramid.httpexceptions as exc
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from ..templates.responses import templates_downloads

# RESOURCE CONTEXT


@view_defaults(route_name='downloads')
class downloads_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'downloads'' view")

    @view_config(request_method='DELETE')
    @view_config(request_param="method=delete")
    def delete(self):
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'downloads'")

    @view_config(request_method='PUT')
    @view_config(request_param="method=put")
    def put(self):
        return exc.exception_response(405, body_template="The PUT method is not allowed on 'downloads'")

    @view_config(request_method='POST')
    @view_config(request_param="method=post")
    def post(self):
        return exc.exception_response(405, body_template="The POST method is not allowed on 'downloads'")

    @view_config(request_method='GET')
    @view_config(request_param="method=get")
    def get(self):
        downloads = templates_downloads(
            log=self.log,
            request=self.request
        )
        return downloads.get()
