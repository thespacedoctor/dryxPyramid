from builtins import object
import logging

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from ..templates.responses import templates_download

# RESOURCE CONTEXT


@view_defaults(route_name='download', permission="view_users")
class download_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.log.debug("instantiating a new 'download'' view")

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        import pyramid.httpexceptions as exc
        return exc.exception_response(405, body_template="The DELETE method is not allowed on the 'download'")

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        import pyramid.httpexceptions as exc
        return exc.exception_response(405, body_template="The PUT method is not allowed on 'download'")

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        import pyramid.httpexceptions as exc
        return exc.exception_response(405, body_template="The POST method is not allowed on 'download'")

    @view_config(request_method='GET', permission="view_users")
    @view_config(request_param="method=get", permission="view_users")
    def get(self):
        download = templates_download(
            log=self.log,
            request=self.request
        )
        return download.get()
