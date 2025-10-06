# Author - one and only gauravdotbhatt
# Dated - 06-10-2025
# quote of the day - go where your heart leads you. (.)=(.)

import requests
from bs4 import BeautifulSoup
import json


def get_headers():
    return {
         "news_obj": {
              "old_hash_id": "sebi-analyst-recommends-buy-on-two-high-flying-chemical-stocks-1759734828432",
              "hash_id": "xlttqg63-1",
              "author_name": "",
              "content": "Two chemical stocks, India Glycols and Pondy Oxides & Chemicals, have seen a stellar run in the last six months, with India Glycols rising over 50% and Pondy Oxides' seeing over 100% rally. Analyst believes that there is more room for rally ahead. Analyst Palak Jain is bullish on these two stocks, driven by strong technicals and fundamental support. ",
              "source_url": "https://stocktwits.com/news-articles/markets/equity/pondy-oxides-india-glycols-eye-further-gains-says-analyst-palak-jain/ch6bDgRR3XK?utm_source=inshorts&utm_medium=referral&utm_campaign=fullarticle",
              "source_name": "Stocktwits",
              "title": "SEBI Analyst recommends buy on two high-flying chemical stocks",
              "important": false,
              "image_url": "https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2025/10_oct/6_mon/img_1759734645984_759.jpg?",
              "shortened_url": "https://shrts.in/folkrz5jh2",
              "created_at": 1759734828000,
              "score": 800,
              "category_names": [
                    "business",
                    "FINANCE"
              ],
              "relevancy_tags": [],
              "tenant": "ENGLISH",
              "fb_object_id": "",
              "fb_like_count": 0,
              "country_code": "IN",
              "impressive_score": 13,
              "targeted_city": [
                    ""
              ],
              "gallery_image_urls": [],
              "full_gallery_urls": [],
              "bottom_headline": "Tap to know more",
              "bottom_text": "Read more here ",
              "darker_fonts": false,
              "bottom_panel_link": "https://stocktwits.com/news-articles/markets/equity/pondy-oxides-india-glycols-eye-further-gains-says-analyst-palak-jain/ch6bDgRR3XK?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts",
              "bottom_type": "DEFAULT",
              "byline_1": [
                    {
                          "type": "TEXT",
                          "text": "swipe left for more at Stocktwits / "
                    },
                    {
                          "type": "TIME"
                    }
              ],
              "byline_2": [
                    {
                          "type": "TEXT",
                          "text": "swipe left for more at Stocktwits / "
                    },
                    {
                          "type": "TIME"
                    }
              ],
              "version": 0,
              "position_start_time": "1970-01-01T00:00:00Z",
              "position_expire_time": "1970-01-01T00:00:00Z",
              "trackers": [],
              "dfp_tags": "score:800,news:default,cat:business,cat:FINANCE,hash:9",
              "dont_show_ad": false,
              "poll_tenant": "ENGLISH",
              "show_inshorts_brand_name": true,
              "crypto_coin_preference": null,
              "is_overlay_supported": false,
              "news_type": "NEWS",
              "is_muted": false,
              "video_audio_type": "USER_SPECIFIED_AUDIO",
              "auto_play_type": "AUTO_PLAY_USER_SPECIFIED",
              "show_in_video_feed_only": false,
              "similar_threshold": 0,
              "is_similar_feed_available": false,
              "publisher_info": {
                    "name": "Stocktwits",
                    "user_id": "bNUIOqdGswRf0mrhElfVMLrnddk2",
                    "user_type": "VENDOR",
                    "profile_image_url": "https://nis-gs.pix.in/public/images/v1/variants/jpg/m/2024/01_jan/5_fri/img_1704466220628_915.jpg",
                    "thumbnail_image_url": "https://nis-gs.pix.in/public/images/v1/variants/jpg/m/2024/01_jan/5_fri/img_1704466220628_915.jpg",
                    "sponsored_text": "",
                    "force_show_interested": false
              },
              "show_publisher_info": false,
              "is_profile_clickable": false,
              "publisher_interaction_meta": {
                    "user_id": "bNUIOqdGswRf0mrhElfVMLrnddk2",
                    "is_publisher_followed": false,
                    "show_follow_button": false
              },
              "capsule_image_url": "",
              "capsule_custom_card_id": "",
              "capsule_custom_card_url": "",
              "capsule_campaign": "",
              "is_youtube_video": null,
              "publishing_status": {},
              "is_market_watch_short": true,
              "publisher_interaction_meta": {
              "user_id": "bNUIOqdGswRf0mrhElfVMLrnddk2",
              "is_publisher_followed": false,
              "show_follow_button": false
        },
        "publishing_status": {}
        }
    }

url = {
    "India" : "https://inshorts.com/api/en/search/trending_topics/india",
    "Business" : "https://inshorts.com/api/en/search/trending_topics/business",
    "Politics" : "https://inshorts.com/api/en/search/trending_topics/politics",
    "Sports" : "https://inshorts.com/api/en/search/trending_topics/sports",
    "Technology" : "https://inshorts.com/api/en/search/trending_topics/technology",
    "Startups" : "https://inshorts.com/api/en/search/trending_topics/startups",
    "Entertainment" : "https://inshorts.com/api/en/search/trending_topics/entertainment",
    "Hatke" : "https://inshorts.com/api/en/search/trending_topics/hatke",
    "International" : "https://inshorts.com/api/en/search/trending_topics/international",
    "Automobile" : "https://inshorts.com/api/en/search/trending_topics/automobile",
    "Science" : "https://inshorts.com/api/en/search/trending_topics/science",
    "Travel" : "https://inshorts.com/api/en/search/trending_topics/travel",
    "Miscellaneous" : "https://inshorts.com/api/en/search/trending_topics/miscellaneous",
    "Fashion" : "https://inshorts.com/api/en/search/trending_topics/fashion",
    "Education" : "https://inshorts.com/api/en/search/trending_topics/education",
    "Health___Fitness" : "https://inshorts.com/api/en/search/trending_topics/Health___Fitness",
}

print("### Checking Api Endpoints Health###")
for category in url.keys():
    print(category, requests.get(url[category]).status_code)

url = url['Business']  #url = 'https://inshorts.com/api/en/search/trending_topics/business'
payload = {'page':'1', 'type':'NEWS_CATEGORY'}
response = requests.get(url, params=payload).json()
data = response['data']['suggested_news']
for i in range(0,10):
    print(i+1, data[i]['news_obj']['content'])
    print("----------------------------")

