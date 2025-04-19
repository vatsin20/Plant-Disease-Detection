import os
import sys
import subprocess

# This is the directory where PyInstaller unpacks the files
basedir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# The directory where the app is launched from
launch_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# Always use embedded Python from _MEIPASS when bundled
python_exe = os.path.join(basedir, "python.exe")

# In development (not bundled), fallback to system Python
if not os.path.exists(python_exe):
    python_exe = sys.executable

# app.py is in the launch directory
app_path = os.path.join(launch_dir, "app.py")

# Run the streamlit command
command = f'"{python_exe}" -m streamlit run "{app_path}"'
print("Running command:", command)
subprocess.call(command, shell=True)
input("Press Enter to close this window...")
