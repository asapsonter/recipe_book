from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.recipe import Recipe, recipe_list 

# implement a resource class that inherits flask restfull 
class RecipeListResource(Resource):
    
    def get(self):
        
        data = []
        
        for recipe in recipe_list:
            if recipe.is_published is True:
                data.append(recipe.data)
        return {"data": data}, HTTPStatus.OK
    
    # use post method tp create recipe
    def post(self):

        data = request.get_json()
        recipe = Recipe(name=data["name"],
                        description=data["description"],
                        directions=data["directions"],
                        num_servings=data["num_servings"],
                        cook_time=data["cook_time"],)
        recipe_list.append(recipe)
        return recipe.data, HTTPStatus.CREATED
    
    
# recipe resource implement get
class RecipeResource(Resource):
    
    def get(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id ==
                        recipe_id and recipe_id.is_published ==True), None)
        
        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
        return Recipe.data, HTTPStatus.Ok
    
    # implement put method
    def put(self, recipe_id):
        data = request.get_json()
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
        
        # update recipes objects
        recipe.name = data["name"]
        recipe.description = data["description"]
        recipe.num_servings = data["num_servings"]
        recipe.directions = data["directions"]
        recipe.cook_time = data["cook_time"]
        
        return recipe.data, HTTPStatus.OK
# define public class methods
class RecipePublishResource(Resource):
    def put(self, recipe_id):
        recipe = next(
            (recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
        
        recipe.is_published = True
        return {}, HTTPStatus.NO_CONTENT
    
    
    # implement delete method
    def delete(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id),None)
        if recipe is None:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
        recipe.is_published = False
        return {}, HTTPStatus.NO_CONTENT
    