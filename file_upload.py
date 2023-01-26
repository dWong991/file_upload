#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File Name:      file_upload.py
    Author:         Jaures Ade
    Date:           2/24/2018
    Python Version: 2.x
    Description:    Updated File Upload CGI script 
"""

import os
import cgi
import cgitb

cgitb.enable()


def printPrompt():
    print("""
<html>
    <head>
        <title>David's File Uploader</title>
    </head>
    <body>
        <h1>Debian File Uploader</h1>
        <form action="/cgi-bin/file_upload.py" 
           enctype="multipart/form-data" method="post">
            <h4>Select files to upload</h4>
                <input type="file" name="ufiles" multiple>
            <h4>Select destination for file</h4>
                <b>~/</b><input type="text" name="udir">
                <br>
            <input type="submit" value="Upload">
        </form>
        <p>
        </p>
    </body>
</html>
""")


def check_params():
    print("<html>\n")

    # Get Uploads
    form = cgi.FieldStorage()

    # Generator to buffer file in chunks
    def fbuff(f, bsize=10000):
        while True:
            buff = f.read(bsize)
            if not buff: break
            yield buff

    # Check that something was uploaded
    if 'udir' in form:
        ufiles = form['ufiles']
        if not isinstance(ufiles, list):
            if ufiles.filename is '':
                print("<b>*<i>No Files Selected</i>*</b>")
                return False
            ufiles = [form['ufiles']]
        udir = ""
        if 'udir' in form:
            udir = form['udir'].file.read()
            if not os.path.exists('/home/david/' + udir):
                print("""
                 <b>*<i>Invalid Destination:
                 '~/{0}' does not exist.
                 </i>*</b>
                 """.format(udir))
                return False

        # Attempt to write each file
        for ufile in ufiles:
            # Get base filename & ovoid directory access violation
            fn = os.path.basename(ufile.filename)

            # Split and write file by chunks
            f = open('/home/david/' + udir + '/' + fn, 'wb', 10000)
            for buff in fbuff(ufile.file):
                f.write(buff)
            f.close()
            print("""<pre>Successfully Uploaded:
                {0}</pre>
            """.format(fn))

        return True

    return False


if __name__ == "__main__":
    print("Content-Type: text/html\n\n")
    printPrompt()
    print("<hr>")
    check_params()
    print("</html>")
