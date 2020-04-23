import requests

# get all visible projects
response = requests.get(
    'https://demo-stable.kimai.org/api/projects',
    params={
        'visible': '1' #values: 1=visible, 2=hidden, 3=both (default; 1)
    },
    headers={
        'Accept': 'application/json',
        'X-AUTH-USER': 'susan_super',
        'X-AUTH-TOKEN': 'api_kitten',
    },
)
if response and response.status_code == 200:
    projects = response.json()
    print(projects)

# get all users (with id and name)
response = requests.get(
    'https://demo-stable.kimai.org/api/users',
    params={
        'visible': '1' #values: 1=visible, 2=hidden, 3=both (default; 1)
    },
    headers={
        'Accept': 'application/json',
        'X-AUTH-USER': 'susan_super',
        'X-AUTH-TOKEN': 'api_kitten',
    },
)
if response and response.status_code == 200:
    users = response.json()
    print(users)

#get all activities
response = requests.get(
    'https://demo-stable.kimai.org/api/activities',
    params={
        'visible': '1' #values: 1=visible, 2=hidden, 3=both (default; 1)
    },
    headers={
        'Accept': 'application/json',
        'X-AUTH-USER': 'susan_super',
        'X-AUTH-TOKEN': 'api_kitten',
    },
)
if response and response.status_code == 200:
    activities = response.json()
    print(activities)

#post (create) new timesheet for another user
response = requests.post('https://demo-stable.kimai.org/api/timesheets',
    data={
        "begin": "2020-04-23T15:00:23",
        "end": "2020-04-23T15:04:23",
        "project": 199,
        "activity": 2490,
        "description": "asdf 22 api python",
        "tags": "asdf 22",
    },
    headers={
        'Accept': 'application/json',
        'X-AUTH-USER': 'susan_super',
        'X-AUTH-TOKEN': 'api_kitten',
    },
)
if response and response.status_code == 200:
    timesheet = response.json()
    print(timesheet)