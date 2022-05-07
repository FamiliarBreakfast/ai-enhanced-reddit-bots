import praw
class Reddit:
	def __init__(self, client_id, client_secret, user_agent, username, password):
		reddit = praw.Reddit(
			client_id=client_id,
			client_secret=client_secret,
			user_agent=user_agent,
			username=username,
			password=password
		)
		self.reddit = reddit

	def get_submissions(self, subreddit, limit=10):
		submissions = self.reddit.subreddit(subreddit).new(limit=limit)
		return submissions