from fastapi import FastAPI

app = FastAPI()

import subprocess

def run_js_script():
    result = subprocess.run(['node', 'your_script.js'], stdout=subprocess.PIPE)
    print(result.stdout)

run_js_script()
