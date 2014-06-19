# coding: utf-8

from flask.ext.script import Command, Option

from .models import Band


class ListBands(Command):
    "prints a list of bands"

    command_name = 'list_posts'

    option_list = (
        Option('--title', '-t', dest='title'),
    )

    def run(self, title=None):

        bands = Band.objects
        if title:
            bands = bands(title=title)

        for band in bands:
            print(band)
