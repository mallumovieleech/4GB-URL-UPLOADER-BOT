import os, time, datetime,



class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7945308877:AAEImD7zmngAKeF554rG0Cqf0sU9R5FD26o")
    
    API_ID = int(os.environ.get("API_ID", "23858762"))
    
    API_HASH = os.environ.get("API_HASH", "d4d6e9a9e553759e45f59c2e74c8f809")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    SESSION_STRING = os.environ.get("SESSION_STRING", "BQFsDkoAkHUUZ0VYWv2zbVS03LrzePXg5U0mpwaIbXZQdXJhjHuDZVNz6X6SYVG1xpIYXm5SPyB8X5TZ45PpJdXEf3HEEhMyeXR5KneaWWQ6ZniX7DjSnE5YHkwR3V90sFC2OcWiuH3qDhr8pUSVkrJE6sGaDrhRZrCFpClPdhpJgpGRRntGwYSvFs4nBYsVb8oCu-avva6ff3-WKB4yV1jkmLHr5rt0QZ38K0sMkDtwbzrY4Dfg57XYWFMNsIp5guusWVKmPoos5FWI_jBQ5cjBLnH3Sa6GIrllxm8j2nS9YDCsINvr2IXLsvXmVZPmuV-4GEkYwO5fN5zC4FKIp-EhZxiJawAAAAHnBYTeAA")

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://damon:damon@cluster0.dxbn6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "LinkToFileUploaderBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002386764735"))
    
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "561339410"))

    AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "561339410").split(" ")]
    
  
