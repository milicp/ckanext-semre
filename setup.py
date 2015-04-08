from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-semre',
	version=version,
	description="CKAN extension for RDF description of dataset relationships",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Petar Milic',
	author_email='milicpetar86@gmail.com',
	url='',
	license='open',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.semre'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
    entry_points='''
        [ckan.plugins]
        semre=ckanext.semre.plugin:SemRePlugin
    ''',
)
