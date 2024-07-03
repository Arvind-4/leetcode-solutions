from _constants import *

for root, dirs, files in os.walk("."):
    for dir in dirs:
        if dir in dirNames:
            shutil.rmtree(os.path.join(root, dir))
            try:
                os.remove(os.path.join(root, "Solution.Identifier"))
            except:
                pass