from groupy.client import Client
import os

TOKEN = os.getenv('TOKEN')
client = Client.from_token(TOKEN)

def get_nickname(member):
    return member.nickname

"""
Get a Member object by searching through group for keyword in nickname.
"""
def get_member(group, keyword):
    group.members.sort(key=get_nickname)
    for member in group.members:
        if(keyword.lower() in member.nickname.lower()):
            return member

def main():
    group = client.groups.get(51796422) # Getting group object for Official Chat
    member = get_member(group, "aquitania")
    print(dir(member))

if __name__ == "__main__":
    main()

