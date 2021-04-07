contacts = [
    ("Pushkar Bhatt", "9837977961"),
    ("Gaurav Bhatt", "8287728318"),
    ("Albert Einstein", "8171369192")
]

def find_contact(contacts, name):
    for n, p in contacts:
        if n == name:
            return p
    return None

def unique_fname_list(contacts):
    unique_names = []
    for name, number in contacts:
        first_name, last_name = name.split(" ", 1)
        for uname in unique_names:
            if uname == first_name: 
                break
            else:
                unique_names.append(first_name)
    return len(unique_names)

def unique_fname_set(contacts):
    unique_names = set()
    for name, number in contacts:
        first_name, last_name = name.split(" ", 1)
        unique_names.add(first_name)
    return len(unique_names)

find_contact(contacts, "Gaurav Bhatt")
print("No of unique names using list: ", unique_fname_list(contacts))
print("No of unique names using tuple: ", unique_fname_set(contacts))