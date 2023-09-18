# serial-number-sheets-automation
***

### Enable Google Sheets API

1. **Sign in to the Google Cloud Console**
   - Go to [https://console.cloud.google.com/](https://console.cloud.google.com/).
   - Sign in with your Google account or create one if you don't have it.

2. **Create a New Project**
   - Click on the project dropdown in the upper-left corner.
   - Click on the "New Project" button.
   - Give your project a name and click "Create."

3. **Enable the Google Sheets API**
   - In the Google Cloud Console, click on "APIs & Services" in the left-hand menu.
   - Click on "Dashboard."
   - Click the "+ ENABLE APIS AND SERVICES" button at the top.

4. **Search for and Select Google Sheets API**
   - In the search bar, type "Google Sheets API" and press Enter.
   - Click on the "Google Sheets API" result.

5. **Enable the API**
   - Click the "Enable" button.

6. **Create Credentials**
   - After enabling the API, click the "Create credentials" button.
   - Choose "OAuth client ID."

7. **Configure OAuth consent screen**
   - If prompted, select "Web application" as the application type.
   - Enter a name for your OAuth consent screen.
   - Under "Authorized domains," add the domain of your application (if applicable).
   - Fill out other required fields as necessary.
   - Click "Save."

8. **Create OAuth Client ID**
   - On the "Create OAuth client ID" page, choose "Web application" as the application type.
   - Under "Authorized JavaScript origins," add the origin URLs for your application (e.g., `http://localhost:8080` for local development).
   - Under "Authorized redirect URIs," add the callback URL for your application (e.g., `http://localhost:8080/callback`).
   - Click "Create."

9. **Download Credentials**
   - After creating the OAuth client ID, you'll see a screen with your client ID and client secret.
   - Click the "Download" button to download the credentials as a JSON file.

### Using Sheets Automation File
1. **Create a Project Directory**
   - Create a new folder for your project. You can name it whatever you like.

3. **Save Credentials**
   - Place this `credentials.json` file in the project folder you created in step 1.

6. **Define SPREADSHEET_ID Variable**
   - Locate the line in your script where you want to define the `SPREADSHEET_ID` variable (e.g., line 11).

7. **Copy Spreadsheet ID**
   - Go to Google Sheets and find the spreadsheet you want to work with.
   - Copy the unique identifier from the URL, which looks like this: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit`.
   - Paste this ID as the value of the `SPREADSHEET_ID` variable in your Python script. For example:
     ```python
     SPREADSHEET_ID = "your-spreadsheet-id-here"
     ```
