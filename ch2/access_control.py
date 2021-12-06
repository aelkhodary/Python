class SecretString:
    """A not-at-all secure way to store a secret string."""

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        """Only show the string if the pass_phrase is correct"""
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ""

if __name__ == "__main__" :
    sec_str = SecretString("ACME: Top Secret", "antwerp")
    print(sec_str.decrypt("antwerp"))

""" To create virtual enviroment 

cd project_directory
python -m venv env
source env/bin/activate  # on Linux or macOS
env/bin/activate.bat     # on Windows ”

use the deactivate command when we are done working on this project.

"""

