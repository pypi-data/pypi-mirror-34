import re


class DocString2Json(object):
    def __init__(self, raw_method):
        self.raw = re.sub(r"^@api", "", raw_method)

    def __iter__(self):
        yield self.get_key("category")
        yield self.get_key("title")
        yield self.get_key("test")
        yield self.get_key("method")
        yield self.get_key("description")
        yield self.get_key("params")

    def __getitem__(self, key):
        return self.get_key(key)

    def get_key(self, key):
        return (key, self.safe(key));

    def safe(self, prop):
        # return getattr(self, prop)
        try:
            return getattr(self, prop)
        except:
            return False
        finally: pass

    @property
    def category(self):
        res = str(re.findall(r"@category ([\w\W]+?)\n", self.raw)[0])
        return res

    @property
    def title(self):
        res = re.findall(r"@title ([\w\W]+?)\n", self.raw)[0]
        return res

    @property
    def test(self):
        res = re.findall(r"@test ([\w\W]+?)\n", self.raw)[0]
        return res

    @property
    def method(self):
        res = re.findall(r"@method ([\w\W]+?)\n", self.raw)
        return "GET" if not res else res[0]

    @property
    def description(self):
        res = re.findall(r"@description ([\w\W]+?)\n", self.raw)[0]
        return res

    @property
    def params(self):
        res = re.findall(r"@param ([\w\W]+?)\n", self.raw)
        return res if res else []

