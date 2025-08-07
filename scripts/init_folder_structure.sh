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

# === Core Layer ===
create_folder_with_gitkeep src/core/domain/models
create_folder_with_gitkeep src/core/domain/repositories
create_folder_with_gitkeep src/core/domain/services

create_folder_with_gitkeep src/core/application/use_cases
create_folder_with_gitkeep src/core/application/dtos

create_folder_with_gitkeep src/core/infrastructure/persistence
create_folder_with_gitkeep src/core/infrastructure/file_storage
create_folder_with_gitkeep src/core/infrastructure/sentiment_analysis
create_folder_with_gitkeep src/core/infrastructure/messaging

create_folder_with_gitkeep src/core/interfaces/api/routes
create_folder_with_gitkeep src/core/interfaces/api/schemas
create_folder_with_gitkeep src/core/interfaces/cli

create_folder_with_gitkeep src/core/config/env
create_folder_with_gitkeep src/core/config/logging

create_folder_with_gitkeep src/core/shared/exceptions
create_folder_with_gitkeep src/core/shared/utils

# === Engine Layer ===
ENGINE="csv_sentiment"
create_folder_with_gitkeep src/engines/$ENGINE/handlers
create_folder_with_gitkeep src/engines/$ENGINE/config
create_folder_with_gitkeep src/engines/$ENGINE/utils

# === Tasks ===
create_folder_with_gitkeep src/tasks
touch src/tasks/${ENGINE}_tasks.py

# === Main Entrypoints ===
create_folder_with_gitkeep src/main
touch src/main/api.py
touch src/main/worker.py

# === Tests ===
create_folder_with_gitkeep tests/core/domain
create_folder_with_gitkeep tests/core/application
create_folder_with_gitkeep tests/core/infrastructure
create_folder_with_gitkeep tests/core/interfaces
create_folder_with_gitkeep tests/engines/$ENGINE

# === Top-Level Files ===
touch .env .gitignore README.md requirements.txt pyproject.toml

echo "✅ Folder structure created with .gitkeep files under '$PROJECT_ROOT'"
