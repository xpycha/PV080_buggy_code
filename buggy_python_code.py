import yaml
import flask
import urllib
app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    url = flask.request.args.get("url")
    return fetch_website(version, url)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}


class Person(object):
    def __init__(self, name):
        self.name = name


def print_nametag(person):
    print(person)


def load_yaml(filename):
    stream = open(filename)
    deserialized_data = yaml.load(stream, Loader=yaml.SafeLoader)  # deserializing data
    return deserialized_data


def authenticate(password):
    # Assert that the password is correct
    if password != "Iloveyou":
        print("Access denied")
        return
    print("Successfully authenticated!")


if __name__ == "__main__":
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")
    choice = input("Select vulnerability: ")
    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(new_person)
    elif choice == "3":
        load_yaml(input("File name: "))
        print("Executed -ls on current folder")
    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)
