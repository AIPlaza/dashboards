import os

def replace_sensitive_data(blob):
    # Define the exact sensitive string to find
    sensitive_string = b'DATABASE_URL="postgresql://p2p_dashboard_user:4scr5XwawprE0cHtx7TJe6w8F7e994q5@dpg-d1omv9ffte5s73bhth20-a.oregon-postgres.render.com/p2p_dashboard"'
    # Define the replacement string
    replacement_string = b'DATABASE_URL="REDACTED_DATABASE_URL"'

    # Only process if the sensitive string is found in the blob content
    if sensitive_string in blob.data:
        blob.data = blob.data.replace(sensitive_string, replacement_string)
    return blob

# This function will be called by git-filter-repo for each blob
def filter_blob(blob):
    # Only apply the filter to the .env file
    if blob.original_path == b'.env':
        return replace_sensitive_data(blob)
    return blob

# git-filter-repo expects a filter_blob function
# or filter_commit, filter_tag etc.
# We're using filter_blob here.
__all__ = ['filter_blob']