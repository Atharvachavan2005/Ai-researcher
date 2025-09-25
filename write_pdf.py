from langchain_core.tools import tool
from datetime import datetime
from pathlib import Path
import subprocess
import shutil

output_dir =Path("output").absolute()
output_dir.mkdir(exist_ok=True)
