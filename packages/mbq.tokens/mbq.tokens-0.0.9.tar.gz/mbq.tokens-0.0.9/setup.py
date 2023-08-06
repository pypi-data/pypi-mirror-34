import codecs
import setuptools

__version__ = '0.0.9'

with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setuptools.setup(
    name='mbq.tokens',
    long_description=readme,
    version=__version__,
    license='Apache 2.0',
    url='https://github.com/managedbyq/mbq.tokens',
    author='Managed by Q, Inc.',
    author_email='open-source@managedbyq.com',
    maintainer='Managed by Q, Inc.',
    maintainer_email='open-source@managedbyq.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='jwt token authorization',
    packages=setuptools.find_packages(),
    install_requires=[
        'cryptography>=2.3,<3.0.0',
        'pyjwt>=1.6.4,<2.0.0',
    ],
    zip_safe=True,
)
