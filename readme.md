# Console Diving Game


## How to create an entity?

When creating an entity, first you need to import the Entity object: '_from entities.entity import Entity_', and create a class for the entity you want to create, which inherits Entity:

> class JellyFish(Entity):

Currently, there are the following parameters you can set:

* __initial_position=(x, y)__ allows you to define where an entity appears, if it was given no starting position when created.

* __states__ is a list of (list of strings), where each line describes one row of the entity's appearance. For example, for the JellyFish we have:

```
    states = [
            [
                "  __  ",
                " OOOO ",
                "OOOOOO",
                " /  \\ ",
            ], # the list of strings for the first state
            [
                "  __  ",
                " OOOO ",
                "OOOOOO",
                " \\  / ",
            ] # the list of strings for the second state
        ]
```

When you want to animate an entity, you need to create the __def update(self):__ function, where you can modify the following things to move the entity, or change it's appearance:

* __self.current_state__ determines the appreance of the entity. It starts from 0

* __self.x__ and __self.y__ determine the position of the entity.