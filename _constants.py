import os
import pathlib
import shutil
import tempfile

BASE_DIR = pathlib.Path(__file__).parent
FILE_NAME = "Solution"

dirNames = [
    "Time Limit Exceeded",
    "Wrong Answer",
    "Accepted",
    "Runtime Error",
    "Memory Limit Exceeded",
    "Compile Error",
    "Presentation Error",
    "Output Limit Exceeded",
    "Internal Error",
    "Restricted Function",
    "Restricted Keyword",
    "Restricted Library",
    "Restricted Header",
]
