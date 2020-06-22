from builtins import object
import io
import csv
import re
from decimal import Decimal
from datetime import datetime


class renderer_plain_text(object):
    """
    *The plain_text renderer - can return content to browser or a file to download*
    """

    def __init__(self, info):
        pass

    def __call__(self, content, system):

        request = system.get('request')
        if request is not None:
            response = request.response
            ct = response.content_type
            if ct == response.default_content_type:
                response.content_type = 'text/plain'

        # setup the file if "download" is true
        if "filename" in request.params:
            now = datetime.now()
            now = now.strftime("%Y%m%dt%H%M%S")
            filename = request.params["filename"].replace(" ", "_")
            filename = """%(filename)s_%(now)s""" % locals()
            response.content_type = 'text/plain'
            response.content_disposition = "attachment; filename=%(filename)s" % locals(
            )

        # create a virutal file to write the content to
        output = io.StringIO(content)
        output = output.getvalue()
        output = output.strip()
        returnOutput = output

        return returnOutput
