import os
import yaml


class Var:
    file_name = None
    local_variable = None

    def __init__(self, file_name):
        self.file_name = file_name
        try:
            root_dir = os.path.dirname(os.path.abspath(__file__)).replace("/Library", "")
            with open(root_dir + '/Data/TestData/' + file_name) as file:
                self.local_variable = yaml.load(file, Loader=yaml.FullLoader)
        except Exception as e:
            print(e)

    @staticmethod
    def env(string):
        try:
            return os.environ[string]
        except Exception as e:
            print(e)
            return "None"

    @staticmethod
    def glob(string):
        try:
            root_dir = os.path.dirname(os.path.abspath(__file__)).replace("/Library", "")
            with open(root_dir + '/Data/GlobalData/global_data.yml') as file:
                global_data = yaml.load(file, Loader=yaml.FullLoader)
                return global_data[string]
        except Exception as e:
            print(e)
            return "None"

    def loc(self, string):
        try:
            return self.local_variable[string]
        except Exception as e:
            print(e)
            return ""
