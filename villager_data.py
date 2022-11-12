"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    unique_species = set()

    # TODO: replace this with your code
    data = open(filename)
    for line in data:
        species = line.rstrip().split("|")[1]
        unique_species.add(species)

    return unique_species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    # TODO: replace this with your code
    data = open(filename)
    for line in data:
        names, species = line.rstrip().split("|")[:2]
        if search_string in ("All", species):
            villagers.append(names)
            
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    names = []
    hobbies_finess = []
    hobbies_Nature = []
    hobbies_education = []
    hobbies_music = []
    hobbies_fashion = []
    hobbies_play = []
    
    
    
    data = open(filename)
    for line in data:
        name = line.rstrip().split("|")[0]
        hobby = line.rstrip().split("|")[3]
        if hobby == 'Fitness':
            hobbies_finess.append(name)
        elif hobby == "Nature":
            hobbies_Nature.append(name)
        elif hobby == "Education":
            hobbies_education.append(name)
        elif hobby == "Music":
            hobbies_music.append(name)
        elif hobby == "Fashion":
            hobbies_fashion.append(name)
        elif hobby == "Play":
            hobbies_play.append(name)
            
    return [sorted(hobbies_finess), sorted(hobbies_Nature), sorted(hobbies_education), sorted(hobbies_music), sorted(hobbies_fashion), sorted(hobbies_play)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code
    data = open(filename)
    for line in data:
        all_data.append(tuple(line.rstrip().split('|')))
            
    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    data = open(filename)
    for line in data:
        name = line.rstrip().split('|')[0]
        motto = line.rstrip().split('|')[4]
        if name == villager_name:
            return motto

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
    likeminded = set()
    same_personality = None
    data = all_data(filename)
    for line in data:
        name = line[0]
        personality = line[2]
        if name == villager_name:
            same_personality = personality
            break
    if same_personality:
        for line in data:
            name = line[0]
            personality = line[2]
            if personality == same_personality:
                likeminded.add(name)
    return likeminded
        
    

print(find_likeminded_villagers('villagers.csv', 'Vivian'))
