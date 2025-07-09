from datetime import datetime, timedelta
import pytz
import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import re
from datetime import datetime, timedelta
import pytz

# Google Calendar API scope
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    creds = None
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def add_assignment_event(service, assignment):
    due_str = assignment['due_time']  # Example: "1st May '25 11:59 PM"

    due_str_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', due_str)

    try:
        due = datetime.strptime(due_str_clean, "%d %b '%y %I:%M %p")
    except ValueError:
        print(f"Could not parse date: {due_str}")
        return

    # Convert to India Standard Time (IST)
    ist = pytz.timezone('Asia/Kolkata')
    due = ist.localize(due)

    event = {
        'summary': f"Assignment: {assignment['subject']}",
        'description': f"ETLab Assignment\nStatus: {assignment['status']}",
        'start': {
            'dateTime': due.isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': (due + timedelta(hours=1)).isoformat(),
            'timeZone': 'Asia/Kolkata',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 60 * 24},  # 1 day before
            ],
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"Event added: {event.get('htmlLink')}")