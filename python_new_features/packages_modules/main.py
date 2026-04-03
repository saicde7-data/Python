# main_script.py
import sys
import os
sys.path.append(os.getcwd())
from .module1 import function_in_module1
from .module2 import function_in_module2

print(function_in_module1())
print(function_in_module2())