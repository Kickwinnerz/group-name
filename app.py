from flask import Flask, render_template, request
import random

app = Flask(__name__)

# List of fake member names to simulate fetching from a group
fake_members = [
    "Alice Johnson",
    "Bob Smith",
    "Charlie Brown",
    "Diana Prince",
    "Evan Wright",
    "Fiona Miller"
]

@app.route('/')
def index():
    """Renders the main form page."""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """Handles the form submission and simulates the process."""
    # Get data from the form
    group_uid = request.form['group_uid']
    pattern = request.form['nickname_pattern']

    # SIMULATION: "Change" the nicknames
    changed_members = []
    for idx, member in enumerate(fake_members, start=1):
        new_nickname = pattern.replace('{number}', str(idx))
        changed_members.append({
            'original_name': member,
            'new_nickname': new_nickname
        })

    # Pass the data to the results template
    return render_template('result.html', 
                           group_uid=group_uid,
                           pattern=pattern,
                           members=changed_members)

# This is necessary for Vercel to use the app correctly.
if __name__ == '__main__':
    app.run(debug=True)
else:
    # This is the crucial line for Vercel.
    # It provides the WSGI application object.
    application = app