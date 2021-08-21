import unittest
import unittestreport
from tools.handle_path import case_dir, report_dir



#测试套件
suite = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern="test_register.py")

runner=unittestreport.TestRunner(
    suite=suite,
    filename="report.html",
    report_dir=report_dir,
    title="接口测试报告",
    tester="long",
    desc="接口自动化测试报告",
    templates=1

)
runner.run()
