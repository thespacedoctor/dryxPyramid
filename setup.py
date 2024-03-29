from setuptools import setup, find_packages
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/dryxPyramid/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.md') as f:
        return f.read()


install_requires = [
    'pyyaml',
    'fundamentals',
    'pyramid',
    'sqlalchemy',
    'passlib',
    'paste',
    'fundamentals',
    'pymysql',
    'khufu',
    'numpy'
]

# READ THE DOCS SERVERS
exists = os.path.exists("/home/docs/")
if exists:
    c_exclude_list = ['healpy', 'astropy',
                      'numpy', 'sherlock', 'wcsaxes', 'HMpTy', 'ligo-gracedb', 'mod_wsgi']
    for e in c_exclude_list:
        try:
            install_requires.remove(e)
        except:
            pass

setup(name="dryxPyramid",
      version=__version__,
      description="basic, reusable code for pyramid webapps",
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Topic :: Utilities',
      ],
      keywords=['pyramid, webapp'],
      url='https://github.com/thespacedoctor/dryxPyramid',
      download_url='https://github.com/thespacedoctor/dryxPyramid/archive/v%(__version__)s.zip' % locals(
      ),
      author='David Young',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["*tests*"]),
      include_package_data=True,
      install_requires=install_requires,
      test_suite='nose2.collector.collector',
      tests_require=['nose2', 'cov-core'],
      # entry_points={
      #     'console_scripts': ['dryxPyramid=dryxPyramid.cl_utils:main'],
      # },
      zip_safe=False)
