#!/usr/bin/env python
import os
import subprocess
import shutil

def print_color(message, color_code):
    print(f"\033[{color_code}m{message}\033[0m")

YELLOW = "33"
GREEN = "32"
RED = "31"

def clone_repository(project_name):
    print_color("Cloning repository...", YELLOW)
    repo_url = "https://github.com/unclecode/fastapi-template.git"
    subprocess.run(["git", "clone", repo_url, project_name])

def git_clean():
    # Remove the git folder, if it exists
    if os.path.exists(".git"):
        shutil.rmtree(".git")

def git_init():
    print_color("Initializing Git...", YELLOW)
    subprocess.run(["git", "init"])

def git_add_remote(remote_url):
    # Change branch to Master
    subprocess.run(["git", "branch", "-M", "master"])
    print_color("Adding remote...", YELLOW)
    subprocess.run(["git", "remote", "add", "origin", remote_url])

def create_virtualenv():
    print_color("Creating virtual environment...", YELLOW)
    subprocess.run(["python3", "-m", "venv", "venv"])

def install_requirements():
    print_color("Installing requirements...", YELLOW)
    subprocess.run(["./venv/bin/pip", "install", "-r", "requirements.txt"])
def run_server():
    print_color("Running server...", YELLOW)
    subprocess.run(["./venv/bin/uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"])

if __name__ == "__main__":
    project_name = input("Enter the name of your new project: ")
    
    # Create project directory
    os.makedirs(project_name, exist_ok=True)
    
    # Change directory to the project directory
    os.chdir(project_name)

    # Clone repository
    clone_repository(".")

    # Remove the git folder, if it exists
    git_clean()

    # Initialize Git
    git_init_choice = input("Do you want to initialize a new Git repository? (yes/no): ")
    if git_init_choice.lower() == "yes":
        git_init()
        git_add_remote_choice = input("Do you want to add a remote? (yes/no): ")    
        if git_add_remote_choice.lower() == "yes":
            remote_url = input("Enter the remote URL: ")
            git_add_remote(remote_url)

    # Create Virtual Environment
    virtualenv_choice = input("Do you want to create a Python virtual environment? (yes/no): ")
    if virtualenv_choice.lower() == "yes":
        create_virtualenv()

    # Install requirements
    install_req_choice = input("Do you want to install requirements from requirements.txt? (yes/no): ")
    if install_req_choice.lower() == "yes":
        install_requirements()

    # Create .env file
    # create_env_choice = input("Do you want to create a .env file? (yes/no): ")
    # if create_env_choice.lower() == "yes":
    with open(".env", "w") as f:
        f.write("")
    
    # Run server
    # run_server_choice = input("Do you want to run the server? (yes/no): ")
    # if run_server_choice.lower() == "yes":
    #     run_server()

    # Explain to user they should set proper environment variable for database and jwt secret token then show how to run usin uvicorn
    print_color("Please set the proper environment variables for your database and JWT secret token.", YELLOW)
    print_color("Then run the server using the following command:", YELLOW)
    print_color("uvicorn app:app --host YOUR_HOST --port YOUR_PORT --reload", YELLOW)

    print_color(f"Project {project_name} setup completed.", GREEN)

