from setuptools import setup

version = '0.1'

setup(
    name='wsgijson',
    version=version,
    author='Casey Marks',
    author_email='casey@fivehut.com',
    description='helpers for JSON-based WSGI services',
    keywords='wsgi, json',
    url='http://github.com/fivehut/wsgijson',
    license='MIT',
    py_modules=['wsgijson'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        ],
    install_requires = [
        'WebOb >= 1.0',
        ],
    )
