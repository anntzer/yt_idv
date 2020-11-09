class BaseContext:
    image_widget = None

    def __init__(self, width, height, **kwargs):
        self.width = width
        self.height = height

    def add_scene(self, ds, field, no_ghost=True):
        from ..scene_graph import SceneGraph

        self.scene = SceneGraph.from_ds(ds, field, no_ghost=no_ghost)
        return self.scene
