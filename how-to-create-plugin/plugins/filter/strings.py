class FilterModule(object):
    def to_uppercase(self, var, duplicate: bool = False):
        if duplicate:
            return var.upper() * 2
        return var.upper()

    def filters(self):
        return {
            'to_uppercase': self.to_uppercase,

            # Aliases for self.to_uppercase
            'grande': self.to_uppercase,
            'gigante': self.to_uppercase,
        }
