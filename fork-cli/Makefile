APP_NAME=fork
ENTRY=main.py

all: build

run:
	@echo "Running project..."
	python3 main.py

build:
	@echo "Building standalone binary with PyInstaller..."
	pyinstaller --onefile --name $(APP_NAME) $(ENTRY)

install: build
	@echo "Installing binary to /usr/local/bin/ (requires sudo)"
	sudo cp dist/$(APP_NAME) /usr/local/bin/$(APP_NAME)

clean:
	@echo "Cleaning build artifacts..."
	rm -rf build dist __pycache__ *.spec

.PHONY: all clean build install
