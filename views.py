#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from flask import request, redirect, render_template, url_for
from flask.views import MethodView
from flask.ext.mongoengine.wtf import model_form

from quokka.modules.comments.models import Comment
from .models import Band


logger = logging.getLogger()


class ListView(MethodView):
    def get(self):
        logger.info('getting list of bands')
        bands = Band.objects.all()
        return render_template('bands/list.html', posts=bands)


class DetailView(MethodView):
    logger.info('getting detail of bands')
    form = model_form(
        Comment,
        exclude=['created_at', 'created_by',
                 'published', 'updated_at', 'last_updated_by']
    )

    def get_context(self, slug):
        band = Band.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "band": band,
            "form": form
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('bands/detail.html', **context)

    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            comment = Comment()
            form.populate_obj(comment)

            band = context.get('band')
            band.comments.append(comment)
            band.save()

            return redirect(url_for('bands.detail', slug=slug))

        return render_template('bands/detail.html', **context)


class JsonView(MethodView):
    def get(self):
        # objects = Band.objects()
        #return json_util.dumps(objects._collection_obj.find(objects._query))
        return 'OK GET'

    def post(self):
        return 'OK POST'
