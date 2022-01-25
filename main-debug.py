import sys

from ApiTest.cli import main_hrun, main_locust
from ApiTest.logger import color_print

cmd = sys.argv.pop(1)

if cmd in ["apitest", "ApiTest", "api"]:
    main_hrun()
elif cmd in ["locust", "locusts"]:
    main_locust()
else:
    color_print("Miss debugging type.", "RED")
    example = "\n".join([
        "e.g.",
        "python main-debug.py apitest /path/to/testcase_file",
        "python main-debug.py locusts -f /path/to/testcase_file"
    ])
    color_print(example, "yellow")
