from bs4 import BeautifulSoup as bs


def main():
    soup_followers = bs(open('./Followers.txt', encoding="utf-8"), 'html.parser')
    followers = get_names(soup_followers)

    soup_following = bs(open('./Following.txt', encoding="utf-8"), 'html.parser')
    following = get_names(soup_following)

    not_follow_back = set(following) - set(followers)
    followers_i_dont_follow = set(followers) - set(following)

    # Pass an argument which one you want
    write_to_file(followers_i_dont_follow)


def write_to_file(set_people):
    with open('accounts.txt', 'w') as f:
        for i in set_people:
            f.write(i+"\n")
        f.close()

def get_names(soup):
    lista_followers = soup.find_all('a', href=True)
    lista_followers = [f.text for f in lista_followers if f.text]
    return lista_followers


if __name__ == "__main__":
    main()
