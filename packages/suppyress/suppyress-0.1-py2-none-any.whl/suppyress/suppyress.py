def safe_run(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except:
        return None


def suppress(func):
    def func_wrapper(*args, **kwargs):
        return safe_run(func, *args, **kwargs)

    return func_wrapper
