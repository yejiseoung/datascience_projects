# Besic commands to setup the configuration
git config --global user.name "YejiSeoung"
git config --global user.email "yejiseoung.ds@gmail.com"

git init directoryname
git init


# Compare to stanged file to previous commit
git diff --cached


# Show where git configs are found
git config --list --show-origin

# Git Commands
git commit -a -m "Added changes without staging"

# deletes and removes the file from being tracked
git rm

# removes the file from being tracked but does not delete
git rm --cached

# renames the file
git mv file to file2

# show history
git log

# show pathch for what has changed for the last 2 commits
git log -p -2 # shows changes - good for code review or what has changed

# show log summary
git log --staticmethod
# pinrts in oneline
git log --pretty=oneline
# shows nice graph and useful visual for branching
git log --pretty=oneline --graph

# shows different output
git log --pretty=format:"%H %an %ae %ar %s"

# search for keyword in the message
git log --grep py(keyword)

# search by author
git log --author="YejiSeoung"

# search for code changes
git log -S code_cahnges

# change the last commit
git commit --amend

# unstage a file
git restore --staging filename

# resets the file
git restore filename