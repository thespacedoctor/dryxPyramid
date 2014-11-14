import io
import datetime
import decimal
from decimal import Decimal
from pyramid.renderers import JSON


class renderer_json(JSON):

    """
    The json renderer - can return content to browser or a file to download
    """

    def __init__(self, info):
        JSON.__init__(self, indent=4, sort_keys=True, separators=(',', ': '))

    def __call__(self, info, system):
        _render = JSON.__call__(self, info)

        # if table if empty
        if len(info):
            tableColumnNames = info[0].keys()

        self.add_adapter(datetime.datetime, self.datetime_adapter)
        self.add_adapter(decimal.Decimal, self.decimal_adapter)

        for row in info:
            for c in tableColumnNames:
                if isinstance(row[c], float) or isinstance(row[c], long) or isinstance(row[c], Decimal):
                    row[c] = float("%0.4f" % row[c])
                elif isinstance(row[c], datetime.datetime):
                    thisDate = str(row[c])[:10]
                    row[c] = "%(thisDate)s" % locals()

        # setup the file if "download" is true
        request = system.get('request')
        response = request.response
        if "filename" in request.params:
            now = datetime.datetime.now()
            now = now.strftime("%Y%m%dt%H%M%S")
            filename = request.params["filename"].replace(" ", "_")
            filename = """%(filename)s_%(now)s""" % locals()
            response.content_type = 'text/json'
            response.content_disposition = "attachment; filename=%(filename)s.json" % locals(
            )
        return _render(info, system)

    def datetime_adapter(self, obj, request):
        return obj.isoformat()

    def decimal_adapter(self, obj, request):
        return float(obj)
