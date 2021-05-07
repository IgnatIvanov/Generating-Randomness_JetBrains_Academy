def tagged(func):
    def wrapper(arg):
        answer = str()
        answer = '<title>'
        answer += func(arg)
        answer += '</title>'
        return answer
        
    return wrapper
