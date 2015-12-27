# -*- coding: utf-8 -*-

from nikola.plugin_categories import Command

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask('snpa')

@app.route("/")
def main_page():
    return "<p>" + os.getcwd() + "</p>"


# nikola plugin command setting
class SNPACommand(Command):
    """Start a snpa server"""

    name = "snpa"
    doc_usage = "[options]"
    doc_purpose = "start the test snpa"

    cmd_options = (
        {
            'name': 'port',
            'short': 'p',
            'long': 'port',
            'default': 5000,
            'type': int,
            'help': 'Port nummber (default: 5000)',
        },
        {
            'name': 'address',
            'short': 'a',
            'long': '--address',
            'type': str,
            'default': '127.0.0.1',
            'help': 'Address to bind (default: 127.0.0.1)',
        },
    )


    def _execute(self, options, args):
        print(options, args)
        print(self.site.config['POSTS'])

        app.run()
