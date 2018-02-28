# file_upload
Python program to upload files from host to guest in Virtual Box

---

## Installation ##

First clone the git repo and cd into the directory
```bash
$ git clone https://github.com/david-topham/file_upload.git
$ cd file_upload
```

Next, run the makefile to install the script
```bash
$ make
```

To cleanup or uninstall the script, simply run make clean
```bash
$ make clean
```

---

## Usage ##

##### 1. The script has a simple interface allowing you to select files and where you would like to upload them in your virtual machine.
<img src="/imgs/fuimg1.PNG" width="400">

##### 2. After successfully uploading files to your virtual machine, the HTML page will display all uploaded files. You can verify in your machine as well that they were all uploaded.
<img src="/imgs/fuimg4.PNG" width="400">

#### 3. Errors will occur if no files are specified or if the specified directory is invalid or does not have proper permissions
<img src="/imgs/fuimg5.PNG" width="400">

