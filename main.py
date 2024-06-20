import time

import requests


from PIL import Image
from io import BytesIO

# instagram profile module
class InstagramProfile:

    def __init__(self, data):
        user_data = data.get("data", {}).get("user", {})
        self.name = user_data.get("full_name", "")
        self.bio = user_data.get("biography", "")
        self.bio_links = [
            {"url": link.get("url", ""), "name": link.get("title", "")}
            for link in user_data.get("bio_links", [])
        ]
        self.followers_count = user_data.get("edge_followed_by", {}).get("count", 0)
        self.following_count = user_data.get("edge_follow", {}).get("count", 0)
        self.post_count = user_data.get("edge_owner_to_timeline_media", {}).get(
            "count", 0
        )
        self.is_private = user_data.get("is_private", True)
        self.profile_picture_hd = user_data.get("profile_pic_url_hd", "")

    # method to get External links
    def getLinks(self):
        links = ""
        for link in self.bio_links:
            links += f'\n-  Name : {link["name"] }'
            links += f'\n-  URL : {link["url"]}\n\n'
        return links

    def __str__(self):
        if self.is_private is True:
            isPrivate = "🔒"
        else:
            isPrivate = "🔓"
        links = ""
        for link in self.bio_links:
            links += (
                f'\n-  Name : {link["name"] if len(link["name"])>0 else "(No name)"}'
            )
            links += f'\n-  URL : {link["url"]}\n\n'
        result = (
            f"Name : {self.name}\nProfile Picture URL : \n{self.profile_picture_hd}\n\nBio : {self.bio}\n"
            f"\nFollowers :{self.followers_count}\nFollowing : {self.following_count}\nPost : {self.post_count} \n\nAccount Privacy: {isPrivate} \n\nExternal links : \n{links}"
        )
        return result


def fetch_image(url):
   try:
       response = requests.get(url)
       response.raise_for_status()  # Raise an HTTPError for bad responses
       image = Image.open(BytesIO(response.content))
       return image      
   except requests.exceptions.RequestException as e:
       print(f"Error fetching image from URL: {url}\nException: {e}")
       send_message('error fetching image from URL')
       return None
   
def image_checker(img1 , img2)   :
    return list(img1.getdata()) == list(img2.getdata())
   
   
def check_images(oldURL , newURL):
    image = fetch_image(oldURL)
    image2 = fetch_image(newURL)
    if not image :
        send_message('Fiald to load old image ')
        return False  
    if not image2 :
        send_message('Fiald to load new image ')
        return False
    
    res = image_checker(image , image2)
    return res 
   
# todo: Replace BOT_TOKEN, CHAT_ID, USERNAME and HEADERS
# for telegram
bot_token = "6780109825:AAHK09h0UrteD01ua0NWFHdKW2OOyqZsfos"
chat_id = "1959645938"


# instagram username that you want to monitor :  for endpoint
username = "rosieberosses"



# necessary headers (cockies) for endpoint


newHeaders = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.6',
    'Cookie': 'ig_did=0C826C21-17C3-444A-ABB7-EBABD37214D7; dpr=1.25; ps_l=0; ps_n=0; mid=Zdn36QALAAEqyJz_3AUlfFs99nTT; datr=DPjZZSkw2lw5o4-RoWWaoglQ; csrftoken=pQiCZ2XqZiiUa7ZPWdUXUZtv8EVuECc2; ds_user_id=65148761839; sessionid=65148761839%3Au9CEtqxE2TuIvk%3A29%3AAYdG7ppiuI7UTS_STJRJmdNQb3qncIqbdK4ThF-fIA; rur="LDC\05465148761839\0541740320991:01f7e21808f28f1cfb433f66fffa031c2582db858cce44a2582dd6b75532e526a4e6c16f"',
    'Referer': 'https://www.instagram.com/rosieberosses/',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Model': '""',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Gpc': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Asbd-Id': '129477',
    'X-Csrftoken': 'pQiCZ2XqZiiUa7ZPWdUXUZtv8EVuECc2',
    'X-Ig-App-Id': '936619743392459',
    'X-Ig-Www-Claim': 'hmac.AR3bYKYFG-5DhUWwDxQrfpAFZhjcBskaxmGhB7_Pty-dNa0f',
    'X-Requested-With': 'XMLHttpRequest'
}

