all: file_upload

file_upload: file_upload.py
	$(info Attempting to update...)
	@git pull origin master
	@cp file_upload.py ~/cgi-bin/
	@chmod 777 ~/cgi-bin/file_upload.py
	@echo Successfully installed file_upload.py script
    
clean:
	@rm -rf ~/cgi-bin/file_upload.py
	@echo Successfully uninstalled file_upload.py script
