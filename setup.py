from distutils.core import setup
setup(
    name='sahlin',
    version='0.1dev',
    author='Kristoffer Sahlin',
    author_email='kristoffer.sahlin@scilifelab.se',
    url='example.com',
    packages=['sahlin',],
    scripts = ['scripts/getting_data.py'],
    license='GPLv3',
    long_description=open('README.md').read(),
)
