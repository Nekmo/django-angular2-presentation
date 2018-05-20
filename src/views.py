import os
from django.views.decorators.cache import cache_page
from django.views.static import serve


__dir__ = os.path.dirname(os.path.abspath(__file__))
angular_dist = os.path.join(__dir__, 'static/snippets/')


@cache_page(60 * 15)
def index(request):
    return serve(request, 'index.html', angular_dist)
