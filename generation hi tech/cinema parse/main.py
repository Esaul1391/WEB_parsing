import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Film:
    title: str
    link: str
    posters: str
    genre: str
    year: str
    descriptions: str


def get_film_description_parms(tags: List[Tag]) -> Dict[str, str]:
    params = {}
    for tag in tags:
        name = tag.text.strip()
        if name == 'Жанр:':
            params['genre'] = tag.next_sibling
        elif name == "Год выпуска:":
            params['year'] = tag.next_sibling
        elif name == 'Описание фильма':
            params['description'] = tag.next_sibling
    return params



def parser_data_by_url(url: str) -> List[Film]:
    result = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find('tale', class_='const')
    cards = table.find_all('div', class_='basebox')
    for card in cards:
        heading = card.find('h2', class_='heading')
        title = heading.text
        link = heading.next.attrs.get('href')
        case_poster = card.find('div', class_='film-poster')
        if not case_poster:
            case_poster = card.find('div', class_="filmposter-licenzia")
        poster = case_poster.find('img').attrs.get('src')
        descriotion = card.find_all("strong")
        descriotion_params = get_film_description_parms(descriotion)
        result.append(
            Film(
                title=title,
                link=link,
                poster=poster,
                **descriotion_params
            )
        )
    return result


if __name__ == '__main__':
    url = ''
    data = parser_data_by_url()
    print(data)