import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# The ID and range of a sample spreadsheet.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1STgXfT69YyLs8i-SaeNPU6bGRRUUDaYdGMJqjODIS5E"
SHEET_RANGE = "ENGINE OIL"
NEW_SHEET_TITLE = "AUTOMATED"


def get_values(service):
    request = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                    range=SHEET_RANGE).execute()
    values = request.get('values', [])

    if not values:
        print('No data found.')
        return

    return values
                

def create_sheet(title, service):
    new_sheet = {
        "requests": [{
            "addSheet": {
                "properties": {
                    "title": title,
                    "index": 0
                }
            }
        }]
    }
    request = service.spreadsheets().batchUpdate(
        spreadsheetId = SPREADSHEET_ID,
        body = new_sheet
    )
    response = request.execute()

    print(response)


def rearrange_values(data, service):
    SKIP_ROW = 1
    SKIP_COLUMN = 5
    output_range = "A"
    
    for row in data:
        new_data = []

        if SKIP_ROW:
            SKIP_ROW -= 1
            continue
        for i in range(len(row)):
            if i>0 and i <= SKIP_COLUMN:
                continue
            elif row[i]:
                new_data.append([row[i]])
        print(new_data)
        add_values_to_sheet(new_data, service, output_range)

        # Write to new column
        if output_range[-1] == "Z":
            output_range = list(output_range)
            output_range[-1] = "A"
            output_range = "".join(output_range)
            output_range = "A" + output_range

        else:
            output_range = list(output_range)
            output_range[-1] = chr(ord(output_range[-1]) + 1)
            output_range = "".join(output_range)
        

def add_values_to_sheet(data, service, range):
    request = service.spreadsheets().values().append(spreadsheetId = SPREADSHEET_ID,
                                                     range = f"{NEW_SHEET_TITLE}!{range}:{range}",
                                                     valueInputOption = "USER_ENTERED",
                                                     insertDataOption = "OVERWRITE",
                                                     includeValuesInResponse = False,
                                                     responseValueRenderOption = "UNFORMATTED_VALUE",
                                                     responseDateTimeRenderOption = "FORMATTED_STRING",
                                                     body={"values": data})
    response = request.execute()
    print(response)


def main():
    creds = None

    """The file token.json stores the user's access and refresh tokens, and is
    created automatically when the authorization flow completes for the first
    time."""
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        data = get_values(service)
        # create_sheet(NEW_SHEET_TITLE, service)
        rearrange_values(data, service)


    except HttpError as err:
        print(err)




if __name__ == '__main__':
    main()