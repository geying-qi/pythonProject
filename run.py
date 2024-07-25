import os
import time

import pytest

from commons.yaml_util import write_yaml, read_yaml, clear_yaml

if __name__ == '__main__':
    pytest.main()
    time.sleep(4)
    os.system("allure generate ./temps -o ./reports --clean")
    #write_yaml("a")
    #read_yaml()
    #clear_yaml()

