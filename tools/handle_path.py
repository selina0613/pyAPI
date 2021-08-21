import os

result = os.path.abspath(__file__)
# print(result)

result1 = os.path.dirname(__file__)
# print(result1)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)

case_data_dir = os.path.join(base_dir, "test_data", "testCase.xlsx")
# print(case_data_dir)

case_dir = os.path.join(base_dir, "test_case")


report_dir = os.path.join(base_dir, "reports")
