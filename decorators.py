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


#2
def html(tag):
    """
    Декоратор, добавляющий теги
    """
    def decorator(func):
        def wrap(*args,**kwargs):
            return '<'+tag+'>'+func(*args,**kwargs)+'</'+tag+'>'
        return wrap
    return decorator

@html('i')
def out():
    return "hello!"

print (out())
    
    
    
    
#3
def benchmark(func):
     """
     Декоратор, выводящий время, которое заняло
     выполнение декорируемой функции.
     """
     import time
     def wrapper(*args, **kwargs):
         t = time.clock()
         res = func(*args, **kwargs)
         print(func.__name__, time.clock() - t)
         return res
     return wrapper
