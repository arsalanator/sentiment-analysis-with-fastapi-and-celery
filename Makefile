# Makefile for Sentiment CSV Service 🛠️

.DEFAULT_GOAL := help

.PHONY: help init lint test run

## help: Show this help message
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

## init: Initialize folder structure with .gitkeep files
init:
	@chmod +x scripts/init_folder_structure.sh
	@scripts/init_folder_structure.sh

## lint: Run code formatters and linters (e.g., black, flake8)
lint:
	@echo "🧹 Running lint check (black, flake8)..."
	@black src tests
	@flake8 src tests

## test: Run all tests using pytest
test:
	@echo "🧪 Running tests..."
	@pytest tests

## run: Run the FastAPI app (main/api.py)
run:
	@echo "🚀 Starting FastAPI server..."
	@uvicorn src.main.api:app --reload
