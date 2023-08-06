
from distutils.core import setup
setup(
  name = 'pynamo',
  packages = ['pynamo'],
  version = '1.0.3',
  description = 'Python Library for Handling Dynamo Syntax and requests.',
  author = 'Barry Howard',
  author_email = 'barry.howard@ge.com',
  keywords = ["dynamo", "ge", "cloudops", "aws"],
  classifiers = [],
  install_requires=[
    "boto3"
  ],
)