import re
import json

class ManifestOutput(object):

    def __init__(self, data):
        self.data = self.manifest_output(data)

    def manifest_output(self, data, input_delimiter="_", output_delimiter="_"):
        for item in data:
            name = output_delimiter.join(self.camel_case_split(str(item))).replace(input_delimiter, " ").title()
            _type = self.calculate_type(data[item])
            data[item] = {"name": name,
                          "type": _type}
        return data

    def json_print(self, indent=4):
        print json.dumps(self.data) 

    def calculate_type(self, item):
        _type = 1
        if isinstance(item, bool):
            _type = 7
        if isinstance(item, int):
            _type = 6
        if isinstance(item, list):
            _type = 5
        return _type

    def camel_case_split(self, identifier):
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
        return [m.group(0) for m in matches]
