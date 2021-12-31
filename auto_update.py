import feedparser

hyemi_blog_rss_url = "https://ohhyemi.github.io/index.xml"
rss_feed = feedparser.parse(hyemi_blog_rss_url)

MAX_POST_NUM = 6

latest_blog_post_list = ""

for idx, feed in enumerate(rss_feed['entries']):
    if(idx > MAX_POST_NUM):
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"

markdown_text = """![waving](https://capsule-render.vercel.app/api?type=waving&height=200&text=Hyemi%20Oh&fontAlign=80&fontAlignY=40&color=gradient)

<h3 align="center">🛠 Tech Stack 🛠</h3>

<p align="center">Tech's that I've used at least once</p>

<p align="center">
  <img src="https://img.shields.io/badge/C++-00599C?&logo=C%2B%2B&logoColor=white">&nbsp 
  <img src="https://img.shields.io/badge/-C%23-F89B00?logo=Csharp&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/-Unity-2E2627?logo=Unity&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/git-FF9900?logo=git&logoColor=white"/>&nbsp
  <br>
  <img src="https://img.shields.io/badge/css-1572B6?logo=css3&logoColor=white"/>&nbsp
  <img src="https://img.shields.io/badge/-HTML5-FF5733?logo=HTML5&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/-hugo-2FBB92?logo=hugo&logoColor=white">&nbsp
</p>

<br>
<br>

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=defianz&layout=compact&theme=omni)![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=defianz&show_icons=true&theme=omni)

<br>
<br>

## 📃 Problem Solving (a.k.a Algorithm)

- Baekjoon Online Judge: [gpal1014](https://www.acmicpc.net/user/gpal1014)
- Solved.ac: [gpal1014](https://solved.ac/profile/gpal1014)

<p align="center">
  <a href="https://solved.ac/profile/gpal1014"><img src="https://github-readme-solvedac-hyp3rflow.vercel.app/api/?handle=gpal1014"></a><br>
</p>

<br>

## 💻 <a href="https://ohhyemi.github.io/"> Tech Blog </a>
📔Recently Posted...
<br>
"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

print(readme_text)

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
