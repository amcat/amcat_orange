from setuptools import setup

from os import path
from pip.req import parse_requirements
from pip.download import PipSession

here = path.abspath(path.join(path.dirname(path.abspath(__file__))))

requirements_txt = path.join(here, "requirements.txt")
requirements = parse_requirements(requirements_txt, session=PipSession())
requirements = [str(ir.req) for ir in requirements]

packages = setuptools.find_packages(here, exclude=["*.tests"])

readme = path.join(here, "README.pypi")

if __name__ == '__main__':
    setup(name = 'orange3sma',
          description = "Provides widgets for social media analytics",
          long_description = open(readme).read(),
          version = '0.1.31',
          packages = packages,
          entry_points={'orange3.addon': 'Social Media Analytics = orange3sma',
                        "orange.widgets": "Social Media Analytics = orange3sma.widgets",
                        'orange.widgets.tutorials': 'exampletutorials = orange3sma.tutorials'},
          author = 'Kasper Welbers and Wouter van Atteveldt',
          author_email = 'k.welbers@vu.nl',
          url = 'https://github.com/amcat/orange3sma',
          install_requires = requirements,
          keywords = ['orange3sma', 'orange3 add-on'],

          include_package_data=True,
          exclude_package_data = {'': ['tests/*']}
          )

