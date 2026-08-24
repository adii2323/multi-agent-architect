import os
import tempfile
from git import Repo
from crewai.tools import tool

@tool("List Directory Tool")
def list_directory(directory_path: str) -> str:
    """Lists all files and folders in a given directory path."""
    try:
        return str(os.listdir(directory_path))
    except Exception as e:
        return f"Error: {e}"

@tool("Read File Tool")
def read_file(file_path: str) -> str:
    """Reads the exact contents of a specific file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"

def clone_github_repo(repo_url: str) -> str:
    """Clones a public GitHub repository into a secure temporary directory and returns the path."""
    temp_dir = tempfile.mkdtemp(prefix="ai_repo_")
    try:
        print(f"Cloning {repo_url} into temporary path: {temp_dir}...")
        Repo.clone_from(repo_url, temp_dir)
        print("Clone successful!")
        return temp_dir
    except Exception as e:
        return f"Failed to clone repository: {e}"