from setuptools import find_packages
from setuptools import setup
import os


version = '1.4'
shortdesc = 'wysihtml5 richtext widget for YAFOWIL with bootstrap integration'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'HISTORY.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()
tests_require = ['yafowil[test]']


setup(
    name='yafowil.widget.wysihtml5',
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
    url=u'http://pypi.python.org/pypi/yafowil.widget.wysihtml5',
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
    test_suite="yafowil.widget.wysihtml5.tests",
    entry_points="""
    [yafowil.plugin]
    register = yafowil.widget.wysihtml5:register
    example = yafowil.widget.wysihtml5.example:get_example
    """)
