import json
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import time

# قراءة الملف الحالي
with open("database/witanime.json", "r", encoding="utf-8") as file:
    current_data = json.load(file)

links = "https://witanime.com/anime-status/%d9%8a%d8%b9%d8%b1%d8%b6-%d8%a7%d9%84%d8%a7%d9%86/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# استمرار التعديل على الملف
request = Request(links, headers=headers)
response = urlopen(request)
html = response.read()
response.close()
time.sleep(1)
soup = bs(html, "html.parser")
c = soup.find_all(
    "div",
    {
        "class": "col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"
    },
)

data = []

for i in c:
    anime_card_details = i.find("div", {"class": "anime-card-details"})
    anime_title = anime_card_details.find("div", {"class": "anime-card-title"})
    print(anime_title.text.strip())
    animetitle = anime_title.text.strip()
    anime_link = anime_title.find("a")["href"]
    request2 = Request(anime_link, headers=headers)
    response2 = urlopen(request2)
    html2 = response2.read()
    response2.close()
    soup2 = bs(html2, "html.parser")
    anime_info_container = soup2.find("div", {"class": "anime-info-container"})
    anime_story_element = anime_info_container.find("p", {"class": "anime-story"}).text.strip()
    
    # التحقق من وجود الأنمي في الملف الحالي
    anime_exists = any(
        anime["Title"] == anime_story_element for anime in current_data
    )
    if anime_exists:
        print("تم تجاهل هذا الأنمي لأنه موجود بالفعل في الملف الحالي.")
        continue

    anime_image = anime_info_container.find("img")["src"]
    anime_genres_list = anime_info_container.find("ul", {"class": "anime-genres"}).find_all("li")
    anime_genres = ",".join([item.text.strip() for item in anime_genres_list])
    anime_info_list = soup2.find_all("div", {"class": "col-md-6 col-sm-12"})
    anime_info = "\n⿻".join([x.find("div", {"class": "anime-info"}).text.strip() for x in anime_info_list])

    anime_ep_list = soup2.find_all("div", {"class": "col-lg-3 col-md-3 col-sm-12 col-xs-12 col-no-padding col-mobile-no-padding DivEpisodeContainer"})

    anime_ep = []

    for t in anime_ep_list:
        anime_ep_url = t.find("div", {"class": "episodes-card-title"}).find("a")["href"]
        anime_ep_name = t.find("div", {"class": "episodes-card-title"}).text.strip()

        # التحقق من وجود الحلقة في الأنمي
        episode_exists = any(
            episode["name"] == anime_ep_name
            for anime in current_data
            for episode in anime.get("ep", [])
            if anime["image"] == anime_image
        )

        if episode_exists:
            print(f"تم تجاهل هذه الحلقة لأنها موجودة بالفعل في الملف الحالي للأنمي: {animetitle}")
            continue

        servers_data = []
        request3 = Request(anime_ep_url, headers=headers)
        response3 = urlopen(request3)
        html3 = response3.read()
        response3.close()
        soup3 = bs(html3, "html.parser")
        anime_servers_list = soup3.find_all("div", {"class": "col-md-6"})
        for server_element in anime_servers_list:
            quality_element = server_element.find("ul", {"class": "quality-list"})
            if quality_element is not None:
                quality_name = quality_element.find("li").text.strip()
                server_links = quality_element.find_all("a")
                server_urls = [link["href"] for link in server_links]
                quality_items = quality_element.find_all("li")
                texts = [item.text.strip() for item in quality_items[1:]]

                server_data = []
                for i in range(len(server_urls)):
                    server_data.append({
                        "server": texts[i],
                        "url": server_urls[i]
                    })

                servers_data.append({
                    "quality": quality_name,
                    "servers": server_data
                })

        anime_ep.append({
            "name": anime_ep_name,
            "servers": servers_data
        })

    # التحقق من وجود الأنمي في الملف الحالي وإضافة الحلقات إليه
    anime_found = False
    for anime in current_data:
        if anime["image"] == anime_image:
            anime["ep"].extend(anime_ep)
            anime_found = True
            break

    # إضافة الأنمي كقسم جديد في حالة عدم وجوده في الملف الحالي
    if not anime_found:
        new_anime = {
            "names": [animetitle],
            "Title": animetitle,
            "image": anime_image,
            "Genres": anime_genres,
            "info": anime_info,
            "ep": anime_ep
        }
        current_data.append(new_anime)

data.append(current_data)
time.sleep(2)

# حفظ الملف النهائي
with open("database/witanime.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("تم حفظ المعلومات بنجاح في ملف JSON.")
