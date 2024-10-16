"""
pip (also known by Python 3's alias pip3) is a package-management system written in Python and is used to install and manage software packages.
pip is used to download and install packages directly from PyPI. PyPI is hosted by Python Software Foundation. 
It is a specialized package manager that only deals with python packages.
After version python 3.4 has every python pip. We can install the package from the pypi website.
We can find a package, information about that package, methods and code examples and written there, how can i install that package
For example termcolor. 
On the terminal : pip3 --version => show the pip version
pip3 install termcolor => install the termcolor package
"""

import termcolor # this package for the write a text in different color and write types

#result = dir(termcolor)
#print(result)

#result = help(termcolor)
#print(result)

result = termcolor.colored("Hello",color="green",on_color="on_magenta")
print(result)

result = termcolor.colored("Hello Serhat",color="green",on_color="on_yellow",attrs=["bold"])
print(result)

#to list all packages, installed with pip => pip list
#uninstall a package => pip uninstall package_name