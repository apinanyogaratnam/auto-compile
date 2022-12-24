VERSION := 0.0.1

.PHONY: build

start:
	python main.py .py date --clear

build:
	pyinstaller --onefile main.py
