#!/bin/bash

PROJECT_ROOT="sentiment_csv_service"
mkdir -p $PROJECT_ROOT/src
cd $PROJECT_ROOT

echo "🔧 Creating folder structure..."

# Helper function to create folder and .gitkeep
create_folder_with_gitkeep() {
  mkdir -p "$1"
  touch "$1/.gitkeep"
}

# === Core Domain Layer ===
create_folder_with_gitkeep src/core/domain/models
create_folder_with_gitkeep src/core/domain/repositories
create_folder_with_gitkeep src/core/domain/services

# === Application Layer ===
create_folder_with_gitkeep src/core/application/use_cases
create_folder_with_gitkeep src/core/application/dtos
create_folder_with_gitkeep src/core/application/ports/input
create_folder_with_gitkeep src/core/application/ports/output
create_folder_with_gitkeep src/core/application/services

# === Configuration and Shared Utilities ===
create_folder_with_gitkeep src/core/config/env
create_folder_with_gitkeep src/core/config/logging
create_folder_with_gitkeep src/core/shared/exceptions
create_folder_with_gitkeep src/core/shared/utils

# === Infrastructure (Adapters/Drivers) ===
create_folder_with_gitkeep src/core/infrastructure/adapters/input/fastapi_api
create_folder_with_gitkeep src/core/infrastructure/adapters/input/celery_worker
create_folder_with_gitkeep src/core/infrastructure/adapters/output/celery_broker
create_folder_with_gitkeep src/core/infrastructure/adapters/output/pandas_adapter
create_folder_with_gitkeep src/core/infrastructure/adapters/output/textblob_adapter

# === File Storage, Messaging, and Persistence Adapters ===
create_folder_with_gitkeep src/core/infrastructure/file_storage
create_folder_with_gitkeep src/core/infrastructure/messaging
create_folder_with_gitkeep src/core/infrastructure/persistence
create_folder_with_gitkeep src/core/infrastructure/sentiment_analysis

# === Engines (Flat Utility Modules for Business Logic) ===
ENGINE="csv_sentiment"
create_folder_with_gitkeep src/engines/$ENGINE/handlers
create_folder_with_gitkeep src/engines/$ENGINE/config
create_folder_with_gitkeep src/engines/$ENGINE/utils

# === Tasks ===
create_folder_with_gitkeep src/tasks
touch src/tasks/${ENGINE}_tasks.py

# === Entrypoints (API / Worker) ===
create_folder_with_gitkeep src/main
touch src/main/api.py
touch src/main/worker.py

# === Tests ===
create_folder_with_gitkeep tests/core/domain
create_folder_with_gitkeep tests/core/application
create_folder_with_gitkeep tests/core/infrastructure
create_folder_with_gitkeep tests/engines/$ENGINE

# === Top-Level Files ===
touch .env .gitignore README.md requirements.txt pyproject.toml

echo "✅ Folder structure created with .gitkeep files under '$PROJECT_ROOT'"
