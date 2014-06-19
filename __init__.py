#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

from quokka.modules.bands.views import JsonView


module = Blueprint('bands', __name__, template_folder='templates')

# Register the urls if needed
# in this case there is no need to register any specific url
# module.add_url_rule('/bands/', view_func=ListView.as_view('list'))
# module.add_url_rule('/bands/<slug>/', view_func=DetailView.as_view('detail'))

module.add_url_rule('/%s/json' % module.name, view_func=JsonView.as_view('json'))