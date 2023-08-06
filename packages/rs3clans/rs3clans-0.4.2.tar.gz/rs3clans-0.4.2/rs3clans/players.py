# Standard Imports
import urllib.request
import json


class Player:

    def __init__(self, name):
        self.name = name
        self.info = self.dict_info()
        self.suffix = self.info['isSuffix']
        self.title = self.info['title']
        try:
            self.clan = self.info['clan']
        except KeyError:
            self.clan = None

    def raw_info(self):
        info_url = (f"http://services.runescape.com/m=website-data/playerDetails.ws?names=%5B%22{self.name},"
               f"%22%5D&callback=jQuery000000000000000_0000000000&_=0")
        client = urllib.request.urlopen(info_url)
        return str(client.read())

    def dict_info(self):
        """
        Gets the raw string info from self.raw_info() and formats it into Dictionary format as follows:

        self.info = {
            'isSuffix': True,
            'recruiting': True,
            'name': 'nriver',
            'clan': 'Atlantis',
            'title': 'the Liberator'
        }

        isSuffix (bool): If the player's title is a Suffix or not
        recruiting (bool): If the player's clan is set as Recruiting or not
        name (str): The player's name, passed as is when creating object Player
        clan (str): The player's clan name
        title (str): The player's current title

        Used to make self.info.
        """
        str_info = self.raw_info()
        info_list = []
        # str_info[36] = Start of json format in URL '{'
        for letter in str_info[36:]:
            info_list.append(letter)
            if letter == '}':
                break
        info_list = ''.join(info_list)
        info_dict = json.loads(info_list)
        info_dict['name'] = info_dict['name'].replace(',', '')
        return info_dict


if __name__ == '__main__':
    player = Player("NRiver")  # Creating Player with the name "NRiver"
    print(player.name)  # Player name
    print(player.info)  # Player info
    print(player.clan)  # Player clan
    print(player.title)  # Player title
    print(player.suffix)  # If the player's title is a suffix or not
