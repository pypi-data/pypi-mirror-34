from setuptools import find_packages
from setuptools import setup
import os


version = '1.4'
shortdesc = 'Select2 widget for YAFOWIL'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()
tests_require = ['yafowil[test]']


setup(
    name='yafowil.widget.select2',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='',
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    url=u'https://github.com/bluedynamics/yafowil.widget.select2',
    license='Simplified BSD',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['yafowil', 'yafowil.widget'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'yafowil>2.1.99',
    ],
    tests_require=tests_require,
    extras_require = dict(
        test=tests_require,
    ),
    test_suite="yafowil.widget.select2.tests",
    entry_points="""
    [yafowil.plugin]
    register = yafowil.widget.select2:register
    example = yafowil.widget.select2.example:get_example
    """)
