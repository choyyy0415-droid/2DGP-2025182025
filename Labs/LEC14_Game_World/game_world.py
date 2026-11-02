BACKGROUND_LAYER = 0
FOREGROUND_LAYER = 1
world = [[], []] # layers for game objects


def clear():
    for layer in world:
        layer.clear()


def add_object(o, depth):
    world[depth].append(o)

def add_objects(ol, depth):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    raise Exception("Object not found")


def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()
