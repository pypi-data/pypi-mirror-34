from setuptools import setup
from setuptools import find_packages

setup(name='haasomeapi',
      version='3.1.14.14',
      description='Python module to interact with the Haasonline Local API',
      url='http://github.com/haasome-tools/haasomeapi',
      author='Haasome Tools',
      author_email='haasomeapi@haasometools.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'requests',
      ],
      zip_safe=False)
