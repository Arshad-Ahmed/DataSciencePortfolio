## 1. Command Line Python ##

/home$ pwd

## 2. Creating a script ##

/home/dq$ echo -e 'import sys\n\n if __name__==__"main"__:\n print(sys.argv[1])'

## 3. Change file permissions ##

/home/dq$ chmod 0700 scipt.py

## 4. Create a virtualenv ##

/home/dq$ virtualenv -p /usr/bin/python3 script;source script/bin/activate

## 5. Move the script ##

(script) /home/dq$ mv script.py printer/

## 6. Execute the script ##

(script) /home/dq/printer$ python script.py "I'm so good at challenges!"