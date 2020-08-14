import json

with open("../keys.json", 'r') as cred_file:
    loaded_dict = json.load(cred_file)

DEBUG = True
SECRET_LEY = loaded_dict["SECRET_KEY"]
DB_NAME = "copypaster_db"
DB_HOST = loaded_dict["DB_HOST"]
DB_PORT = loaded_dict["DB_PORT"]
DB_USER = loaded_dict["DB_USER"]
DB_PASSWORD = loaded_dict["DB_PASSWORD"]

POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"