from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='blockchainpy',
      version='0.0.4',
      description='A blockchain implementation in Python',
      url='https://github.com/rishikant42/blockchain',
      author='Rishi kant',
      author_email='rshkntshrm@gmail.com',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      packages=['blockchain'],
      install_requires=[
          'pycrypto',
          'requests',
      ],
      zip_safe=False)
