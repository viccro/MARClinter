#A MARC21 leader, as deciphered from https://www.loc.gov/marc/bibliographic/bdleader.html
from prettytable import PrettyTable

class Leader:
    def __init__(self, leader_string, spec):
        self.record_length = LeaderField(self.get_position_label('00-04',spec),'00-04',int(leader_string[0:5]))
        self.set_record_status = self.get_LeaderField('05', leader_string[5:6], spec)
        self.set_record_type = self.get_LeaderField('06', leader_string[6:7], spec)
        self.bibliographic_level = self.get_LeaderField('07', leader_string[7:8], spec)
        self.control_type = self.get_LeaderField('08', leader_string[8:9], spec)
        self.character_encoding_scheme = self.get_LeaderField('09', leader_string[9:10], spec)
        self.indicator_count = LeaderField(self.get_position_label('10',spec),'10', int(leader_string[10:11]))
        self.subfield_code_count = LeaderField(self.get_position_label('11',spec),'11',int(leader_string[11:12]))
        self.base_addr_of_data = LeaderField(self.get_position_label('12-16',spec),'12-16',int(leader_string[12:17]))
        self.encoding_level = self.get_LeaderField('17', leader_string[17:18], spec)
        self.descriptive_cataloging_form = self.get_LeaderField('18', leader_string[18:19], spec)
        self.multipart_resource_record_level = self.get_LeaderField('19', leader_string[19:20], spec)
        self.length_of_length_of_field_portion = LeaderField(self.get_position_label('20',spec),'20',int(leader_string[20:21])) #4
        self.length_of_starting_character_position_portion = LeaderField(self.get_position_label('21',spec),'21',int(leader_string[21:22])) #5
        self.length_of_implementation_defined_portion = LeaderField(self.get_position_label('22',spec),'22',int(leader_string[22:23])) #0
        self.undefined_value = LeaderField(self.get_position_label('23',spec),'23',leader_string[23:24]) #0

    def __str__(self):
        pt = PrettyTable()
        pt.field_names = ['Position','Field Label', 'Value']

        for lf in [i for i in dir(self) if (not callable(i) and "__" not in i)]:
            try:
                pt.add_row([getattr(self,lf).position, getattr(self,lf).label, getattr(self,lf).value])
            except Exception as e:
                pass

        return pt.get_string(sortby="Position").__str__()

    def get_LeaderField(self, ldr_position_str, record_string, spec):
        return LeaderField(self.get_position_label(ldr_position_str, spec), ldr_position_str,
               spec.fields['LDR']['positions'][ldr_position_str]['codes'][record_string]["label"])

    @staticmethod
    def get_position_label(ldr_position_str, spec):
        try:
            return spec.fields['LDR']['positions'][ldr_position_str]['label']
        except:
            return "Undefined"

class LeaderField:
    def __init__(self, label, position_str, value):
        self.label = label
        self.position = position_str
        self.value = value

    def __str__(self):
        return self.position + ", " + self.label + ", " + str(self.value)
