# -*- coding: utf-8 -*-
import twitter


def main() ->None:
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_TOKEN_KEY = ""
    ACCESS_TOKEN_SECRET = ""
    auth = twitter.OAuth(consumer_key=CONSUMER_KEY,
                         consumer_secret=CONSUMER_SECRET,
                         token=ACCESS_TOKEN_KEY,
                         token_secret=ACCESS_TOKEN_SECRET)
    t = twitter.Twitter(auth=auth)
    response = t.statuses.home_timeline()
    print(response)


if __name__ == "__main__":
    main()
