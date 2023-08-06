import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='odbindex',
    version='0.0.4',
    author='Marko Sanković',
    author_email='msankovic@synapticon.com',
    description='Generate OBLAC Drives Bundle Index Page',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/synapticon/odbindex',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux'
    ),
    scripts=['odbindex']
)
