from animal import Animal, Dog, Cat

def display_animal(animal):
    animal.walk()
    animal.run()
    animal.eat("food")
    animal.make_sound()

def main():
    dog = Dog("Buddy", 3)
    cat = Cat("Whiskers", 2)

    animals = [dog,cat]

    for animal in animals:
        display_animal(animal)

    #print(f"\nTotal number of animals created: {Animal.count}")

    try:
        age= dog.get_age()
        print(f"{dog.name} is {age} years old.")
    except Exception as e:
        print(f"Error getting age: {e}")

if __name__ == "__main__":
    main()