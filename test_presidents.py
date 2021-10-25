import requests

presidentsList = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson",
                  "Buren", "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan",
                  "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland",
                  "Harrison", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding",
                  "Coolidge", "Hoover", "Roosevelt", "Truman", "Eisenhower", "Kennedy", "Johnson",
                  "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Bush", "Obama", "Trump",
                  "Biden"]

url_ddg = "https://api.duckduckgo.com"

def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]


def test_PresidentsList():
    resp = requests.get(url_ddg + "/?q=presidents_of_the_united_states&format=json")
    rsp_data = resp.json()
    retrievedPresidents = []
    for i in rsp_data["RelatedTopics"]:
        if(i["Text"].split('-')[0].split()[-1] in presidentsList):
            retrievedPresidents.append(i["Text"].split('-')[0].split()[-1])
    assert retrievedPresidents.sort() == presidentsList.sort()
