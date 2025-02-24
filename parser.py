import requests
from bs4 import BeautifulSoup

url = input("Введите URL страницы: ")

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = soup.find_all('span', class_='titleline')
    
    scores = soup.find_all('span', class_='score')
    
    subtexts = soup.find_all('td', class_='subtext')
    
    unique_posts = set()
    
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("Результаты парсинга\n")
        file.write("=" * 50 + "\n\n")

        post_number = 1
        for i, title in enumerate(titles):
            title_text = title.get_text()

            link = title.find('a')['href']

            post_key = f"{title_text}||{link}"  
            if post_key in unique_posts:
                continue 
            unique_posts.add(post_key)  

            if i < len(scores):
                score = scores[i].get_text()
            else:
                score = "N/A"

            if i < len(subtexts):
                subtext = subtexts[i]
                user = subtext.find('a', class_='hnuser')
                user_name = user.get_text() if user else "N/A"

                comments = subtext.find_all('a')[-1].get_text()
                if "comment" not in comments:
                    comments = "0 comments"
            else:
                user_name = "N/A"
                comments = "N/A"

            result = (
                f"Пост №{post_number}\n"
                f"  Заголовок: {title_text}\n"
                f"  Ссылка: {link}\n"
                f"  Очки: {score}\n"
                f"  Пользователь: {user_name}\n"
                f"  Комментарии: {comments}\n"
                "-" * 50 + "\n\n"
            )

            file.write(result)
            post_number += 1 
    
    print(f"Данные успешно сохранены в файл 'output.txt'. Найдено уникальных постов: {len(unique_posts)}")
else:
    print(f"Ошибка при запросе страницы: {response.status_code}")
