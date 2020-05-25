#!/usr/local/bin/python
# encoding: utf-8
"""
*The HTML template module for the `templates_login.py` resource*

:Author:
    David Young
"""
from builtins import object
import sys
import os
import khufu

class templates_login(object):
    """
    *The worker class for the templates_login module*

    **Key Arguments**

    - ``log`` -- logger
    - ``request`` -- the pyramid request
    - ``mainCssFilePath`` -- the filename of the main css file
    - ``jsFilePath`` -- the filename of the main js file
    - ``pageTitle`` -- pageTitle
    - ``icon`` -- webapp icon
    - ``came_from`` -- the url this login page was triggered from
    - ``message`` -- message to display as notification
    """
    # Initialisation

    def __init__(
        self,
        log,
        request,
        mainCssFilePath="main.css",
        jsFilePath="main-ck.js",
        pageTitle="Login",
        iconPath="",
        came_from="/",
        message=""
    ):
        self.log = log
        self.request = request
        self.mainCssFilePath = mainCssFilePath
        self.jsFilePath = jsFilePath
        self.pageTitle = pageTitle
        self.iconPath = iconPath
        self.came_from = came_from
        self.message = message

        # xt-self-arg-tmpx

        log.debug("instansiating a new 'templates_login' object")

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """
        *get the templates_login object*

        **Return**

        - ``loginPage`` -- the login page
        """
        self.log.debug('starting the ``get`` method')

        loginPage = khufu.scaffolding.login_page(
            log=self.log,
            mainCssFilePath=self.mainCssFilePath,
            jsFilePath=self.jsFilePath,
            pageTitle=self.pageTitle,
            iconPath=self.iconPath,
            came_from=self.came_from,
            message=self.message,
        )
        loginPage = loginPage.get()

        self.log.debug('completed the ``get`` method')
        return loginPage

    # xt-class-method
