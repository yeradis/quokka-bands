#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from quokka.core.db import db
from quokka.core.models import Content, Image


class Gallery(Content):
    body = db.StringField(required=True)
    images = db.ListField(
        db.ReferenceField(Image, reverse_delete_rule=db.DENY), default=[]
    )


class Artist(Content):
    title_alias = db.StringField(max_length=255, required=False)
    body = db.StringField(required=True)
    images = db.ListField(
        db.ReferenceField(Image, reverse_delete_rule=db.DENY), default=[]
    )
    galleries = db.ListField(
        db.ReferenceField(Gallery, reverse_delete_rule=db.DENY), default=[]
    )


class Band(Content):
    body = db.StringField(required=True)
    artists = db.ListField(
        db.ReferenceField(Artist, reverse_delete_rule=db.DENY), default=[]
    )
    images = db.ListField(
        db.ReferenceField(Image, reverse_delete_rule=db.DENY), default=[]
    )
    galleries = db.ListField(
        db.ReferenceField(Gallery, reverse_delete_rule=db.DENY), default=[]
    )


# reverse_delete_rule=db.DENY
#reverse_delete_rule=db.NULLIFY

class Album(Content):
    body = db.StringField(required=True)
    artists = db.ListField(
        db.ReferenceField(Artist, reverse_delete_rule=db.DENY), default=[]
    )
    bands = db.ListField(
        db.ReferenceField(Band, reverse_delete_rule=db.DENY), default=[]
    )
    images = db.ListField(
        db.ReferenceField(Image, reverse_delete_rule=db.DENY), default=[]
    )
    release_date = db.DateTimeField(default=datetime.datetime.now, required=False)

    label = db.StringField(required=False)
    producer = db.StringField(required=False)
    catalog_number = db.StringField(required=False)
    region = db.StringField(required=False)
    style = db.StringField(required=False)


