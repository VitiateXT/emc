import os

os.system('pyinstaller emc.py --onefile')
os.system(r'move dist\emc.exe C:\Users\vitia\AppData\Local\Programs\Python\Python312\Scripts\emc.exe')