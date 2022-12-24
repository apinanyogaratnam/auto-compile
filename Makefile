VERSION := 0.1.0

.PHONY: build

start:
	python main.py .py date --clear

build:
	pyinstaller --onefile main.py

tag:
	git tag -m "v${VERSION}" v${VERSION}
	git push --tags

workflow:
	make tag
