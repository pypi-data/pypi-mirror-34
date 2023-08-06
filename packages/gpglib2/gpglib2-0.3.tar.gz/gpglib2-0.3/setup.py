from setuptools import setup, find_packages
from gpglib import VERSION

# All the packages except test
packages = [pkg for pkg in find_packages() if not pkg.startswith('tests')]

setup(
      name = "gpglib2"
    , version = VERSION
    , packages = packages
    , install_requires =
      [ 'pycryptodome==3.6.4'
      , 'bitstring==3.1.5'
      ]

    , extras_require =
      { "tests":
        [ "noseOfYeti"
        , "nose"
        ]
      }

    # metadata for upload to PyPI
    , author = "Stephen Moore"
    , author_email = "delfick755@gmail.com"
    , description = "A python3 compatible fork of gpglib, a Library for decrypting gpg that doesn't shell out to gpg"
    , license = "LGPLv2"
    , keywords = "gpg decrypt"
    )
