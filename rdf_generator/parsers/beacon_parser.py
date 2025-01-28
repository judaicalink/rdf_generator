import re


class BeaconParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.metadata = {}
        self.identifiers = []

    def parse(self):
        """
        Parses the BEACON file to extract metadata and identifiers.
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line.startswith("#"):
                    # Parse metadata
                    key_value = re.match(r"#(\w+):\s*(.*)", line)
                    if key_value:
                        key, value = key_value.groups()
                        self.metadata[key.upper()] = value
                else:
                    # Collect identifiers
                    if line:
                        self.identifiers.append(line)

    def get_target_links(self):
        """
        Generates target links by combining identifiers with the TARGET template.
        """
        target_template = self.metadata.get("TARGET")
        if not target_template:
            raise ValueError("No TARGET template defined in the BEACON file.")

        links = [
            target_template.replace("{ID}", identifier)
            for identifier in self.identifiers
        ]
        return links
