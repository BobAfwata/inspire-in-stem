# Creating a directory

mkdir git_basics
cd git_ basics 

# Adding files 

touch exercise_01.py 
touch exercise_02.py extercise_03.py exercise_04.py 

# Initializing the directory to use git 

git init 

# Configuring git 
This part assumes one has installed git on their machines if not install 
Windows : Download and install the executable
Linux : sudo apt-get install git 
MacOs : brew install git 

Create a Github accout : www.github.com

git configure user.name "BobAfwata"
git configure user.email "bob@xyz.com"


# Adding files to github
One says You commit the files into github 

git add *  #adds all files 
git add example_01.py  specific file

git commit -m "first python project"

git push   # Your files are now on github 

# Other useful git commands 
git clone www.url.git 
git branch master 
git checkout lesson_one
git stash


