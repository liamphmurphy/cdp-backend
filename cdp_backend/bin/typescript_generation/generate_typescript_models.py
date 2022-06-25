#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom import NotFoundErr
from jinja2 import Environment, FileSystemLoader, select_autoescape

from numpy import require
from cdp_backend.database import DATABASE_MODELS
import inspect
import ast


# mapping of fireo Model field types to TypeScript types
TYPE_MAPPINGS = {
    "BooleanField": "boolean",
    "IDField": "string",
    "TextField": "string",
    "NumberField": "number",
    "DateTime": "Date",
    "utcnow": "Date",
}

TYPESCRIPT_TEMPLATE_FILE = "./typescript_model.html"
template = Environment(loader=FileSystemLoader("./")).get_template(TYPESCRIPT_TEMPLATE_FILE)

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
        self.references = []

        self.source_tree = ast.parse(inspect.getsource(model))

        self.set_attributes()
        self.rendered = template.render(className=self.name, attributes=self.attributes_list, references=self.references)


    def set_attributes(self):
        """
            Given the original source tree, parse the attributes that exist for this model.
        """
        processed_attributes = dict()
        for node in ast.walk(self.source_tree):
            # once we hit the example class for a given model, we can stop parsing
            if self.assign_node_is_example(node):
                return

            if isinstance(node, ast.Assign):
                id = self.get_assignment_id(node)
                type = self.get_assignment_type(node)
                if id is None or type is None:
                    continue

                for child in ast.walk(node):
                    # if both of these conditions are true, this is an 'Assign' node pertaining to a class attribute
                    if self.node_is_field(child) and id not in processed_attributes:
                        # TODO: make this next part way less gross
                        required_char = "?"
                        if self.node_is_required(child):
                            required_char = ""
                        self.attributes_list.append(f'{id}{required_char}: {type};')
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
            Given an AST node, typically of type 'Assign', check if there is a keyword of 'required' passed in, indicating this class attirbute is required.
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
        type_val = ""
        if self.attribute_has_function_call(assign_attr):
            try:
                # need to map the fireo Model field types to an associated TypeScript type
                if assign_attr.value.func.attr == "ReferenceField":
                    type_val = self.extract_reference_field(assign_attr.value) # reference fields require some extra work to determine what type is being referenced
                    self.references.append(type_val)
                else:
                    type_val = TYPE_MAPPINGS[assign_attr.value.func.attr]
            except KeyError as e:
                raise KeyError(f'model "{self.name}" encountered an unknown class attribute type: {e} with a node value of: {ast.dump(assign_attr.value)}')

        return type_val

    def extract_reference_field(self, reference_node) -> str:
        return reference_node.args[0].id # TODO: this seems to be a list in most cases... how do we know which one to get? always the first one?

    def assign_node_is_example(self, node) -> bool:
        """
            Given an AST node of type 'FunctionDef', determine if this is an "Example" model. Most, if not all, of the Python models have "Example" classes that give an example of what a valid model looks like. We don't want to process these for TypeScript generation.
        """
        if not isinstance(node, ast.FunctionDef):
            return False

        if node.name == "Example":
            return True

        return False

    def attribute_has_function_call(self, node):
        """
            Given an AST node of type 'Assign', determine if it's value is inferered from a function call.
        """
        return isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Attribute)




# create generators based on the already existing DATABASE_MODELS list
generators = dict()
for model in DATABASE_MODELS:
    generators[model.__name__] = Generator(model)

print(generators["MinutesItem"].rendered)
