The howto_run.md file describes the steps to run the P2P Dashboard locally, including setting up both the FastAPI backend and the Streamlit frontend. It explains how to create a virtual environment, install dependencies, configure the database and secret key, and run the backend server.

Crucially, Part 2 details the process for creating a user and generating an API key using the backend's interactive documentation (Swagger UI). This involves:

Accessing the /docs endpoint of the running backend.
Using the POST /admin/users/ endpoint to create a new user with a username and password.
Using the POST /admin/token endpoint with the created username and password to obtain an access token.
Authorizing the session in the Swagger UI using the obtained access token (prefixed with Bearer ).
Using the POST /admin/keys/ endpoint to generate an API key for the authorized user, providing a name for the key.
Saving the generated API key securely as it will not be shown again.


the question is, why after creating user admin generating keys, es decir porque despues de hacer el proceso esta se reinicia, donde se almacena, en postgresql?

Gemini
Based on the howto_run.md file, when you run the application locally using the provided instructions, the database used is a file-based SQLite database specified by the DATABASE_URL="sqlite:///./p2p_dashboard.db" line in the .env file.

This means that the user information (like the 'admin' user you created) and the generated API keys are stored within the p2p_dashboard.db file in your project's root directory.

The document doesn't mention PostgreSQL at all. So, if you are seeing the user and keys disappear after restarting, it is likely due to something related to the SQLite database file. This could happen if:

The p2p_dashboard.db file is being deleted or moved.
There's an issue with how the application is writing to or reading from the database file upon restart.
The virtual environment is not properly activated when running the backend, leading to the application not finding the correct database file.
To investigate further, you could:

Check if the p2p_dashboard.db file exists in your project's root directory after you've created a user and key.
See if the file is still there after you restart the backend.
Ensure you are activating the correct backend virtual environment before running the uvicorn command.
The document doesn't describe a setup that uses PostgreSQL, so the data is not being stored there in this local setup.