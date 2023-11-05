import os
import sys

module_path = os.path.abspath("../src/rcac/app.py")
sys.path.append(os.path.dirname(module_path))

import app

app.lambda_handler(" ", " ")