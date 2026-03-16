class User: 
    def __init__(self, user_id, name, email): 
        self.__user_id = user_id 
        self.__name = name 
        self.__email = email 
        
    def get_name(self): 
        return self.__name 
    
    def display(self): 
        print(f"User: {self.__name} ({self.__email})")