# profile url
monitored_profile = f"https://www.instagram.com/{username}/"
# URL of the Instagram API endpoint
url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"


# send message
def send_message(message):
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            json={"chat_id": chat_id, "text": message},
        )
        print("Telegram message response code", response.status_code)
        return response
    except:
        print("there was an error occur while sending message!")
        return None


# method for fetching data from the endpoint
def fetch_data():
    print("fetching data")
    try:
        # Make a GET request to the endpoint with the specified headers
        response = requests.get(url, headers=newHeaders)
        if response.status_code == 200:
            return InstagramProfile(response.json())
        else:
            print("There was an error of hitting the endpoint")
            send_message("There was an error while hitting the endpoint!")
            return None
    except:
        send_message("There was an error on requesting!")
        print("There was an error on the request")
        return None


def checkInfo(new_data, old_data):
    print("start checking..")
    result = True
    if new_data is None:
        print("new Data was error")
        result = False
        send_message("new data was none")
        return
    if old_data is None:
        print("old data was error")
        result = False
        send_message("old data was none")
        return
    if new_data.name != old_data.name:
        print(f"attention : name have been changed.\n\n{monitored_profile}")
        result = False
        send_message(
            f"Name changed from : {old_data.name} \tto : {new_data.name}.\n\n{monitored_profile}"
        )

    if new_data.bio != old_data.bio:
        print("attention : bio have been changed")
        result = False
        send_message(
            f"Bio changed from : \n{old_data.bio}\nto : \n{new_data.name}.\n\n{monitored_profile}"
        )

    if new_data.followers_count != old_data.followers_count:
        print("attention : followers count have been changed")
        result = False
        send_message(
            f"Followers count changed from : {old_data.followers_count}\tto : {new_data.followers_count}.\n\n{monitored_profile}"
        )

    if new_data.following_count != old_data.following_count:
        print("attention : following count have been changed")
        result = False
        send_message(
            f"Following count changed from : {old_data.following_count}\tto : {new_data.following_count}.\n\n{monitored_profile}"
        )

    if new_data.post_count != old_data.post_count:
        print("attention : post count have been changed")
        result = False
        send_message(
            f"Post count changed from : {old_data.post_count}\tto : {new_data.post_count}.\n\n{monitored_profile}"
        )

    if new_data.is_private != old_data.is_private:
        isPrivate = "🔒"
        if old_data.is_private:
            isPrivate = "🔓"
        print("attention : account privacy have been changed")
        result = False
        send_message(
            f"Account privacy changed!\n Now its : {isPrivate}.\n\n{monitored_profile}"
        )

    if new_data.profile_picture_hd != old_data.profile_picture_hd:
        
        imageNotChanged = check_images(old_data.profile_picture_hd  , new_data.profile_picture_hd)
        if imageNotChanged : 
            print("attention : profile pictuer have been changed")
            result = False
            send_message(
                f"Profile Picture is changed to  :\n{new_data.profile_picture_hd}\n\nold one is :\n{old_data.profile_picture_hd}.\n\n{monitored_profile}"
            )    
        

    if new_data.getLinks() != old_data.getLinks():
        print("attention : Extrnal links have been changed")
        result = False
        send_message(
            f"External Links have been updated  from :\n{old_data.getLinks()}\nto :\n{new_data.getLinks()}.\n\n{monitored_profile}"
        )
    return result


def main():
    counter = 0
    old_data = fetch_data()
    # first when the bot is run send the message :
    send_message(f"--       The bot is now acctivate        --\n{old_data.__str__()}")

    print(counter)
    while True:
        data = fetch_data()
        checking_result = checkInfo(data, old_data)
        if checking_result is False:
            old_data = data
        if counter == 3:
            send_message(
                f"--\t\t           3 Hourly Checking           \t\t--\n{data.__str__()}"
            )
            print("3 hourly message was sent")
            counter = 0

        print("sleep 1 hour")
        counter += 1
        time.sleep(3600)


if __name__ == "__main__":
    main()
