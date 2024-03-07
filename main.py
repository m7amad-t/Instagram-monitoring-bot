import time

import requests

# instagram profile module
class InstagramProfile:

    def __init__(self, data):
        user_data = data.get('data', {}).get('user', {})
        self.name = user_data.get('full_name', '')
        self.bio = user_data.get('biography', '')
        self.bio_links = [
            {
                'url': link.get('url', ''),
                'name': link.get('title', '')
            }
            for link in user_data.get('bio_links', [])
        ]
        self.followers_count = user_data.get('edge_followed_by', {}).get('count', 0)
        self.following_count = user_data.get('edge_follow', {}).get('count', 0)
        self.post_count = user_data.get('edge_owner_to_timeline_media', {}).get('count', 0)
        self.is_private = user_data.get('is_private', True)
        self.profile_picture_hd = user_data.get('profile_pic_url_hd', '')

    # method to get External links
    def getLinks(self):
        links = ''
        for link in self.bio_links:
            links += f'\n-  Name : {link["name"] }'
            links += f'\n-  URL : {link["url"]}\n\n'
        return links

    def __str__(self):
        if self.is_private is True:
            isPrivate = '🔒'
        else:
            isPrivate = '🔓'
        links = ''
        for link in self.bio_links:
            links += f'\n-  Name : {link["name"] if len(link["name"])>0 else "(No name)"}'
            links += f'\n-  URL : {link["url"]}\n\n'
        result = f'Name : {self.name}\nProfile Picture URL : \n{self.profile_picture_hd}\n\nBio : {self.bio}\n' \
                 f'\nFollowers :{self.followers_count}\nFollowing : {self.following_count}\nPost : {self.post_count} \n\nAccount Privacy: {isPrivate} \n\nExternal links : \n{links}'
        return result

# todo: Replace BOT_TOKEN, CHAT_ID, USERNAME and HEADERS
# for telegram
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'



# instagram username that you want to monitor :  for endpoint
username = 'INSTAGRAM_USERNAME'

# profile url 
monitored_profile = f'https://www.instagram.com/{username}/'
# URL of the Instagram API endpoint
url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'

#? how to get it : open instagram on your browser and go to someone profile then (Ctrl+Shift+j) go to network section ->
#? then filter the result for XHR files   find that request : https://www.instagram.com/api/v1/users/web_profile_info/?username=_____
#? then copy request headers and use it here ..
# necessary headers (cockies) for endpoint
headers = {
    
}



# send message
def send_message(message):
    try: 
        response = requests.post(
            f'https://api.telegram.org/bot{bot_token}/sendMessage',
            json={'chat_id': chat_id, 'text': message}
        )
        print("Telegram message response code", response.status_code)
        return response
    except:
        print('there was an error occur while sending message!')
        return None


# method for fetching data from the endpoint
def fetch_data():
    print('fetching data')
    try:
        # Make a GET request to the endpoint with the specified headers
        response = requests.get(url, headers=newHeaders)
        if response.status_code == 200:
            return InstagramProfile(response.json())
        else:
            print('There was an error of hitting the endpoint')
            send_message('There was an error while hitting the endpoint!')
            return None
    except:
        send_message('There was an error on requesting!')
        print('There was an error on the request')
        return None

def checkInfo(new_data, old_data):
    print('start checking..')
    result = True
    if new_data is None:
        print('new Data was error')
        result = False
        send_message('new data was none')
        return
    if old_data is None: 
        print('old data was error')
        result = False
        send_message('old data was none')
        return 
    if new_data.name != old_data.name:
        print(f'attention : name have been changed.\n\n{monitored_profile}')
        result = False
        send_message(f'Name changed from : {old_data.name} \tto : {new_data.name}.\n\n{monitored_profile}')
    
    if new_data.bio != old_data.bio:
        print('attention : bio have been changed')
        result = False
        send_message(f'Bio changed from : \n{old_data.bio}\nto : \n{new_data.name}.\n\n{monitored_profile}')
    
    if new_data.followers_count != old_data.followers_count:
        print('attention : followers count have been changed')
        result = False
        send_message(f'Followers count changed from : {old_data.followers_count}\tto : {new_data.followers_count}.\n\n{monitored_profile}')
    
    if new_data.following_count != old_data.following_count:
        print('attention : following count have been changed')
        result = False
        send_message(f'Following count changed from : {old_data.following_count}\tto : {new_data.following_count}.\n\n{monitored_profile}')
    
    if new_data.post_count != old_data.post_count:
        print('attention : post count have been changed')
        result = False
        send_message(f'Post count changed from : {old_data.post_count}\tto : {new_data.post_count}.\n\n{monitored_profile}')
    
    if new_data.is_private != old_data.is_private:
        isPrivate = '🔒'
        if old_data.is_private:
            isPrivate = '🔓'
        print('attention : account privacy have been changed')
        result = False
        send_message(f'Account privacy changed!\n Now its : {isPrivate}.\n\n{monitored_profile}')
    
    if new_data.profile_picture_hd != old_data.profile_picture_hd:
        print('attention : profile pictuer have been changed')
        result = False
        send_message(f'Profile Picture is changed to  :\n{new_data.profile_picture_hd}\n\nold one is :\n{old_data.profile_picture_hd}.\n\n{monitored_profile}')
    
    if new_data.getLinks() != old_data.getLinks():
        print('attention : Extrnal links have been changed')
        result = False
        send_message(f'External Links have been updated  from :\n{old_data.getLinks()}\nto :\n{new_data.getLinks()}.\n\n{monitored_profile}')
    return result


def main():
    counter = 0
    old_data = fetch_data()
    # first when the bot is run send the message : 
    send_message(f'--       The bot is now acctivate        --\n{old_data.__str__()}')
    
    print(counter)
    while True:
        data = fetch_data()
        checking_result = checkInfo(data, old_data) 
        if checking_result is False:
            old_data = data
        if counter == 3: 
            send_message(f'--\t\t           3 Hourly Checking           \t\t--\n{data.__str__()}')
            print('3 hourly message was sent')
            counter = 0
    
        print('sleep 1 hour')
        counter += 1
        time.sleep(3600)




if __name__ == "__main__":
    main()
