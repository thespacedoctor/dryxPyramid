#!/usr/local/bin/python
# encoding: utf-8
"""
templates_login.py
==================
:Summary:
    The HTML template module for the `templates_login.py` resource

:Author:
    David Young

:Date Created:
    November 20, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu


class templates_login():

    """
    The worker class for the templates_login module

    **Key Arguments:**
        - ``log`` -- logger
        - ``request`` -- the pyramid request
        - ``mainCssFileName`` -- the filename of the main css file
        - ``jsFileName`` -- the filename of the main js file
        - ``pageTitle`` -- pageTitle
        - ``icon`` -- webapp icon
        - ``came_from`` -- the url this login page was triggered from
        - ``message`` -- message to display as notification

    **Todo**
    """
    # Initialisation

    def __init__(
        self,
        log,
        request,
        mainCssFilePath="main.css",
        jsFileName="main-ck.js",
        pageTitle="Login",
        iconPath="",
        came_from="/",
        message=""
    ):
        self.log = log
        self.request = request
        self.mainCssFilePath = mainCssFilePath
        self.jsFileName = jsFileName
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
        """get the templates_login object

        **Return:**
            - ``loginPage`` -- the login page

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        loginPage = khufu.scaffolding.login_page(
            log=self.log,
            mainCssFilePath=self.mainCssFilePath,
            jsFileName=self.jsFileName,
            pageTitle=self.pageTitle,
            iconPath=self.iconPath,
            came_from=self.came_from,
            message=self.message,
        )
        loginPage = loginPage.get()

        self.log.info('completed the ``get`` method')
        return loginPage

    # xt-class-method
