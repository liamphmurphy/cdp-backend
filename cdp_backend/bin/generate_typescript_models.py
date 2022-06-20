#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom import NotFoundErr
from jinja2 import Environment, BaseLoader, select_autoescape

from numpy import require
from cdp_backend.database import DATABASE_MODELS
import inspect
import ast

template = Environment(loader=BaseLoader).from_string("""
    export default class {{ className }} implements Model {
    {% for attr in attributes %}
        {{ attr }}
    {% endfor %}
}
""".strip()
)

# mapping of fireo Model field types to TypeScript types
TYPE_MAPPINGS = {
    "BooleanField": "boolean",
    "IDField": "str",
    "TextField": "str",
    "DateTime": "Date",
    "utcnow": "Date",
}

class Generator:
    """
       Generator will contain metadata and support utilities for capturing the data needed
       from one of the Python models to generate an equivalent TypeScript model
    """
    name = ""
    docstring = ""
    attributes_list = []
    references = [] # list of other models that the TS model needs to import

    source_tree = {}
    rendered = ""


    # start point for the Generator logic
    def __init__(self, model):
        self.name = model.__name__
        self.docstring = inspect.cleandoc(model.__doc__)
        self.attributes_list = [] # TODO: there is a bug where 'self.attributes_list" state is maintained between Generators... better way to fix this?

        self.source_tree = ast.parse(inspect.getsource(model))

        self.set_attributes()
        self.rendered = template.render(className=self.name, attributes=self.attributes_list)


    def set_attributes(self):
        """
            Given the original source tree, parse the attributes that exist for this model.
        """
        processed_attributes = dict()
        for node in ast.walk(self.source_tree):
            if isinstance(node, ast.Assign):
                id = self.get_assignment_id(node)
                type = self.get_assignment_type(node)
                if id is None or type is None:
                    continue

                for child in ast.walk(node):
                    # if both of these conditions are true, this is an 'Assign' node pertaining to a class attribute
                    if self.node_is_field(child) and id not in processed_attributes.keys():
                        required_char = ""
                        if not self.node_is_required(child):
                            required_char = "?"
                        self.attributes_list.append(f'{id}{required_char}: <type>')
                        processed_attributes[id] = None # mark this ID was processed

    def node_is_field(self, node) -> bool:
        """
           Given an AST node (expected is an 'Assign'), check if any of the child nodes is of type 'Name' with the id == 'fields', this indicates this is a class attribute to be generated.
        """
        is_field = False
        for child in ast.walk(node):
            if isinstance(child, ast.Attribute):
                if child.value.id == "fields":
                    is_field = True

        return is_field

    def node_is_required(self, node) -> bool:
        """
            Given an AST node, typically of type 'Assign', check if there a keyword of 'required' was passed in, indicating this class attirbute is required.
        """
        for child in ast.walk(node):
            if isinstance(child, ast.Call):
                for keyword in child.keywords:
                    if keyword.arg == 'required':
                        return True

        return False

    def get_assignment_id(self, assign_attr) -> str:
        """
            Given an AST node of type 'Assign', find the name of the attribute that is being referenced. This is found by finding a sub 'Assign' type that contains this attribute.
        """
        for child in ast.walk(assign_attr):
            if isinstance(child, ast.Assign):
                for target in child.targets:
                    if isinstance(target, ast.Name):
                        return target.id

    def get_assignment_type(self, assign_attr) -> str:
        """
            Given an AST node of type 'Assign', find the name of the attribute that is being referenced. This is found by finding a sub 'Assign' type that contains this attribute.
        """
        if isinstance(assign_attr.value, ast.Call) and isinstance(assign_attr.value.func, ast.Attribute):
            try:
                type_val = TYPE_MAPPINGS[assign_attr.value.func.attr]
                return type_val
            except KeyError as e:
                print(f'model "{self.name}" encountered an unknown class attribue type: {e}')

        return ""




# create generators based on the already existing DATABASE_MODELS list
generators = dict()
for model in DATABASE_MODELS:
    generators[model.__name__] = Generator(model)

print(generators["Vote"].rendered)
