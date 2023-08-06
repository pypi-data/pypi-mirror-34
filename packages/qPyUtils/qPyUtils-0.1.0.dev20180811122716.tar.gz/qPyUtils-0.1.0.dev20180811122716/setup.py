#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'qPyUtils',
        version = '0.1.0.dev20180811122716',
        description = 'qPyUtils',
        long_description = 'qPyUtils\n========\n\nPython/Bash utils by qianws and his collections\n\n.. raw:: html\n\n   <!---\n   ![Progress](http://progressed.io/bar/30?title=completed)\n   [![codebeat badge](https://codebeat.co/badges/a0171eb6-cda3-4c33-b5bc-fbba1affa373)](https://codebeat.co/projects/github-com-koyo922-qpyutils-master)\n   [![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)\n   [![Join the chat at https://gitter.im/qPyUtils/Lobby](https://badges.gitter.im/qPyUtils/Lobby.svg)](https://gitter.im/qPyUtils/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n   -->\n\n|Build Status| |codecov| |PyPI version| |Python versions| |platform|\n\ncurrently, includes:\n\n-  ``log.writer`` for standardized style of using logger\n-  [STRIKEOUT:``log.parser`` an extensible framework for parsing logs in\n   parallel]\n\n.. |Build Status| image:: https://travis-ci.org/koyo922/qPyUtils.svg?branch=master\n   :target: https://travis-ci.org/koyo922/qPyUtils\n.. |codecov| image:: https://codecov.io/gh/koyo922/qPyUtils/branch/master/graph/badge.svg\n   :target: https://codecov.io/gh/koyo922/qPyUtils\n.. |PyPI version| image:: https://badge.fury.io/py/qPyUtils.svg\n   :target: https://badge.fury.io/py/qPyUtils\n.. |Python versions| image:: https://img.shields.io/badge/python-2.7%20%7C%203.6-blue.svg\n   :target: https://www.python.org/downloads/release\n.. |platform| image:: https://img.shields.io/badge/platform-mac%20os%20%7C%20linux-lightgrey.svg\n\n',
        author = 'Qian Weishuo ',
        author_email = 'qzy922@gmail.com',
        license = 'MIT License',
        url = 'https://github.com/koyo922/qPyUtils',
        scripts = [],
        packages = [
            'qPyUtils',
            'qPyUtils.log'
        ],
        namespace_packages = [],
        py_modules = [],
        classifiers = [
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        entry_points = {},
        data_files = [],
        package_data = {
            'configs': ['properties_qa.yml', 'properties_dev.yml', 'properties.yml']
        },
        install_requires = [
            'six',
            'pathlib'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
