# RepoCleanup

Needed a quick way to clean up my forks of repos... this is the way to do it quickly.

# Python Requirements

* PyGithub


# Scripts

Just a couple of scripts for performing the most basic actions desired

## list-repositories.py

List out the repositories owned by your repository. You can use the repo names generated from this
script to feed into the delete script.

Update the script with the required authnetication method and just run with no params.

## delete-repository.py

This is the delete script. 
Update the script with the required authnetication method
and pass the full name of the repo you want to delete as arguments:

```
# Assuming your GitHub account is: JohnSmith
# And the repos you want to delete are: BlueBox, RedBox, and GreenBox

# Single delete
./delete-repository.py JohnSmith/BlueBox

# Multiple delete
./delete-repository.py JohnSmith/RedBox JohnSmith/GreenBox

