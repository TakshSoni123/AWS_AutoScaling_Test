import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["POST"])
def stress_cpu():
    # Start stress_cpu.py in a new process
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "CPU stress test started"

@app.route("/", methods=["GET"])
def get_ip():
    # Return the private IP address of the EC2 instance
    import socket
    return socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
