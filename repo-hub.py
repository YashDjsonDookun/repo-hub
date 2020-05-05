import os

current_directory = (os.path.basename(os.getcwd()))

def create_repository():
    os.system(f'echo # {current_directory} >> README.md')
    os.system("git init .")
    os.system("git add .")
    os.system('git commit -m "Initial Commit"')
    os.system("hub create")
    os.system("git push origin master")

def push_to_repository(commitArg):
    os.system("git add .")
    os.system(f'git commit -m "{commitArg}"')

# create_repository()
push_to_repository("Fixed readme")