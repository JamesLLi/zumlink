from flask import Flask
import subprocess
app = Flask(__name__)

@app.route("/")
def ping():
    text_file = open("output.txt", "w")
    data = (subprocess.check_output(["ping", "-c3", "-q", "192.168.111.100"]))
    text_file.write(data)
    text_file.close()
	
if __name__ == "__main__":
    app.run(host='0.0.0.0')
