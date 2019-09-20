from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/dryxPyramid/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.md') as f:
        return f.read()

setup(
    name='dryxPyramid',
    version=__version__,
    description='Templating and basecode for Pyramid webapps',
    long_description=readme(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    keywords=['utilities', 'pyramid'],
    url='https://github.com/thespacedoctor/dryxPyramid',
    download_url='https://github.com/thespacedoctor/dryxPyramid/archive/v%(__version__)s.zip' % locals(
    ),
    author='David Young',
    author_email='davidrobertyoung@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'dryxPyramid': [
        'resources/*/*', 'resources/*.*']},
    include_package_data=True,
    install_requires=[
        'pyramid',
        'sqlalchemy',
        'passlib',
        'paste',
        'sqlalchemy',
        'fundamentals',
        'mod_wsgi',
        'pymysql',
        'pytest',
        'webtest'
    ],
    test_suite='nose2.collector.collector',
    tests_require=['nose2', 'cov-core'],
    # entry_points={
    #     'console_scripts': ['funniest-joke=funniest.cmd:main'],
    # },
    zip_safe=False
)
