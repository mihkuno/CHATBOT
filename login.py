from main import EchoBot
import json

cookies = {}
try:
    # Load the session cookies
    with open('session.json', 'r') as f:
        cookies = json.load(f)
except:
    # If it fails, never mind, we'll just login again
    pass

# Attempt a login with the session, and if it fails, just use the email & password

# bugo ko
# client = EchoBot('caindayjoenin@yahoo.com.ph', 'letsplayminecraft098', session_cookies=cookies)
#main account (locked)
#client = EchoBot('caindayjoeninyo@gmail.com', 'min@toChan321', session_cookies=cookies)
#main account (locked)
client = EchoBot('caindayjoeninyo@gmail.com', 't@n@k@San321', session_cookies=cookies)

# dummy account
#client = EchoBot('09353787332', 'letspokemongo123', session_cookies=cookies)

# Save the session again
with open('session.json', 'w') as f:
    json.dump(client.getSession(), f)

#keep the client on for listening fetched message     
# #it acts like a loop()
client.listen()