import os
import shutil
import cv2

jpg = ".jpg"
py = ".py"
src = "C:\\Users\\Greg\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
_1080p_ = (1080,1920)

# Pull images from assets folder, save in cwd
src_files = os.listdir(src)
for file in src_files:
	try:
		file_path = os.path.join(src, file)
		if os.path.isfile(file_path) and file+jpg not in os.listdir(os.getcwd()):
			shutil.copy(file_path, os.getcwd())
	except:
		pass


# Convert file to jpg, delete if not 1920x1080
# Ignore .jpg and .py files
for file in os.listdir(os.getcwd()):
	try:
		if file[-4:] != jpg and file[-3:] != py:
			os.rename(file, file+jpg)
			file = file+jpg
		size = cv2.imread(file,0).shape[:2]
		if size != _1080p_:
			os.remove(file)
	except:
		pass