
import json

version_json = '''
{"dirty": false, "full-revisionid": "8d3de49c6c04ce2d3fdfb3c56d1d3a05f352a875", "error": null, "version": "0.15.0.post8", "date": "2018-07-16T16:21:51.281495"}'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)

