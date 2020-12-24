from setuptools import setup,find_packages

with open('README.rst','r') as f:
	readme = f.read()

setup(
	name ='pgbackup',
	version='0.1.0',
	description='Database backup locally or to AWS S3.',
	long_description=readme,
	author='Kushtar Zhaniev',
	author_email=zhkushtarbek@gmail.com,
	packages=find_packages('src'),
	package_dir={'':'src'},
	install_requires=[]
)
