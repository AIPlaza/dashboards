GitGuardian has detected the following PostgreSQL URI exposed within your GitHub account.
Details

- Secret type: PostgreSQL URI

- Repository: AIPlaza/dashboards

- Pushed date: July 28th 2025, 15:40:47 UTC

Fix this secret leak
Mark as false positive


Run python -m pytest
ImportError while loading conftest '/home/runner/work/dashboards/dashboards/tests/conftest.py'.
tests/conftest.py:12: in <module>
    from p2p_api.main import app, get_db, get_api_key, configure_database
p2p_api/main.py:11: in <module>
    from . import (
p2p_api/crud.py:27: in <module>
    def finalize_run(db: Session, run_id: int, total_offers: int | None = None, error_message: str | None = None):
E   TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'
Error: Process completed with exit code 4.

Before you begin, it is CRITICAL to back up your repository. You can simply duplicate your
  C:\Users\DELL\P2P-Dashboard folder to C:\Users\DELL\P2P-Dashboard_backup or similar.

  ---

  Instructions to Remove `DATABASE_URL` from Git History

  We will use git filter-repo for this. If you don't have it installed, you might need to install it first. You 
  can usually install it via pip:
   1 pip install git-filter-repo
  (You might need to add git-filter-repo to your system's PATH if it's not found after installation.)

  Once `git-filter-repo` is installed, follow these steps:

   1. Navigate to your repository:
      Open your terminal or command prompt and change your directory to your project's root:
   1     cd C:\Users\DELL\P2P-Dashboard

   2. Ensure you are on the `production` branch:
   1     git checkout production

   3. Run `git filter-repo` to remove the `DATABASE_URL` from all files in your history:

      Important: You need to replace <YOUR_ACTUAL_DATABASE_URL_VALUE> with the exact sensitive string that was  
  committed. This is the full value of your DATABASE_URL environment variable, including postgresql://,
  username, password, host, port, and database name.

   1     git filter-repo --path .env --replace-text
     '<YOUR_ACTUAL_DATABASE_URL_VALUE>==REDACTED_DATABASE_URL'

       * Example: If your .env file contained DATABASE_URL=postgresql://user:pass@host:5432/mydb, then
         <YOUR_ACTUAL_DATABASE_URL_VALUE> should be postgresql://user:pass@host:5432/mydb.

   4. Force push the rewritten history:
      After git filter-repo completes, your local history will be rewritten. You must force push to update the  
  remote repository.

   1     git push origin production --force
      Note: If others are collaborating on this branch, they will need to rebase their work on top of the new   
  history.

  ---

  Once you have successfully completed these steps and confirmed that the sensitive information is no longer    
  visible in your GitHub repository's history (check the commit history on GitHub), please inform me.
