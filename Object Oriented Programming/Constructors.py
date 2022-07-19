class Person:
    def __init__(self, name):
        self.name = ___
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is " + str(self)

# Create a new instance with a name of your choice
some_person = Person("Piyush")
# Call the greeting method
print(some_person.greeting())
