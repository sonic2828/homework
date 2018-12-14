#1
def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print "{0} была вызвана: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper
    
    
    
    
    
#3
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
 
@makebold
@makeitalic
def hello():
    return "hello"
 
print hello()
