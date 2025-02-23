import requests
import time
from pystyle import Colors, Colorate

def main():
 
 usernames = []
 epicid = []
 sites = ["https://github.com/", "https://soundcloud.com/", "https://steam.com"]
 pfps = []
 emails = []
 URL = "https://api.proswapper.xyz"

 print(Colorate.Horizontal(Colors.white_to_black, """
░█████╗░░██╗░░░░░░░██╗███╗░░██╗░██████╗███████╗░█████╗░
██╔══██╗░██║░░██╗░░██║████╗░██║██╔════╝██╔════╝██╔══██╗
██║░░██║░╚██╗████╗██╔╝██╔██╗██║╚█████╗░█████╗░░██║░░╚═╝
██║░░██║░░████╔═████║░██║╚████║░╚═══██╗██╔══╝░░██║░░██╗
╚█████╔╝░░╚██╔╝░╚██╔╝░██║░░███║██████╔╝███████╗╚█████╔╝
░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚═════╝░╚══════╝░╚════╝░"""))
 user = input(Colorate.Horizontal(Colors.white_to_black, "Username: "))
 NEWURL = URL + "/external/name/" + user
 response = requests.request("GET", NEWURL, timeout=10)
 result = response.json()
 if len(result) == 0:
    print("No account found")
 else:
   if len(result[0]["externalAuths"].items()) == 0:
     print("No external auths found")
   else:
     displayName = result[0]["displayName"]
     accountId = result[0]["id"]

     if "nintendo" in result[0]["externalAuths"]:
       nintendoid = result[0]["externalAuths"]["nintendo"]["accountId"]
       print(Colorate.Horizontal(Colors.white_to_black, f"Nintendo Account Id: {nintendoid}"))
     if "xbl" in result[0]["externalAuths"]:
       xboxuser = result[0]["externalAuths"]["xbl"]["externalDisplayName"]
       print(Colorate.Horizontal(Colors.white_to_black, f"Xbox Username: {xboxuser}"))
       usernames.append(xboxuser)
     if "psn" in result[0]["externalAuths"]:
       psnuser = result[0]["externalAuths"]["psn"]["externalDisplayName"]
       print(Colorate.Horizontal(Colors.white_to_black, f"PSN Username: {psnuser}"))
       usernames.append(psnuser)
     if "steam" in result[0]["externalAuths"]:
       steamuser = result[0]["externalAuths"]["steam"]["externalDisplayName"]
       steamid = result[0]["externalAuths"]["steam"]["id"]
       print(Colorate.Horizontal(Colors.white_to_black, f"steam username: "))
       usernames.append(steamuser)
     else:
       steamid = "1"
     

     epicid.append(accountId)
     usernames.append(displayName)
     
     for name in usernames:
      for platform in platforms:
        [] # to be continued

     for site in sites:
      for name in usernames:
        if site == "https://steam.com":
          if len(steamid) > 2:
           response = requests.get(f'https://api.findsteamid.com/steam/api/summary/{steamid}', headers=headers)
           print("Avatar: " + response.json()["avatar"])
           print("realname: " + response.json()["realname"])
           print("steamid: " + response.json()["steamid"])
           print("timecreated: " + response.json()["timecreated"])
           print("Country Code: " + response.json()["loccountrycode"])
           print("profileurl: " + response.json()["profileurl"])

        if site == "https://github.com/":
         headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}
         response = requests.get(f'https://api.github.com/users/{name}', headers=headers)
         if response.status_code == 200:
          print(response.json())
          avatar = response.json()["avatar_url"]
          gname = response.json()["name"]
          gemail = response.json()["email"]

          usernames.append(gname)
          pfps.append(avatar)
          emails.append(gemail)
         else:
          response = requests.get(site + name)
          if response.status_code == 200:
           print(f'{site}{name}')


   

main()
