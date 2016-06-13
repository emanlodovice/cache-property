from django.core.cache import cache

from functools import wraps

# decorator that can be used on model properties for caching the returned value
# of that decorated property
def cache_property(base_key='sample-', duration=60):
    def cache_decorator(func):
        @wraps(func)
        def wrapper(self):
            cache_key = '{}{}'.format(base_key, self.pk)
            print cache_key
            cached_data = cache.get(cache_key)
            if cached_data is not None:
                return cached_data
            else:
                data = func(self)
                cache.set(cache_key, data, duration)
                return data
        return wrapper
    return cache_decorator
