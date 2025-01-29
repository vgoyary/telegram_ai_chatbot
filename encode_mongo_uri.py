import urllib.parse

username = "vileenagoyary02"  # Your MongoDB username
password = "Vil098!@#"         # Your MongoDB password

# URL-encode the username and password
encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)

# Construct the MongoDB URI
mongo_uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.33efe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

print(mongo_uri)  # Print the encoded URI
