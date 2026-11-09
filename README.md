# Favorite-Car-Brand-Poll

## Running the website

Run the app with Flask from the project folder:

```powershell
python -m flask --app app run
```

The first time the app starts, it creates `instance/votes.db`. Votes are saved
in that SQLite database file, so they are still there after you stop and restart
the app on the same computer. The `instance` folder is ignored by Git so the
database is not uploaded as part of the source code.

Open `/form1nico` to vote and `/admin` to see the vote totals. The results page
is currently public and does not require an admin password.
