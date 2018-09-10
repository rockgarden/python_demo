# run command:
# $ gunicorn placeholder --log-file=-

import hashlib
import os
import sys
from io import BytesIO

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY',
                            '%jv_4#hoaqwig2gu!eg#^ozptd*a@88u(aasv7z!7xt^5(*i&k')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1, localhost').split(',')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': (os.path.join(BASE_DIR, 'templates'),),
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.static',
                ],
            },
        },
    ),
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
    ),
    # TODO: Not Found: /static/site.css
    STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles'),
    STATIC_URL='/static/',
)

from django import forms
from django.conf.urls import url
#
from django.core.cache import cache
from django.urls import reverse
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import etag
from django.conf.urls.static import static
# Use pillow to handle image
from PIL import Image, ImageDraw


class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""

    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG'):
        """Generate an image of the given type and return as raw bytes.
        A new generate method has been added to the ImageForm to encapsulate the logic of building the image.
        It takes one argument for the image format, which defaults to PNG, and returns the image contents as bytes.
        :param image_format:
        :return:
        """
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        # A cache key is generated that depends on the width, height, and image format.
        key = '{}.{}.{}'.format(width, height, image_format)
        # Before a new image is created, the cache is checked to see if the image is already stored.
        content = cache.get(key)
        if content is None:
            # Using the width and height given by the URL and validated by the form,
            # a new image is constructed using the Image class from Pillow.
            image = Image.new('RGB', (width, height))
            # generate now uses ImageDraw to add a text overlay if it will fit.
            draw = ImageDraw.Draw(image)
            text = '{} X {}'.format(width, height)
            textwidth, textheight = draw.textsize(text)
            if textwidth < width and textheight < height:
                texttop = (height - textheight) // 2
                textleft = (width - textwidth) // 2
                draw.text((textleft, texttop), text, fill=(255, 255, 255))
            content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            # When there is a cache miss and a new image is created, the image is cached using the key for an hour.
            cache.set(key, content, 60 * 60)
        return content


def generate_etag(request, width, height):
    """
    takes the same arguments as the placeholder view.
    It uses hashlib to return an opaque ETag value, which will vary based on the width and height values.
    :param request:
    :param width:
    :param height:
    :return:
    """
    content = 'Placeholder: {0} x {1}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


@etag(generate_etag)  # The generate_etag function will be passed to the etag decorator on the placeholder view.
def placeholder(request, width, height):
    """
    The view calls form.generate to get the constructed image,
    and the bytes for the image are then used to construct the response body.
    :param request:
    :param width:
    :param height:
    :return:
    """
    form = ImageForm({'height': height, 'width': width})
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid Image Request')


def index(request):
    # The updated index view builds an example URL by reversing the placeholder view,
    # and passes it to the template context.
    example = reverse('placeholder', kwargs={'width': 50, 'height': 50})
    context = {
        'example': request.build_absolute_uri(example)
    }
    # The home.html template is rendered using the render shortcut.
    return render(request, 'home.html', context)


urlpatterns = [
                  url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder,
                      name='placeholder'),
                  url(r'^$', index, name='homepage'), ] + static(settings.STATIC_URL,
                                                                 document_root=settings.STATIC_ROOT)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
