import random as r

bad_matches = [('Brenna','KevKat'),
               ('Brenna', 'Syrcus'),
               ('Brenna', 'Michelle'),
               ('Arianna', 'Erik'),
               ('Charlie', 'Erik'),
               ('Xander', 'Michelle'),
               ('Rebecca', 'Thomas'),
               ('Ben', 'Brenna'),
               ('Ben', 'Thomas'),
               ('Vanessa', 'Charlie'),
               ('Vanessa', 'Erik'),
               ('Syrcus', 'KevKat'),
               ('Xander', 'Simon'),
               ('Arianna', 'Rebecca'),
               ('Michelle', 'Erik')]


def rand_input(total):
    names = []
    for name in total:
        names.insert(r.randint(0, len(names)), name)
    return names


def rand_output(names_1, names_2):
    pairs = []
    while len(names_1) > 0:
        first = r.randint(0, len(names_1) - 1)
        f_name = names_1.pop(first)
        second = r.randint(0, len(names_2) - 1)
        s_name = names_2.pop(second)
        new_pair = (f_name, s_name)
        reverse = (s_name, f_name)
        if bad_matches.__contains__(new_pair) or bad_matches.__contains__(reverse):
            if len(names_1) == 0:
                print("bad run")
                return False
            else:
                names_1.append(f_name)
                names_2.append(s_name)
            continue
        elif f_name == s_name:
            if len(names_1) == 0:
                print("bad run")
                return False
            else:
                names_1.append(f_name)
                names_2.append(s_name)
        else:
            pairs.append(new_pair)
    return pairs


if __name__ == '__main__':
    names_raw = ['KevKat',
                 'Syrcus',
                 'Xander',
                 'Simon',
                 'Vanessa',
                 'Andrew',
                 'Nate',
                 'Ben',
                 'Mady',
                 'Zac',
                 'Archer',
                 'Thomas',
                 'B',
                 'Cami',
                 'Terra',
                 'Erik',
                 'Arianna',
                 'Charlie',
                 'Michelle',
                 'Rebecca',
                 'Brenna',
                 'Nicole']
    randomize = rand_input(names_raw)
    print(randomize)
    pairings = rand_output(randomize, names_raw)
    for pairs in pairings:
        print(pairs)
