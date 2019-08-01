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
    *Override fundamentals utKit*
    """
    # Variable Data Atrributes

    # Override Variable Data Atrributes
    # Initialisation
    def __init__(
            self,
            moduleDirectory
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
        self.dbConfig = """
         version: 1
         db: unit_testing
         host: localhost
         user: unittesting
         password: utpass
         """

        return


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
        engine = engine_from_config(app_settings, prefix='sqlalchemy.')
        self.config = testing.setUp()
        self.config.registry.dbmaker = sessionmaker(bind=engine)
        self.config.add_request_method(db, reify=True)
        self.config.add_settings(self.testSettings)

        # SETUP A DATABASE CONNECTION BASED ON WHAT ARGUMENTS HAVE BEEN PASSED
        settings = self.testSettings
        if "database settings" in settings:
            host = settings["database settings"]["host"]
            user = settings["database settings"]["user"]
            passwd = settings["database settings"]["password"]
            dbName = settings["database settings"]["db"]
            dbConn = ms.connect(
                host=host,
                user=user,
                passwd=passwd,
                db=dbName,
                use_unicode=True,
                charset='utf8',
                local_infile=1,
                client_flag=ms.constants.CLIENT.MULTI_STATEMENTS,
                connect_timeout=3600
            )
            dbConn.autocommit(True)
            self.config.add_settings({"dbConn": dbConn})

    def tearDown(self):
        testing.tearDown()
