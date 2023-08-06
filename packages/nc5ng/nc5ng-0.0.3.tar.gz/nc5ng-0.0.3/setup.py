from setuptools import setup

VERSION="0.0.3"
PKG_INFO= {
    'name':"nc5ng",
    'version':VERSION,
    'description': "Python MetaPackage for nc5ng",
    'long_description': """Used to install all components of nc5ng-python 

For More Information See: https://nc5ng.org/projects/nc5ng-python

For Documentation See: https://docs.nc5ng.org/latest
""",
    'author':"Andrey Shmakov",
    'author_email':"akshmakov@gmail.com",
    'url':"https://nc5ng.org/projects/nc5ng-python",
    'download_url':"https://github.com/nc5ng/nc5ng-python-toplevel",
    'install_requires':[
        'nc5ng-core==0.0.3'
        ],
    'license':"MIT"
}

setup(**PKG_INFO)
