"""
Find the unique object in list:
Explanation: So we will have list of objects [ {}, {}, {}] and each object name will unique
on the basis of the name value find that object.

For Example: [{"age": 21, "name": 'unique_name'}]
"""

# First approach
def find_the_unique_object(data, name):
    """
    It will return the unique objects from the list
    """

    for object in data:
        for key, value in object.items():
            if key == 'name'  and value == name:
                return object

# Second approach

def find_the_unique_object(data, name):
    """
    It will return the unique objects from the list
    """

    return next((obj for obj in data if obj.get('name') == name), None)


if __name__ == "__main__":

    data = [{"age": 23, "name": "abc"}, {"age": 23, "name": "xyz"}]

    print(find_the_unique_object(data, "xyzx"))

