from __future__ import unicode_literals

import logging
import os
from RequestHandlers import *
from mopidy import config, ext



__version__ = '0.1.0'

# TODO: If you need to log, use loggers named after the current Python module
logger = logging.getLogger(__name__)






def my_app_factory(config, core):
    return [
        ('/', CreateOrJoinSession, {'core': core}),
        ('/createSession', CreateSession),
        ('/joinSession', JoinSession),
        ('/getUsers', GetAllUsers)
]

class Extension(ext.Extension):

    dist_name = 'Mopidy-KillTheDJ'
    ext_name = 'killthedj'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        # TODO: Comment in and edit, or remove entirely
        #schema['username'] = config.String()
        #schema['password'] = config.Secret()
        return schema

    def setup(self, registry):
        registry.add('http:app', {
            'name': self.ext_name,
            'factory': my_app_factory,
        })