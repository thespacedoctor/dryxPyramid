from builtins import str
from builtins import range
from builtins import object
import csv
import io
import re
from decimal import Decimal
from datetime import datetime


class renderer_csv(object):
    """
    *The CSV renderer - can return plain text in browser or a file to download*
    """

    def __init__(self, info):
        pass

    def __call__(self, rows, system):
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
            response.content_type = 'text/csv'
            response.content_disposition = "attachment; filename=%(filename)s.csv" % locals(
            )

        # if table if empty
        if len(rows) == 0:
            return "no data returned"

        # Column Headers and widths
        header = []
        allRows = []
        tableColumnNames = list(rows[0].keys())
        columnWidths = []
        columnWidths[:] = [len(tableColumnNames[i])
                           for i in range(len(tableColumnNames))]

        # create a virutal file to write the content to
        output = io.StringIO()
        writer = csv.writer(
            output, dialect='excel', delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # clean up data
        for row in rows:
            for c in tableColumnNames:
                if isinstance(row[c], float) or isinstance(row[c], Decimal):
                    row[c] = "%0.4f" % row[c]
                elif isinstance(row[c], datetime):
                    thisDate = str(row[c])[:10]
                    row[c] = "%(thisDate)s" % locals()

        # set the column widths
        for row in rows:
            for i, c in enumerate(tableColumnNames):
                if len(str(row[c])) > columnWidths[i]:
                    columnWidths[i] = len(str(row[c]))

        # fill in the data
        for row in rows:
            thisRow = []
            for i, c in enumerate(tableColumnNames):
                thisRow.append(row[c])
            allRows.append(thisRow)

        # write the headers
        for i, c in enumerate(tableColumnNames):
            header.append(c)
        writer.writerow(header)

        # write out the data
        writer.writerows(allRows)
        output = output.getvalue()

        output = output.strip()
        returnOutput = output

        return returnOutput
