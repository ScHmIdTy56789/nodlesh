from pyramid.config import Configurator
from nodlesh.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_view('nodlesh.views.my_view',
                    context='nodlesh:resources.Root',
                    renderer='nodlesh:templates/mytemplate.pt')
    config.add_static_view('static', 'nodlesh:static')
    return config.make_wsgi_app()

