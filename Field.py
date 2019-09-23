import Spec

#A MARC21 field, as deciphered from the MARC spec
class Field:
    def __init__(self, field, content, spec):
        self.tag = field[0:3]
        self.length = int(field[3:7])
        self.starting_position = int(field[7:])
        self.content = self.isolateContent(content)
        print(field)

        description = spec.getFieldDescription(self.tag)

        for func in [self.setLabel,
                     self.setRepeatable,
                     self.setIndicator1,
                     self.setIndicator2,
                     self.setSubfields]:
            try:
                func()
            except:
                pass


    def isolateContent(self,content):
        try:
            field_chunk = content[self.starting_position:self.starting_position + self.length]
        except Exception as e:
            raise ("Content string starting position or length was bad in field " + self.tag + e)
        return field_chunk

    def setLabel(self, description):
        self.label = description['label']

    def setRepeatable(self, description):
        self.repeatable = description['repeatable']

    def setUrl(self, description):
        self.url = description['url']

    def setIndicator1(self, description):
        self.indicator1 = description['indicator1']

    def setIndicator2(self, description):
        self.indicator2 = description['indicator2']

    def setSubfields(self, description):
        self.subfields = description['subfields']
