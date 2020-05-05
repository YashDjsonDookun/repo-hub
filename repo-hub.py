import os

current_directory = (os.path.basename(os.getcwd()))

def create_repository():
    os.system(f'echo # {current_directory} >> README.md')
    os.system("git init .")
    os.system("git add .")
    os.system('git commit -m "Initial Commit"')
    os.system("git push origin master")
    # pass

def push_to_repository():
    pass

create_repository()