## 1. Merge conflicts ##

/home/dq/chatbot$ git merge feature/queen-bot master

## 2. Aborting a merge ##

/home/dq/chatbot$ git merge --abort

## 3. Fixing the conflicts ##

/home/dq/chatbot$ echo -e "print('I am the queen')" > bot.py

## 4. Multi-line conflicts ##

/home/dq/chatbot$ git add .;git commit -m "Resolved multi-line conflict"; git pu

## 5. Multiple conflicts ##

/home/dq/chatbot$ git add .;git commit -m "Resolved multiple conflicts";git push

## 6. Accepting changes from only one branch ##

/home/dq/chatbot$ git push origin master

## 7. Ignoring files ##

/home/dq/chatbot$ git add .;git commit -m "Added gitignore";git push origin mast

## 8. Removing cached files ##

/home/dq/chatbot$ git rm bot.py ;git add .;git commit -m "Removed bot.py";git pu