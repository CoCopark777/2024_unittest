import os
import time

import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("./script",pattern="test*.py")
    unittest.main(defaultTest='suite', verbosity=2)
