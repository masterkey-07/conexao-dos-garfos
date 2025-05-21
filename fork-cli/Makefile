APP_NAME=fork
ENTRY=main.py
VENV_DIR=.venv

all: build

setup:
	@if [ ! -d "$(VENV_DIR)" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV_DIR); \
	else \
		echo "Virtual environment already exists."; \
	fi

	@echo "Installing requirements..."
	$(VENV_DIR)/bin/pip install -r requirements.txt

run:
	@echo "Running project..."
	python3 main.py

build:
	@echo "Building standalone binary with PyInstaller..."
	pyinstaller --onefile --name $(APP_NAME) $(ENTRY)

test:
	@echo "Testing projects..."
	pytest

install: build
	@echo "Installing binary to /usr/local/bin/ (requires sudo)"
	sudo cp dist/$(APP_NAME) /usr/local/bin/$(APP_NAME)

uninstall:
	@echo "Uninstalling binary from /usr/local/bin/ (requires sudo)"
	sudo rm /usr/local/bin/$(APP_NAME)

clean:
	@echo "Cleaning build artifacts..."
	rm -rf build dist __pycache__ *.spec

.PHONY: all clean build install setup uninstall run test
