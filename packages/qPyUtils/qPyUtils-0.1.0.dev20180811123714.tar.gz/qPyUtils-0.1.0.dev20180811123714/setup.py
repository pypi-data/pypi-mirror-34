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
        version = '0.1.0.dev20180811123714',
        description = '',
        long_description = '',
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
            'configs': ['properties.yml', 'properties_dev.yml', 'properties_qa.yml']
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
