from apps.app1 import blueprint


@blueprint.route('/')
def route_default():
    return "app1 index!"


@blueprint.route('/test')
def route_test():
    return "app1 test!"
