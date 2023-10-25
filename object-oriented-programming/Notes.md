# Python  OOO

## Python styles and coding standards
- [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

## Python OOP

- class, class attributes, instance attributes, class methods, instance methods, `dunder` methods (e.g., `__init()__`, `__str()__`, ...), ...
  - [https://realpython.com/python3-object-oriented-programming/](https://realpython.com/python3-object-oriented-programming/)

## Relationship between classes in python OOO

### Inheritance

- We use inheritance only if there
exists an **“is-a”** relationship between two classes.
- Examples:
  - Car `is a` Vehicle => Car can inherit from Vehicle
  - Apple `is a` Fruit => Apple can inherit from Fruit
  - Cat `is an` Animal
- **subclass** (or child or subtype or derived class): inherits from *superclass*
  - `derive` or  `inherit` or `extend` base class 
    - i.e., subclass inherits the interface and the implementation of the base class
- **superclass** (or base or parent or super class): class from which  *subclass* is derived
- method override: when same method (i.e., same name) exists in both classes, the method in the subclass override the one in the superclass
- `super()` method: when we need to access to the superclass method (e.g `method_name()`) from the subclass => `super().method_name()`
  - `super()`: deep dive: [https://realpython.com/python-super/](https://realpython.com/python-super/)
- classes `inherit`the builtin `object` class by default
- Method Resolution Order (mro): `ClassName.__mro__` show how and where (in which order) to search methods (useful in multiple inheritance scenario)
- **Implementation inheritance** vs **Interface inheritance**

  - Implementation inheritance (or class inheritance) is when a subclass inherits behavior implementation from a base class. The subclass inherit methods, properties and attributes of the superclass without having to write them again

  - Interface inheritance (or interface implementation) is when a subclass only inherits the description of behavior from the base class and provides the implementation itself. The subclass **must implement** all the methods and properties of the interface.
    - To create an abstract class in python:
      - Create abstract class by inheriting the class `ABC`class: e.g.,  `class MyClass(ABC):`
      - we need to decorate methods with the `@abstractmethod` decorator

### Composition

- Composition is a **"has-a"** relationship between classes.
  - `Composite` *has a* `Component`
- Example: A car (`Composite`) has an engine (`Component`), wheels (`Component`)



### Aggregation

- Aggregation is a special type of composition that allows you to create a **"whole-part"** relationship between classes.
- Example: A university has departments, and each department has students.

### Association

- Association is a relationship between two classes that describes the way they interact with each other.
- Example: A person can have a bank account.

### Dependency

- Dependency is a relationship between two classes where one class depends on the other class for its functionality.
- Example: if you have a class that uses another class's methods or attributes, then it depends on that class.


## Ref

- [https://realpython.com/inheritance-composition-python/](https://realpython.com/inheritance-composition-python/)
- [https://www.programiz.com/python-programming/inheritance](https://www.programiz.com/python-programming/inheritance)
- UML
  - [https://creately.com/guides/class-diagram-relationships/](https://creately.com/guides/class-diagram-relationships/)
  - [https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/)
  - [More about uml diagrams](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-uml/)
