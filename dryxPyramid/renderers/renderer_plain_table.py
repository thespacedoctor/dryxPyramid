from builtins import str
from builtins import range
from builtins import object
import io
import csv
import re
from decimal import Decimal
from datetime import datetime

class renderer_plain_table(object):
    """
    *The plain_table renderer - can return content to browser or a file to download*
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
            response.content_type = 'text/plain'
            response.content_disposition = "attachment; filename=%(filename)s" % locals(
            )

        # if table if empty
        if len(rows) == 0:
            return "no data returned"

        # setup variables
        header = []
        divider = []
        allRows = []
        tableColumnNames = list(rows[0].keys())
        columnWidths = []
        columnWidths[:] = [len(tableColumnNames[i])
                           for i in range(len(tableColumnNames))]

        # create a virutal file to write the content to
        output = io.BytesIO()

        # setup csv styles
        delimiter = "|"
        writer = csv.writer(output, dialect='excel', delimiter=delimiter,
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        dividerWriter = csv.writer(output, dialect='excel', delimiter="+",
                                   quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # clean up data
        for row in rows:
            for c in tableColumnNames:
                if isinstance(row[c], float) or isinstance(row[c], int) or isinstance(row[c], Decimal):
                    row[c] = "%0.2f" % row[c]
                elif isinstance(row[c], datetime):
                    thisDate = str(row[c])[:10]
                    row[c] = "%(thisDate)s" % locals()

        # set the column widths
        for row in rows:
            for i, c in enumerate(tableColumnNames):
                if len(str(row[c])) > columnWidths[i]:
                    columnWidths[i] = len(str(row[c]))

        # create the output content
        # fill in the data
        for row in rows:
            thisRow = []
            thisRow.append("")
            for i, c in enumerate(tableColumnNames):
                row[c] = str(str(row[c]).ljust(columnWidths[i] + 2)
                             .rjust(columnWidths[i] + 3))
                thisRow.append(row[c])
            thisRow.append("")
            allRows.append(thisRow)

        # table borders for human readable
        header.append("")
        divider.append("")

        for i, c in enumerate(tableColumnNames):
            header.append(
                c.ljust(columnWidths[i] + 2).rjust(columnWidths[i] + 3))
            divider.append('-' * (columnWidths[i] + 3))

        # table border for human readable
        header.append("")
        divider.append("")
        dividerWriter.writerow(divider)
        writer.writerow(header)
        dividerWriter.writerow(divider)

        # write out the data
        writer.writerows(allRows)
        # table border for human readable
        dividerWriter.writerow(divider)

        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        output = output.getvalue()
        output = """exported on %(now)s\n%(output)s""" % locals(
        )

        output = output.strip()
        returnOutput = output

        return returnOutput
