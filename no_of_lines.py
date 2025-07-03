#!/usr/bin/env python3
import os

# Allowed source code file extensions
ALLOWED_EXTENSIONS = ('.java', '.py', '.kt', '.js', '.ts', '.vb', '.html', '.css')

def count_lines_in_source_files(directory):
    total_lines = 0
    line_counts = {}

    print(f"📁 Scanning directory: {directory}\n")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Only process allowed extensions
        if os.path.isfile(file_path) and filename.endswith(ALLOWED_EXTENSIONS):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    count = len(lines)
                    line_counts[filename] = count
                    total_lines += count

            except Exception as e:
                print(f"❌ Could not read {filename}: {e}")

    print("=== 📊 Summary ===")
    for file, count in line_counts.items():
        print(f"{file}: {count} lines")
    print(f"\n🧮 Total lines across all source files: {total_lines}")

# Example usage
directory_path = input("Enter the directory path: ").strip()
count_lines_in_source_files(directory_path)