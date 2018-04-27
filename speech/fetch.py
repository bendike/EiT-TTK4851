import urllib.request, json

class FetchSpeech:

    def get_json(self):
        with urllib.request.urlopen("https://api.thingspeak.com/channels/442123/feeds.json?api_key=P9L2THBJF9F51FGQ&results=2") as url:
            data = json.loads(url.read().decode())
            return data

    def get_hammer(self):
        data = self.get_json()
        return data["feeds"][-1]["field1"]

    def get_pincer(self):
        data = self.get_json()
        return data["feeds"][-1]["field2"]

    def get_clean(self):
        data = self.get_json()
        return data["feeds"][-1]["field3"]

    def get_all_fields(self):
        return [self.get_hammer(), self.get_pincer(), self.get_clean()]

    def get_tool_to_pick(self):
        tool_list = self.get_all_fields()
        for i, element in enumerate(tool_list):
            if element is not None:
                if i == 0:
                    return "hammer"
                elif i == 1:
                    return "pincer"
                elif i == 2:
                    return "clean"

fetch = FetchSpeech()
print(fetch.get_tool_to_pick())