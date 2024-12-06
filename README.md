# Edit_Google_Sheets_Example

This is an example repository for activities that involve editing files that are hosted on Google Drive using a simple python script.

## Activating the API's

For this example, it will be necessary to activate two APIs in the Google Cloud Console.

```
    - Google Sheets API
    - Google Drive API
```

After activation, you will need to create a credential for access:

- Go to "Credentials" and click "Create credentials".
- Choose "Service Account".
- After creating, download the private key JSON file for authentication.

***Don't forget to share the spreadsheet with the email provided after creating the credential.***

## Coding

Before starting, you will need to install the "gspread" library, which will enable authentication and editing of the spreadsheet.

```
   $ pip install gspread google-auth
```

After installing, just make the necessary changes to the code **(mainly changing the name of the spreadsheet and the .json of credentials)** and have fun editing the spreadsheet.