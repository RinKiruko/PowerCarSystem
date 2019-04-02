import os
from hashlib import md5
from django.conf import settings


def generate_path(instance, filename):
    ext = filename.rsplit('.', 1)[-1]
    h = md5(str(filename).encode()).hexdigest()
    result = 'Catalog/%s/%s/%s.%s' % (h[:2], h[2:4], h[4:], ext)
    path = os.path.join(settings.MEDIA_ROOT, result)
    
    if os.path.exists(path):
        os.remove(path)
    return result