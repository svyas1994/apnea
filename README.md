# apnea
Website to keep track of my sleep apnea equipment history.

- Can view website once you unsuspend service - https://apnea.onrender.com
- pip freeze > requirements.txt
- psql -h dpg-ctmrcrrtq21c73fbj3c0-a.virginia-postgres.render.com -U apnea_db_user apnea_db [connect to psql server]
- \l (list databases)
- \c <database_name> (connect to DB)
- \dt (list all tables in current DB)
- https://blog.gitguardian.com/secrets-api-management/?utm_source=product&utm_medium=product&utm_campaign=white_knight_v2

# TODO
- I want to create a get_timestamp() fuunction that pulls the latest max(timestamp)
record of a specific value in ONE column. This function should refresh at either
page refresh or whenever data is inserted in the database.