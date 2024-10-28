import os
import time
import HTMLTestRunner

import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("./script",pattern="test*.py")
    unittest.main(defaultTest='suite', verbosity=2)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # file = open('./report/report.html', 'wb')
    # runner = HTMLTestRunner(stream=file, verbosity=1, title="TestReport", tester='Li',
    #              description="测试详情如下：")
    # runner.run(suite)

