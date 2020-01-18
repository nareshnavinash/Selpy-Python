import os
import yaml
import allure


class Var:
    file_name = None
    local_variable = None
    dynamic_variable = None
    file_path = None

    def __init__(self, file_name, type):
        self.file_name = file_name
        if type == "local":
            try:
                root_dir = os.path.dirname(os.path.abspath(__file__)).replace("/Library", "")
                self.file_path = root_dir + '/Data/TestData/' + file_name
                with open(self.file_path) as file:
                    self.local_variable = yaml.load(file, Loader=yaml.FullLoader)
                allure.attach.file(self.file_path, name=self.file_name, attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                print(e)
        if type == "dynamic":
            try:
                root_dir = os.path.dirname(os.path.abspath(__file__)).replace("/Library", "")
                self.file_path = root_dir + '/Data/DynamicData/' + file_name
                if not os.path.isfile(self.file_path):
                    if str(self.env("snap")) == "1":
                        f = open(self.file_path, "w")
                        f.close()
                with open(self.file_path) as file:
                    self.dynamic_variable = yaml.load(file, Loader=yaml.FullLoader)
                allure.attach.file(self.file_path, name=self.file_name, attachment_type=allure.attachment_type.TEXT)
            except IOError as e:
                print("File is not accessible\n" + str(e))
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

    def local_value_for(self, string) -> str:
        try:
            return self.local_variable[string]
        except Exception as e:
            print(e)
            return ""

    def write(self, params):
        if self.env("snap") == "1":
            with open(self.file_path, 'w') as file:
                documents = yaml.dump(params, file)

    def dynamic_value_for(self, string) -> str:
        try:
            return self.dynamic_variable[string]
        except Exception as e:
            print(e)
            return ""

    def compare(self, displayed_variable):
        if self.env("snap") == "1":
            self.write(displayed_variable)
        for key, value in displayed_variable.items():
            try:
                file_value = self.dynamic_variable[key]
            except Exception as e:
                print(e)
                file_value = "key_not_available"
            if file_value == "key_not_available":
                with allure.step("Verifying the key: " + str(key)):
                    assert (file_value == value), "Key is not available in the dynamic data file\n Key:- " + key \
                                                  + "\nTo store the displayed value try running the suite with\n" \
                                                  + "snap=1 pytest"
            else:
                with allure.step("Verifying the key: " + str(key)):
                    assert (file_value == value), "Value for the Key:- " + key + ", Mismatches\n" \
                                                  + "File Value:- " + file_value \
                                                  + "\nDisplayed Value:- " + value \
                                                  + "\nFile used for validation is:" + self.file_name \
                                                  + "\nTo change the Dynamic file value run the suite with" \
                                                  + "\nsnap=1 pytest"
