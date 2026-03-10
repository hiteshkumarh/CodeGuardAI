import sys
import subprocess
with open('clean_output.txt', 'w', encoding='utf-8') as f:
    subprocess.run([r'..\.venv\Scripts\python.exe', 'run_validation.py'], stdout=f, stderr=subprocess.STDOUT, text=True)
print("Done")
