#!/usr/local/bin/python
# encoding: utf-8
"""
*The base model for other model modules to build on top of*

:Author:
    David Young
"""

from builtins import object
import sys
import os


class base_model(object):
    """
    A superclass model for pyramid apps 

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``elementId`` -- the specific element id requests (or False)
        - ``search`` -- is the result given from a search query
    """

    def __init__(
        self,
        log,
        request,
        elementId=False,
        search=False
    ):
        self.log = log
        self.request = request
        self.elementId = elementId
        self.search = search
        self.qs = dict(request.params)  # the query string
        # the query string defaults
        self.defaultQs = {
            "format": None
        }
        self.sql = {}
        # self.resourceName = "basemodel"

        if isinstance(elementId, list):
            print("  asd")
            self.elementId = (",").join(str(elementId))
            print(self.elementId)

        return None

    def close(self):
        del self
        return None

    def _set_default_parameters(
            self):
        """set default parameters

        **Return:**
            - None
        """
        self.log.debug('starting the ``_set_default_parameters`` method')

        # refererRoute = self.request.referer.split(
        #     self.request.host)[1].split("?")[0]
        # requestRoute = self.request.url.split(
        #     self.request.host)[1].split("?")[0]

        defaultQs = {
            "format": None,
            "pageLimit": 100,
            "pageStart": 0,
            "sortBy": False,
            "sortDesc": False,
            "filterBy1": False,
            "filterValue1": False,
            "filterOp1": False,
            "filterBy2": False,
            "filterValue2": False,
            "filterOp2": False
        }

        # NOW OVERRIDE THESE DEFAULTS IF NEEDED
        for k, v in self.defaultQs.items():
            defaultQs[k] = v

        # ADD DEFAULTS TO THIS REQUEST - CLEAR OUR PARAMETERS COMING FROM A
        # NON-RELATED RESOURCE/ROUTE
        for k, v in defaultQs.items():
            if k not in self.qs.keys():
                self.qs[k] = v

        self.sql["where"] = " where 1=1 "
        self.sql["limit"] = ""

        if self.qs["pageLimit"]:
            self.sql["limit"] = "limit %(pageLimit)s" % self.qs

        self.log.debug('completed the ``_set_default_parameters`` method')
        return None

    # xt-class-method
