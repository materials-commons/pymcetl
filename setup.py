# build with: python setup.py install --user

from setuptools import setup, find_packages


try:
    with open('mcetl/VERSION.txt') as f:
        version = f.read().strip()
except IOError:
    version = '0.9.0'


setup(
    name='mcetl',
    version=version,
    description='The Materials Commons ETL command',
    long_description="""Python version of ETL parser""",
    url='https://materials-commons.github.io/python-api/',
    author='Materials Commons development team',
    author_email='materials-commons-authors@umich.edu',
    license='MIT',
    package_data={'mcetl': ['VERSION.txt']},
    include_package_data=True,
    packages=find_packages(),
    scripts=['scripts/pymcetl'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],
    keywords='materials science mc etl lift prisms',
    install_requires=[
        "configparser",
        "httplib2",
        "six",
        "rethinkdb==2.3.0.post6",
        "xlsxwriter",
        "openpyxl",
        "materials_commons"
    ]
)
