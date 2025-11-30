from configparser import ConfigParser
from flask import Flask, render_template, jsonify
from markupsafe import Markup

app = Flask("Config App")

config_data = "" 

@app.route("/")
def Index():
    return render_template("index.html")


def read_config(file_path):
    parser = ConfigParser()

    try:
        parser.read(file_path)
    except Exception as e:
        raise Exception(f"Could not read config file: {e}")

    if not parser.sections():
        raise Exception("Config file is empty or missing")

    data = {}

    for section in parser.sections():
        data[section] = {}
        for key, value in parser.items(section):
            data[section][key] = value

    return data


def format_output(config):
    """Return the EXACT output format you requested."""
    output = "Configuration File Parser Results:\n"

    for section, values in config.items():
        output += f"\n{section}:\n"
        for key, value in values.items():
            output += f"- {key}: {value}\n"

    return output


@app.route("/getConfigData", methods=["GET"])
def get_config_data():
    return Markup(f"<pre>{config_data}</pre>")


if __name__ == "__main__":
    config_dict = read_config("config-file.txt")

    config_data = format_output(config_dict)

    print(config_data)

    app.run(debug=True)
