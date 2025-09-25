# Pluggable interface for parts lookup
class PartsLookupAdapter:
    def lookup(self, part_number:str) -> dict:
        raise NotImplementedError

def get_adapter(name:str):
    if name == "stub":
        return StubPartsAdapter()
    raise ValueError(f"No adapter: {name}")

class StubPartsAdapter(PartsLookupAdapter):
    def lookup(self, part_number:str):
        # Returns canned response
        return {"part_number": part_number, "name": "Stub Part", "desc": "For testing"}