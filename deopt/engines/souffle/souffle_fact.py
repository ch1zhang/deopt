from deopt.datalog.base_fact import BaseFact
from deopt.engines.souffle.souffle_subgoal import SouffleSubgoal
from deopt.datalog.variable import Variable
from deopt.utils.file_operations import create_file
import string
import os


class SouffleFact(BaseFact):

    def generate_fact_file(self, export_location):
        # Converts self.fact_data in a string and exports to the program_path location as a fact file
        file_path = os.path.join(export_location, self.name + ".facts")
        data_as_a_string = "".join(i + "\n" for i in self.raw_data_entries)
        create_file(data_as_a_string, file_path)

    def generate_fact(self):
        self.name = self.randomness.get_lower_case_alpha_string(4)
        invalid_name = ["lxor", "lnot", "brie", "land", "bxor", "bnot", "mean", "bshr", "true", "band", "bshl"]
        while self.name in invalid_name:
            self.name = self.randomness.get_lower_case_alpha_string(4)
        self.variables_types = [self.randomness.random_choice(self.allowed_types) for i in range(self.arity)]
        # Generate rows
        for i in range(self.number_of_rows):
            table_entry = self.name + "("
            raw_data_row = ""
            for j in range(self.arity):
                data_type = self.variables_types[j]
                data_item = self.generate_data_item(data_type)
                table_entry += str(data_item) + ", "
                raw_data_row += str(data_item) + "\t"
            table_entry = table_entry[:-2] + ")."
            self.raw_data_entries.append(raw_data_row.strip())
            self.fact_data.append(table_entry)

    def get_fact_as_a_relation(self):
        fact_subgoal = SouffleSubgoal(randomness=self.randomness, arity=self.arity, params=self.params)
        fact_subgoal.generate_subgoal(name=self.name, 
                                        variables=[Variable(name=string.ascii_uppercase[i], vtype=self.variables_types[i]) for i in range(self.arity)], 
                                        variables_types=self.variables_types)
        return fact_subgoal

    def generate_decleration(self):
        self.declaration = ".decl " + self.name + "("
        for i in range(self.arity):
            self.declaration += string.ascii_uppercase[i] + ":" + self.variables_types[i].get_name() + ", "
        self.declaration = self.declaration[:-2] + ")"

    def generate_data_item(self, type):
        if type.get_ancestor_type_name() == "number":
            return self.randomness.get_random_integer(-10,10)
        
        if type.get_ancestor_type_name() == "symbol":
            return '"' + self.randomness.get_random_alpha_numeric_string(self.randomness.get_random_integer(1, 10)) + '"'

        if type.get_ancestor_type_name() == "unsigned":
            return self.randomness.get_random_integer(0,10)

        if type.get_ancestor_type_name() == "float":
            return self.randomness.get_random_float(-10, 10)

    def get_fact_input_string(self):
        return ".input " + self.name