py := python # python command
logger := keylogger.py # main logger entry point

run:: $(logger)
	python $(logger)

.PHONY: build
build::
	pyinstaller \
		--onefile \
		$(logger)

clean::
	@rm -rf \
		build/ \
		dist/ \
		__pycache__/ \
		*.spec \
		logs/*

install:: requirements.txt
	pip install -r requirements.txt