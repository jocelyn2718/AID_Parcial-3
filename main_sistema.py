# Jocelyn Alfaro Castro 
# Generar un programa que consuma una api que muestre hostname e ip de una maquina

from flask import Flask, jsonify
import platform
import sys
import subprocess

app = Flask(__name__)

@app.route('/task')
def index():
    hostname = platform.node()
    local_ip = get_local_ip()

    data = {
        "hostname": hostname,
        "local_ip": local_ip
    }
    return jsonify(data)

def get_local_ip():
    if platform.system() == "Windows":
        local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
    else:
        local = subprocess.getoutput("ifconfig | grep 'inet' | grep -Fv 127.0.0.1 | awk '{print $2}'")
    return local

if __name__ == '__main__':
    app.run(debug=True)