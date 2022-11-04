import requests
 	
app_id = "1ca388f7"
app_key = "0b199fbb47db6f97dc1afa5eaf80c94a"
endpoint = "entries"
language_code = "en-gb"

word_id = "book"

def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False
    
    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for sense in senses:
        definitions.append(f"📖 {sense['definitions'][0]}")
    output['definitions'] = "\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

        return output

if __name__ == '__main__':
    from pprint import pprint as print
    print(getDefinitions('Great Britain'))
    print(getDefinitions('america'))