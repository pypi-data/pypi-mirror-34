from setuptools import setup, find_packages

setup(
    name='zaifapi',
    version='1.6.3',
    description='Zaif Api Library',
    long_description='https://pypi.python.org/pypi/zaifapi',
    url='https://github.com/techbureau/zaifapi',
    author='AkiraTaniguchi, DaikiShiroi',
    author_email='dededededaiou2003@yahoo.co.jp',
    packages=find_packages(),
    license='MIT',
    keywords='zaif bit coin btc xem mona jpy virtual currency block chain',
    classifiers=[
      'Development Status :: 1 - Planning',
      'Programming Language :: Python',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License'
    ],
    install_requires=['requests', 'websocket-client', 'Cerberus']
)
