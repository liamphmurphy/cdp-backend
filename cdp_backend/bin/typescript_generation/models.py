REFERENCE_TYPE = "ReferenceField"

# mapping of fireo Model field types to TypeScript types
TYPE_MAPPINGS = {
    "BooleanField": "boolean",
    "IDField": "string",
    "TextField": "string",
    "NumberField": "number",
    "DateTime": "Date",
    "utcnow": "Date",
}

class Attribute:
    """
        Attribute will contain data and methods that represents a single attribute. As it stands,
        for each attribute in a cdp_backend Python model, there will be an equivalent TS model attribute.
    """
    id = ""
    required = False
    reference = False
    processed = False
    type = ""

    def __init__(self, id:str, type:str, required=False):
        self.id = id
        self.type = type
        self.required = required

        # if the attribute is of type "ReferenceField", mark as required. Used in template generation. 
        if self.is_reference(type):
            self.reference = True
    
    def mark_processed(self):
        self.processed = True

    # builds the line that assigns the attribute, seen in the TS constructor.
    def build_typescript_attribute(self) -> str:
        assignment_line = ""
        if self.reference:
            assignment_line = f'this.{self.id} = jsonData["{self.id}"].id;'
        else:
            assignment_line = f'this.{self.id} = jsonData["{self.id}"];'

        if self.required:
            return assignment_line
        else:
            # tabbing is to enforce proper indentation in the generated TS model.
            return "if(jsonData[\"{0}\"]) {{\n\t\t{1}\n\t}}".format(self.id, assignment_line)

    # build the string representing the attribute declaration line in the TS model. 
    def build_declaration_line(self) -> str:
        required_char = "?"
        if self.required:
            required_char = ""
        return f'{self.id}{required_char}: {self.type};'
  
    def is_reference(self, type) -> bool:
        """
            Checks if the passed in type is present in the TYPE_MAPPINGS dictionary. If not, it is not
            a known concrete type and is assumed to be a reference.
        """
        return type not in TYPE_MAPPINGS.values()


    def build_reference_line(self) -> str:
        return f'import {self.type} from "./{self.type}'