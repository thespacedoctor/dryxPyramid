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
    @review: when complete review and cleanup this `templates_login.py` module
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import khufu
# from ...models.login import models_login_get
# from ...models.login.element import models_login_element_get


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

    **Todo**
        - @review: when complete, clean templates_login class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
        self,
        log,
        request,
        mainCssFileName="main.css",
        jsFileName="main-ck.js",
        pageTitle="Login",
        iconPath=""
    ):
        self.log = log
        self.request = request
        self.mainCssFileName = mainCssFileName
        self.jsFileName = jsFileName
        self.pageTitle = pageTitle
        self.iconPath = iconPath

        # xt-self-arg-tmpx

        log.debug("instansiating a new 'templates_login' object")

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the templates_login object

        **Return:**
            - ``responseContent`` -- the response

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        templates_login = None

        loginPage = khufu.scaffolding.login_page(
            log=self.log,
            mainCssFileName=self.mainCssFileName,
            jsFileName=self.jsFileName,
            pageTitle=self.pageTitle,
            iconPath=self.iconPath
        )
        loginPage = loginPage.get()

        self.log.info('completed the ``get`` method')
        return loginPage
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx
