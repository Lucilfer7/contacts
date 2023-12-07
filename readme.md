# Google Contacts Phone Numbers Extractor

## Description

This Python script utilizes the Google Contacts API to retrieve and save phone numbers from your Google Contacts. It authenticates the application using OAuth 2.0, accesses the user's contact list, and extracts phone numbers along with associated names. The script then saves this information to a text file for further use.

## Key Components

### 1. API Configuration:

The script is configured with the necessary parameters for accessing the Google Contacts API, including the API service name, version, and the path to the client secret file obtained from the Google Developers Console.

### 2. Output Directory:

The script specifies a directory where the output text file containing phone numbers will be saved. If the directory does not exist, it is created.

### 3. Authentication:

The `authenticate_and_get_service` function handles the OAuth 2.0 authentication process using the `google_auth_oauthlib` library. It obtains the necessary credentials to access the Google Contacts API.

### 4. Data Retrieval and Saving:

The `save_phone_numbers` function utilizes the authenticated service to fetch contact information, focusing on names and phone numbers. The obtained data is then formatted and saved to a text file in the specified output directory.

### 5. Execution:

The script executes the authentication process and data retrieval, providing feedback on the saved file's location.

## Usage

1. **Before running the script, ensure that the `google-auth`, `google-auth-oauthlib`, and `google-api-python-client` libraries are installed.**

   ```bash
   pip install google-auth google-auth-oauthlib google-api-python-client
   ```

2. **Obtain the `client_secret.json` file from the Google Developers Console and place it in the script's directory.**

3. **Run the script, and it will guide you through the `OAuth 2.0 authentication process`, fetch contact information, and save phone numbers to a text file.**

## Note

Ensure that you handle sensitive information, such as the `client_secret.json` file, securely, and consider appropriate security measures when using and sharing the script.
