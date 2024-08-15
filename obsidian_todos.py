#!/usr/bin/env python3

import os
import datetime

def search_todos(obsidian_vault_path, todo_marker="- [ ]"):
    """
    Search for TODO items recursively
    """
    todos = []
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    """
    Traverse the directory
    """
    for root, _, files in os.walk(obsidian_vault_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.readlines()
                
                """
                Check for todos in the file
                """
                for line in content:
                    if todo_marker in line:
                        if today in line or "@today" in line:
                            todos.append(line.strip())
    
    return todos

# Prompt for the Obsidian vault path
obsidian_vault_path = input("Enter the path to your Obsidian vault: ")

todos = search_todos(obsidian_vault_path)

if todos:
    print("Today's TODOs:")
    for todo in todos:
        print(todo)
else:
    print("No TODOs found for today.")
