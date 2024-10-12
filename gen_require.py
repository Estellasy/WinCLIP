import os
import subprocess

project_path = os.path.dirname(os.path.abspath(__file__))
subprocess.run(['pipreqs', project_path, '--force'])