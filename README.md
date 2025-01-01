# apnea
Website to keep track of my sleep apnea equipment history.

- Can view website once you unsuspend service - https://apnea.onrender.com
- pip freeze > requirements.txt
- psql -h dpg-ctmrcrrtq21c73fbj3c0-a.virginia-postgres.render.com -U apnea_db_user apnea_db [connect to psql server]
- \l (list databases)
- \c <database_name> (connect to DB)
- \dt (list all tables in current DB)

# TODO
- switch to psql
- now need to do all the parts, and parameterize the functions for each part
- then test everything
- then make bootstrap mobile UI super sexy