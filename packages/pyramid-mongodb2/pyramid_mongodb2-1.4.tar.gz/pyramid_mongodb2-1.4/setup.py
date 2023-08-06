from setuptools import setup, find_packages


def readfile(name):
    with open(name) as f:
        return f.read()


README = readfile('README.md')

install_requires = [
    'pyramid',
    'pymongo',
    'pyramid_mongodb2_debugtoolbar'
]

testing_extras = [
    'WebTest',
    'nose',
    'coverage',
]

setup(name='pyramid_mongodb2',
      version='1.4',
      description='An improved package that provides mongodb connectivity. Not compatible with pyramid_mongo or pyramid_mongodb',
      long_description=README,
      long_description_content_type="text/markdown",
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "License :: OSI Approved :: MIT License",
      ],
      keywords='wsgi pylons pyramid mongodb pymongo pyramid_mongodb2_debugtoolbar',
      author="Jonathan Mackenzie",
      author_email="pylons-discuss@googlegroups.com",
      url="https://github.com/jonnoftw/pyramid_mongodb2",
      license="MIT",
      packages=find_packages('pyramid_mongodb2', exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      extras_require={
          'testing': testing_extras,
      },
      test_suite="tests",
      )
