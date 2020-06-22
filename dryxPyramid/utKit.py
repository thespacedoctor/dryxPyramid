"""
*Unit testing tools*
"""
import os
import shutil
import unittest
import yaml
from pyramid import testing
from pyramid.path import AssetResolver
from pyramid.request import apply_request_extensions
from paste.deploy.loadwsgi import appconfig
import pymysql as ms
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from fundamentals import utKit

# OVERRIDES


class utKit(utKit):
    """
    *Override dryx utKit*
    """
    # Variable Data Atrributes

    # Override Variable Data Atrributes
    # Initialisation
    def __init__(
            self,
            moduleDirectory,
            dbConn=False
    ):
        self.moduleDirectory = moduleDirectory
        # x-self-arg-tmpx

        # SETUP PATHS TO COMMON DIRECTORIES FOR TEST DATA
        self.pathToInputDir = moduleDirectory + "/input/"
        self.pathToOutputDir = moduleDirectory + "/output/"

        # SETUP LOGGING
        self.loggerConfig = """
        version: 1
        formatters:
            file_style:
                format: '* %(asctime)s - %(name)s - %(levelname)s (%(filename)s > %(funcName)s > %(lineno)d) - %(message)s  '
                datefmt: '%Y/%m/%d %H:%M:%S'
            console_style:
                format: '* %(asctime)s - %(levelname)s: %(filename)s:%(funcName)s:%(lineno)d > %(message)s'
                datefmt: '%H:%M:%S'
            html_style:
                format: '<div id="row" class="%(levelname)s"><span class="date">%(asctime)s</span>   <span class="label">file:</span><span class="filename">%(filename)s</span>   <span class="label">method:</span><span class="funcName">%(funcName)s</span>   <span class="label">line#:</span><span class="lineno">%(lineno)d</span> <span class="pathname">%(pathname)s</span>  <div class="right"><span class="message">%(message)s</span><span class="levelname">%(levelname)s</span></div></div>'
                datefmt: '%Y-%m-%d <span class= "time">%H:%M <span class= "seconds">%Ss</span></span>'
        handlers:
            console:
                class: logging.StreamHandler
                level: DEBUG
                formatter: console_style
                stream: ext://sys.stdout
        root:
            level: DEBUG
            handlers: [console]"""

        # Override Variable Data Atrributes
        self.dbConfig = False
        if dbConn:
            self.dbConfig = """
            version: 1
            db: unit_tests
            host: localhost
            user: utuser
            password: utpass
            """

        return

    def get_project_root(self):
        """
        *Get the root of the `python` package - useful for getting files in the root directory of a project*

        **Return**

        - ``rootPath`` -- the root path of a project

        """
        import os
        rootPath = os.path.dirname(__file__)

        return rootPath

    def refresh_database(self):
        """
        *Refresh the unit test database*
        """
        from fundamentals.mysql import directory_script_runner
        from fundamentals import tools
        packageDirectory = self.get_project_root()
        su = tools(
            arguments={"settingsFile": packageDirectory +
                       "/test_settings.yaml"},
            docString=__doc__,
            logLevel="DEBUG",
            options_first=False,
            projectName=None,
            defaultSettingsFile=False
        )
        arguments, settings, log, dbConn = su.setup()
        directory_script_runner(
            log=log,
            pathToScriptDirectory=packageDirectory + "/tests/input",
            dbConn=dbConn,
            successRule=None,
            failureRule=None
        )


def db(request):
    # database connection
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        if request.exception is not None:
            session.rollback()
        else:
            session.commit()
        session.close()
    request.add_finished_callback(cleanup)

    return session


class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        '''This is the default setup method for pyramid unit tests. It will instantiate a database connection to the unit_tesing database on localhost
        '''
        moduleDirectory = os.path.dirname(__file__)
        app_settings = appconfig(
            'config:' + self.testIni)
        from webtest import TestApp
        self.testapp = TestApp('config:' + self.testIni)
        # test user and test pass need to be adding to the test_settings.yaml
        # file
        self.testapp.post(
            '/login', params={'login': self.settings["test user"], 'password': self.settings["test pass"]})

    def tearDown(self):
        testing.tearDown()
