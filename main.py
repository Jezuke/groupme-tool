from groupy.client import Client
import os

TOKEN = os.getenv('TOKEN')
client = Client.from_token(TOKEN)

def get_nickname(member):
    return member.nickname

group = client.groups.get(51796422) # Getting group object for Official Chat

# group.members.sort(key=get_nickname)
# for member in group.members:
#     print(member)

# print("Total num of members:", len(group.members))

# Member experiment
# TODO Figure out what attributes a member has
