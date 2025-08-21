#!/usr/bin/env python3
import os

# Allowed source code file extensions
ALLOWED_EXTENSIONS = (
    # High-usage programming languages
    '.py',     # Python
    '.java',   # Java
    '.js',     # JavaScript
    '.ts',     # TypeScript
    '.jsx',    # React (JavaScript)
    '.tsx',    # React (TypeScript)
    '.cpp',    # C++
    '.c',      # C
    '.cs',     # C#
    '.rb',     # Ruby
    '.go',     # Go
    '.php',    # PHP
    '.swift',  # Swift
    '.kt',     # Kotlin
    '.rs',     # Rust
    '.m',      # Objective-C
    '.r',      # R
    '.dart',   # Dart
    '.scala',  # Scala
    '.sh',     # Shell script

    # Web development / frontend
    '.html',   # HTML
    '.css',    # CSS

    # Configuration / markup / data
    '.json',   # JSON config/data
    '.yaml', '.yml',  # YAML
    '.xml',    # XML
    '.ini',    # INI files
    '.toml',   # TOML
    '.env',    # Environment variables
    '.config', # Generic .config files
    '.cfg',    # Configuration
    '.properties', # Java .properties files
    '.sql',    # SQL scripts
)

def count_lines_in_source_files(directory):
    total_lines = 0
    line_counts = {}

    print(f"\n📁 Scanning directory (including subdirectories): {directory}\n")

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(ALLOWED_EXTENSIONS):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                        count = len(lines)
                        relative_path = os.path.relpath(file_path, directory)
                        line_counts[relative_path] = count
                        total_lines += count
                except Exception as e:
                    print(f"❌ Could not read {file_path}: {e}")

    if line_counts:
        print("=== 📊 Summary of Source Code Line Counts ===\n")
        for file, count in sorted(line_counts.items()):
            print(f"📄 {file}: {count} lines")
        print(f"\n🧮 Total lines across all source files: {total_lines}")
    else:
        print("⚠️ No source files with allowed extensions found.")

# Example usage
if __name__ == '__main__':
    directory_path = input("📥 Enter the directory path: ").strip()
    if os.path.isdir(directory_path):
        count_lines_in_source_files(directory_path)
    else:
        print("❌ Invalid directory path. Please enter a valid one.")


