from rdf_generator.parsers.csv_parser import CSVParser
from rdf_generator.rdf_builder import RDFBuilder

# Parse CSV file
csv_parser = CSVParser("data/people.csv")
data = csv_parser.read_csv()

# Generate RDF from CSV data
rdf_builder = RDFBuilder()
for row in data:
    rdf_builder.add_person(row['Name'], row['Email'])

# Save the RDF output
rdf_output = rdf_builder.serialize()
print(rdf_output)


# from rdf_generator.parsers.beacon_parser import BeaconParser
# from rdf_generator.rdf_builder import RDFBuilder
#
# # Parse the BEACON file
# beacon_parser = BeaconParser("example_beacon.txt")
# beacon_parser.parse()
#
# # Print metadata
# print("Metadata:", beacon_parser.metadata)
#
# # Generate RDF for the links
# rdf_builder = RDFBuilder()
# for link in beacon_parser.get_target_links():
#     rdf_builder.graph.add((rdf_builder.ns[link.split('/')[-1]], rdf_builder.ns.link, rdf_builder.ns[link]))
#
# # Serialize the RDF
# print(rdf_builder.serialize(format="turtle"))