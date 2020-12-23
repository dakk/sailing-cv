from setuptools import find_packages
from setuptools import setup


setup(name='sailingcv',
	version=0.1,
	description='',
	author=['Davide Gessa'],
	setup_requires='setuptools',
	author_email=['gessadavide@gmail.com'],
	packages=['sailingcv'],
	package_data={},
	entry_points={
		'console_scripts': [
			'sailingcv-test=sailingcv.main:start'
		],
	},
	install_requires=open ('requirements.txt', 'r').read ().split ('\n')
)
