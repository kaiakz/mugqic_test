import os
import json
import re

mugqic_path = "../data_test/SoftStackCatalog/modulefiles/mugqic"

# Store all infomation like:
# {
#     "bcftools": {
#         "module_version": "1.3",
#         "available_versions": ["1.1", "1.2", "1.3"],
#         "description": "",
#         "url": "",
#     },
#     ...
# }

DATABASE = {}

def read_mugqic_info(path, database):
    # read each modules' name as a list
    mods = os.listdir(path)
    for mod in mods:
        info = {}

        sub_dir_path = os.path.join(path, mod)
        sub_dir_ctx = os.listdir(sub_dir_path)

        # read ".version" to get the current version
        with open(os.path.join(sub_dir_path, ".version")) as f:
            info["module_version"] = parse_module_version(f.read())

        # read the files' name as available_version
        sub_dir_ctx.remove(".version")
        info["available_versions"] = sub_dir_ctx
        get_description_url(mod, info)
        database[mod] = info


def parse_module_version(ctx):
    # Search set ModulesVersion "0.21.0"
    ver = re.search("\"(.*)\"", ctx).group()
    return eval(ver)

def get_description_url(mod, info):
    with open("other.json") as f:
        data = json.load(f)
        info["description"] = data[mod]["description"]
        info["url"] = data[mod]["url"]


read_mugqic_info(mugqic_path, DATABASE)
with open("result.json", "w") as f:
    json.dump(DATABASE, f)