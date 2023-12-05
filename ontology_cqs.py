import csv

class OntologyCQs:
    name: str
    uri: str
    publication: str
    cqs_uri: str
    commments: str
    cqs: [str]

    def __init__(self, name, uri = None, publication = None, cqs_uri = None, comments = None, cqs = None) -> None:
        self.name = name
        if uri is not None:
            self.uri = uri
        if publication is not None:
            self.publication = publication
        if cqs_uri is not None:
            self.cqs_uri = cqs_uri
        if comments is not None:
            self.comments = comments
        if cqs is not None:
            self.cqs = cqs
        else:
            self.cqs = []

def load_ontology_cqs(filename):
    ontology_cqs_by_name = {}
    curr_ontology_cqs: OntologyCQs = None
    cqs_mod = False
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            key = row[0].strip()
            value = row[1].strip()
            if cqs_mod:
                if key == '':
                    cqs_mod = False
                    curr_ontology_cqs = None
                else:
                    curr_ontology_cqs.cqs.append(value)
            if key == 'Ontology name:':
                curr_ontology_cqs = OntologyCQs(value)
                ontology_cqs_by_name[curr_ontology_cqs.name] = curr_ontology_cqs
            elif key == 'URI: ':
                curr_ontology_cqs.uri = value
            elif key == 'Publication:':
                curr_ontology_cqs.publication = value
            elif key == 'CQs URI:':
                curr_ontology_cqs.cqs_uri = value
            elif key == 'ID':
                cqs_mod = True
    return ontology_cqs_by_name

def split_cqs(ontology_cqs: OntologyCQs):
    return [
        OntologyCQs(
            ontology_cqs.name,
            cqs=[cq])
        for cq in ontology_cqs.cqs
    ]