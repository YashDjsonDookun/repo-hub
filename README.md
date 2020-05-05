# repo-hub

### Like I once said:

> I AM LAZY ~Djson 😎

🤡 This script requires both **_git_** and **_hub_** to be installed on your machines.
(You're expected to know how it's done, Not gonna explain...)

🤡 And of course, you're expected to have python3 installed too!

🤡 You'll also need to add the script to your **_PATH_** for this to work everywhere.
(Figure this out too)

### What does it do?
    -   provides the ability to create a remote repository within the current directory and push<br/>to it
    -   provides the ability to push to the existing remote repository within the current directory
(current directory here means the project directory that you are working on)

### Usage:
~~~
    python3 repo-hub.py -h or --help for any help
    python3 repo-hub.py -c or --create to create new repository and push to it
    python3 repo-hub.py -p <"Commit Message"> or --push <"Commit Message"> to push to current remote repository
~~~