import random
import string
import json

class URLObject(object):
    def __init__(self, url_code=None, url_name=None):
        self.url_name = url_name
        self.url_code = url_code
        self.times_used = 0

    def used_url(self):
        self.times_used += 1

json_dict = json.load(open('url_hash_file.json'))

url_hash_table = {}
for name, url_object in json_dict.iteritems():
    url_hash_table[name] = URLObject()
    url_hash_table[name].__dict__.update(url_object)

def generate_code():
    character_pool = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(character_pool) for i in range(6))
    return random_string

def add_to_hash(url_input):
    global url_hash_table
    new_url_code = generate_code()
    while True:
        if new_url_code not in url_hash_table:
            url_hash_table[new_url_code] = URLObject(new_url_code, url_input)
            save_to_json()
            return new_url_code
        else:
            new_url_code = generate_code()

def save_to_json():
    json_dict = {}
    for name, url_object in url_hash_table.iteritems():
        json_dict[name] = {a:b for a, b in url_object.__dict__.iteritems() if b}

    json.dump(json_dict, open('url_hash_file.json', 'w'))

if __name__ == '__main__':
    print url_hash_table


