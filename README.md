# serial-number-sheets-automation

## Enable Google Sheets API
1. ### Sign in to the Google Cloud Console
*item
  - Go to https://console.cloud.google.com/.
  - Sign in with your Google account or create one if you don't have it.
2. ### Create a New Project
  - Click on the project dropdown in the upper-left corner.
  - Click on the "New Project" button.
  - Give your project a name and click "Create."
3. ### Enable the Google Sheets API

In the Google Cloud Console, click on "APIs & Services" in the left-hand menu.
Click on "Dashboard."
Click the "+ ENABLE APIS AND SERVICES" button at the top.
Search for and Select Google Sheets API

In the search bar, type "Google Sheets API" and press Enter.
Click on the "Google Sheets API" result.
Enable the API

Click the "Enable" button.
Create Credentials

After enabling the API, click the "Create credentials" button.
Choose "OAuth client ID."
Configure OAuth consent screen

If prompted, select "Web application" as the application type.
Enter a name for your OAuth consent screen.
Under "Authorized domains," add the domain of your application (if applicable).
Fill out other required fields as necessary.
Click "Save."
Create OAuth Client ID

On the "Create OAuth client ID" page, choose "Web application" as the application type.
Under "Authorized JavaScript origins," add the origin URLs for your application (e.g., http://localhost:8080 for local development).
Under "Authorized redirect URIs," add the callback URL for your application (e.g., http://localhost:8080/callback).
Click "Create."
Download Credentials

After creating the OAuth client ID, you'll see a screen with your client ID and client secret.
Click the "Download" button to download the credentials as a JSON file. Keep this file secure; you'll need it to authenticate with the Google Sheets API.
Use the Google Sheets API

You can now use the downloaded credentials to authenticate your application and make requests to the Google Sheets API. Refer to the Google Sheets API documentation and the language-specific libraries or tools you are using for further instructions on how to interact with the API.
