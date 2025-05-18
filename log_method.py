import functools

def log_method(func):
  @functools.wraps(func)
  def wrapper(self, *args, **kwargs):
    print("->", func.__name__.replace("_", " "))
    return func(self, *args, **kwargs)
  return wrapper
