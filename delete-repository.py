import sys
from github import Github

# Authenticate

# using username and password
gh = Github("user", "password")

## or using an access token
gh = Github("Github Access Token")

# Github Enterprise with custom hostname
#gh = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")


for cli_arg in sys.argv[1:]:
    print(cli_arg)


print("This will delete these Github Repositories. Are you sure? CTRL-C to exit.\n")

junk_data=sys.stdin.readline()


# Lets loop through the repos to delete
for target_repo in sys.argv[1:]:
    print("Deleting Repo: ",target_repo)
    try:
        gh.get_repo(target_repo).delete()
    except:
        print("Whoops Something Went Wrong, skipping")
