import requests
import json
import csv

# Replace ACCESS_TOKEN with the generated access token
ACCESS_TOKEN = "EAANmjqga4McBALpNRsqZBNTG6fDxppVPlHQWton0EocVasZCUqebjTyrilUwZB8Ky1T86ALrKcV4eTR9gv0uqTwNYOIDnn6efcVo33CEWpvie3wsy22tJXPmcA6QFAJv4QYGZCsmPMvawUHtnVP8MZCrpdklsT8SafOFc8e4XtQmCNiYN1D0XG2Apc12Qb58dKfPm9xZCMvwZDZD"

# Endpoint for user location
location_endpoint = "https://graph.facebook.com/me?fields=location&access_token=" + ACCESS_TOKEN
location_response = requests.get(location_endpoint)
location_data = location_response.json()

# Endpoint for user likes
likes_endpoint = "https://graph.facebook.com/me?fields=likes&access_token=" + ACCESS_TOKEN
likes_response = requests.get(likes_endpoint)
likes_data = likes_response.json()

# Endpoint for user friends
friends_endpoint = "https://graph.facebook.com/me?fields=friends&access_token=" + ACCESS_TOKEN
friends_response = requests.get(friends_endpoint)
friends_data = friends_response.json()

# Endpoint for user posts
posts_endpoint = "https://graph.facebook.com/me?fields=posts&access_token=" + ACCESS_TOKEN
posts_response = requests.get(posts_endpoint)
posts_data = posts_response.json()

# Endpoint for user gender
gender_endpoint = "https://graph.facebook.com/me?fields=gender&access_token=" + ACCESS_TOKEN
gender_response = requests.get(gender_endpoint)
gender_data = gender_response.json()

# Create a dictionary to store the data
data = {}
data['location'] = location_data
data['likes'] = likes_data
data['friends'] = friends_data
data['posts'] = posts_data
data['gender'] = gender_data

# Write the data to a CSV file
with open('facebook_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['location', 'likes', 'friends', 'posts', 'gender'])
    writer.writerow([location_data, likes_data, friends_data, posts_data, gender_data])

print("Data written to facebook_data.csv")

# Write the data to a JSON file
with open('facebook_data.json', 'w') as file:
    json.dump(data, file)

#Save the Facebook API response for location to a CSV file
#location
print("Data written to facebook_data.json")
with open("location.csv", "w", newline="") as location_file:
 writer = csv.writer(location_file)
 writer.writerow(["Location"])
try:
    location_name = location_data["location"]["name"]
except KeyError:
    location_name = ''

writer.writerow([location_name])
#friends
with open("friends.csv", "w", newline="") as friends_file:
 writer = csv.writer(friends_file)
 writer.writerow(["Friends"])
for friend in friends_data["friends"]["data"]:
 writer.writerow([friend["name"]])
#post
with open("posts.csv", "w", newline="") as posts_file:
 writer = csv.writer(posts_file)
 writer.writerow(["Posts"])
for post in posts_data.get('posts', {}).get('data', []):
    if 'message' in post:
         writer.writerow([post['message']])
for post in posts_data["posts"]["data"]:
    if "message" in post:
        writer.writerow([post['message']])
        writer.writerow([post["message"]])
#gender
with open("gender.csv", "w", newline="") as gender_file:
 writer = csv.writer(gender_file)
 writer.writerow(["Gender"])
 writer.writerow([gender_data["gender"]])

print("Data written to location.csv, likes.csv, friends.csv, posts.csv and gender.csv")
