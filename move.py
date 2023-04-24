from constants import *

for path in BASE_DIR.glob("**/Solution.py"):
    if "Accepted" in str(path):
        shutil.move(
            path, path.parent.parent.parent / "Solution.py"
        )