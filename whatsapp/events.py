def on_ready(fun):
    
    def returnf():
        return fun()
    
    return returnf()