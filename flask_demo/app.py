# coding: utf8
from flask import Flask
import configparser
import requests
from mysql_operation import operation

app = Flask(__name__)


@app.route('/')
def test():
    config = configparser.ConfigParser()
    config.read('config.ini')
    names_url = config['REGISTRY']['names']
    tags_url = config['REGISTRY']['tags']

    names = requests.get(names_url).json()['repositories']
    lines = ''
    for n in names:
        res = requests.get(tags_url.format(n))
        if res.ok:
            tags = res.json()['tags']
            for t in tags:
                line = """<tr>
                              <td>{}</td>
                              <td>{}</td>
                          </tr>"""
                lines += line.format(n, t)
                operation(n, t)

    result = '''<table>
                    <thead>
                        <tr>
                            <th>names</th>
                            <th>tags</th>
                        </tr>
                    </thead>
                    <tbody>
                        {}
                    </tbody>
                </table>
    '''
    return result.format(lines)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
