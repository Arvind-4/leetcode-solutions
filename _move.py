from _constants import *

for path in BASE_DIR.glob("**/Solution.*"):
    if "Accepted" in str(path):  
        shutil.move(
            path, path.parent.parent.parent / (FILE_NAME + path.suffix)
        )