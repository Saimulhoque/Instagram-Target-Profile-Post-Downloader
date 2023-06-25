import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to Instagram (optional)
loader.login('your username' , 'password')

# Function to filter and download videos
def download_videos(post):
    if post.is_video:
        loader.download_post(post, target='#videos')

# Download posts by a specific user
username = 'Target Account Username'
profile = instaloader.Profile.from_username(loader.context, username)
loader.download_profile(profile, download_videos)


# Download videos from your feed
loader.download_feed(target='#videos', filter_posts=lambda post: post.is_video)

# Logout (optional)
loader.logout()