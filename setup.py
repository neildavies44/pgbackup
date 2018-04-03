from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Backup PostGreSQL databases locally or to AWS S3.',
    long_description=readme,
    author='Neil Davies',
    author_email='neil.davies44@gmail.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
