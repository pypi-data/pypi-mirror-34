# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['ignorio']

package_data = \
{'': ['*']}

install_requires = \
['click>=6.7,<7.0', 'colorama>=0.3.9,<0.4.0', 'requests>=2.19,<3.0']

entry_points = \
{'console_scripts': ['ig = ignorio.cli:main']}

setup_kwargs = {
    'name': 'ignorio',
    'version': '0.2.1',
    'description': 'Manage your .gitignore with ease!',
    'long_description': "#Ignorio\n*Manage your .gitignore with ease!*\n\n\n**Ignorio** is a simple package to manage your [git exclusions](https://git-scm.com/docs/gitignore). This command line application helps you to download a template from [gitignore.io](http://gitignore.io/) without going to the site using the site's [API](https://www.gitignore.io/api/)\n\n\n#Usage\nTODO\n",
    'author': 'Franccesco Orozco',
    'author_email': 'franccesco@codingdose.info',
    'url': 'https://github.com/franccesco/ignorio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
