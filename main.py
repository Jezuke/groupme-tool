import os
from flask import Flask, redirect, url_for, request
from groupy.client import Client

TOKEN = os.getenv('TOKEN')
client = Client.from_token(TOKEN)

app = Flask(__name__)

def get_nickname(member):
    return member.nickname

"""
Get a Member object by searching through group for keyword in nickname.
"""
@app.route('/member/<name>')
def get_member(group, keyword):
    group.members.sort(key=get_nickname)
    for member in group.members:
        if(keyword.lower() in member.nickname.lower()):
            return member

@app.route('/search_member', methods=['POST'])
def search_member():
    if request.method == 'POST':
        group = client.groups.get(51796422) # Getting group object for Official Chat
        member_name = request.form['nm']
        member = get_member(group, member_name)
        return member.data

if __name__ == "__main__":
    app.run(debug=True)

