# .bashrc

# Source global definitions
if [ -f /usr/socs/Profile ]; then
        . /usr/socs/Profile
fi

# User specific aliases and function

# display the welcome message
echo "Welcome to <$HOSTNAME>"
# display total number of sessions I am logged into
x=`who | grep $(whoami) | wc -l`
echo "You have $x login sessions to this host."
# Alias comp206 to go to the folder COMP206
alias comp206="cd ~/Projects/COMP206"
# set my shell's prompt to include my username, hostname, current directory and time
a=$(date +"%T")
export PS1="\u@$HOSTNAME[$a]: \w\$"
# display a random quote
fortune
# the thing of my liking: print today's date
b=`date`
echo "Today is $b"

