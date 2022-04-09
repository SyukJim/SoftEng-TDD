import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble

class TestNerClient(unittest.TestCase):

     #{ ents: [{...}],
     # html: "<span>..."}

    def test_get_ents_return_dictiionary_given_empoty_input_self(self):
        model - NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        sel.assertIsInstance(ents, dict)

    def test_get_ents_return_list_given_nonempty_string(self):
        model - NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in Wisconsin")
        sel.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model - NerModelTestDouble('eng')
        doc_ents = [{'text': 'Laurent Fressinet', 'label_':'PERSON'}]
        model.return_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}], html: "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model - NerModelTestDouble('eng')
        doc_ents = [{'text': 'Lithuanian', 'label_':'PERSON'}]
        model.return_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Lithuanian', 'label': 'Group'}], html: "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model - NerModelTestDouble('eng')
        doc_ents = [{'text': 'the sea', 'label_':'LOC'}]
        model.return_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'the sea', 'label': 'Location'}], html: "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Eng', 'label_':'LANGUAGE'}]
        model.return_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Eng', 'label': 'Language'}], html: "" }
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_multiple_ents_serialization_all(self)
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Eng', 'label_':'LANGUAGE'}, {'text': 'Judith', 'label_': 'PERSON'}]
        model.return_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents':
                          [{'ent': 'Eng', 'label': 'Language'}], html: "" }
        self.assertListEqual(result['ents'], expected_result['ents'])


