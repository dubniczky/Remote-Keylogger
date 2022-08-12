logger := keylogger.py

run:: $(logger)
	python $(logger)

build::
	pyinstaller --onefile $(logger)

clean::
	@rm -rf build/ dist/ __pycache__/ *.spec
