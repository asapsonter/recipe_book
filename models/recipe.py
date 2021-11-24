# create empty list
recipe_list = []

# create get recipe function foe store list
def get_recipe_id():
    if recipe_list:
        last_recipe = recipe_list[-1]
    else:
        return 1
    return last_recipe.id + 1

# create recipe instance classs
class Recipe:
    def __init__(self, name, num_servings, decription, cook_time, dirctions ):
        self.id = get_recipe_id()
        self.name = name
        self.num_servings =num_servings
        self.decription = decription
        self.cook_time = cook_time
        self.dirctions =dirctions
        self.is_published = False
        
    # define data methods
    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'num_servings': self.num_of_servings,
            'cook_time': self.cook_time,
            'directions': self.directions
        }
