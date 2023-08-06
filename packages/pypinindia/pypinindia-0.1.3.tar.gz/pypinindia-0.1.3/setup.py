# @copyright: 2016. All rights reserved.

from setuptools import setup

try:
    from pypandoc import convert_file
    long_description = convert_file('README.md', 'md')

except ImportError:
    long_description = """
    
    Indian Pincodes and related Information
    
    
    More information at: https://github.com/rajacsp/pypinindia.
"""

setup(name='pypinindia',
      description='Indian Pincodes and related Information',
      long_description=long_description,
      version='0.1.3',
      url='https://github.com/rajacsp/pypinindia',
      author='Raja CSP Raman',
      author_email='raja.csp@gmail.com',
      license='Apache2',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3'
      ],
      packages=['pinin'],
      install_requires=[          
          'pypandoc>=1.4'
      ],
      entry_points={
          'console_scripts': [
              'encrypt=pinin.main:run'
          ]
      }
)