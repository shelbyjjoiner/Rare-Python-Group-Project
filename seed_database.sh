
python3 manage.py migrate
python3 manage.py makemigrations rareapi
python3 manage.py migrate rareapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata categories
python3 manage.py loaddata tag
python3 manage.py loaddata comments
python3 manage.py loaddata posts
python3 manage.py loaddata rare_users