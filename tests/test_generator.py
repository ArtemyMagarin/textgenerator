import unittest
import textgenerator


class TestGenerator(unittest.TestCase):
    WORD_LIST = ['One', 'Fish', 'Two', 'Fish', 'Red', 'Fish', 'Blue', 'Fish']

    def test_make_model_with_window_size_eq_1(self):
        model = textgenerator.make_model(self.WORD_LIST, 1)
        ref_model = {
            ('One',): {'Fish': 1},
            ('Fish',): {'Two': 1, 'Red': 1, 'Blue': 1},
            ('Two',): {'Fish': 1},
            ('Red',): {'Fish': 1},
            ('Blue',): {'Fish': 1},
        }
        self.assertEqual(ref_model, model)

    def test_make_model_with_window_size_eq_2(self):
        model = textgenerator.make_model(self.WORD_LIST, 2)
        ref_model = {
            ('One', 'Fish'): {'Two': 1},
            ('Fish', 'Two'): {'Fish': 1},
            ('Two', 'Fish'): {'Red': 1},
            ('Fish', 'Red'): {'Fish': 1},
            ('Red', 'Fish'): {'Blue': 1},
            ('Fish', 'Blue'): {'Fish': 1},
        }
        self.assertEqual(ref_model, model)

    def test_generator_works_properly(self):
        model = textgenerator.make_model(self.WORD_LIST, 2)
        generated = textgenerator.generate(model, 1, ('One', 'Fish'))
        self.assertEqual(' '.join(self.WORD_LIST)+'.', generated)
