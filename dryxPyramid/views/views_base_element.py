from builtins import object
import logging
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults


@view_defaults(route_name='base_element_view',  permission="view_users")
class base_element_view(object):

    def __init__(self, request):
        self.request = request
        self.log = logging.getLogger(__name__)
        self.resourceName = "baseview"

    @view_config(request_method='DELETE', permission="edit_users")
    @view_config(request_param="method=delete", permission="edit_users")
    def delete(self):
        import pyramid.httpexceptions as exc
        resourceName = self.resourceName
        return exc.exception_response(404, body_template="The DELETE method is not enabled on the '%(resourceName)s' element resource" % locals())

    @view_config(request_method='PUT', permission="edit_users")
    @view_config(request_param="method=put", permission="edit_users")
    def put(self):
        import pyramid.httpexceptions as exc
        resourceName = self.resourceName
        return exc.exception_response(404, body_template="The PUT method is not enabled on the '%(resourceName)s' element resource" % locals())

    @view_config(request_method='POST', permission="edit_users")
    @view_config(request_param="method=post", permission="edit_users")
    def post(self):
        import pyramid.httpexceptions as exc
        resourceName = self.resourceName
        return exc.exception_response(404, body_template="The POST is not allowed on the '%(resourceName)s' element resource" % locals())

    @view_config(request_method='GET',  renderer="json", permission="view_users")
    @view_config(request_param="method=get",  renderer="json", permission="view_users")
    def get(self):
        import pyramid.httpexceptions as exc
        resourceName = self.resourceName
        return exc.exception_response(404, body_template="The GET method is not enabled to return JSON on the '%(resourceName)s' resource" % locals())

    @view_config(request_method='GET', request_param="format=json", renderer="json", permission="view_users")
    @view_config(request_param=["method=get", "format=json"], renderer="json", permission="view_users")
    def get_json(self):
        import pyramid.httpexceptions as exc
        resourceName = self.resourceName
        return exc.exception_response(404, body_template="The GET method is not enabled to return JSON on the '%(resourceName)s' resource" % locals())

    @view_config(request_method='GET', request_param="format=csv", renderer="csv", permission="view_users")
    @view_config(request_param=["method=get", "format=csv"], renderer="csv", permission="view_users")
    def get_csv(self):
        import pyramid.httpexceptions as exc
        resourceName = self.resourceName
        return exc.exception_response(404, body_template="The GET method is not enabled to return CSV on the '%(resourceName)s' resource" % locals())

    @view_config(request_method='GET', request_param="format=plain_table", renderer="plain_table", permission="view_users")
    @view_config(request_param=["method=get", "format=plain_table"], renderer="plain_table", permission="view_users")
    def get_plain_table(self):
        import pyramid.httpexceptions as exc
        resourceName = self.resourceName
        return exc.exception_response(404, body_template="The GET method is not enabled to return ascii tables on the '%(resourceName)s' resource" % locals())

    @view_config(request_method='GET', request_param="format=html")
    @view_config(request_param=["method=get", "format=html"])
    def get_html(self):
        import pyramid.httpexceptions as exc
        resourceName = self.resourceName
        return exc.exception_response(404, body_template="The GET method is not enabled to return HTML on the '%(resourceName)s' resource" % locals())
