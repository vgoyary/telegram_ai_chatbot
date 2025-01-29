import urllib.parse

username = "vileenagoyary02"
password = "Vil098!@#"

encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)

mongo_uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.33efe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

print(mongo_uri)
