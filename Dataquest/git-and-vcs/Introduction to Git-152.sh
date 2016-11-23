## 1. Version control systems ##

/home/dq/random_numbers$ git init

## 2. The .git folder ##

/home/dq/random_numbers$ ls -al

## 3. Creating some files ##

/home/dq/random_numbers$ echo "if __name__=="__main__":\nprint("10")" > script.p

## 4. Git status ##

/home/dq/random_numbers$ git add README.md

## 5. Configuring git ##

/home/dq/random_numbers$ git config --global user.name "Arshad Ahmed"

## 6. Committing ##

/home/dq/random_numbers$ git commit -m "Initial commit. Added script.py and READ

## 7. File differences ##

/home/dq/random_numbers$ git status

## 8. Making a second commit ##

/home/dq/random_numbers$ git commit -m "adding random number generation code"

## 9. Looking at the commit history ##

/home/dq/random_numbers$ git log

## 10. Seeing commit differences ##

/home/dq/random_numbers$ git log --stat