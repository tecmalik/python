import unittest

from stringtask import simplestring


def removeCharacter(input):
    pass


class MyTestCase(unittest.TestCase):
    def test_that_the_characters_in_the_string_is_counted(self):
        result = simplestring.get_number_of_characters("semicolon.africa")
        expected = {'s':1,'e':1,'m':1,'i':2,'c':2,'o': 2,'l':1,'n':1,".":1,'a':2,'f':1 ,'r':1}
        self.assertEqual(result, expected)

    def test_that_two_given_strings_separated_by_spaces_can_swap_the_first_two_characters_of_each(self):
        first_input, second_input = 'abc', 'xyz'
        result = simplestring.swapFirstCharacters(first_input, second_input)
        expected = 'xyc abz'
        self.assertEqual(result, expected)

    def test_that_ce_is_added_at_the_middle_if_the_word_can_be_divided_equally(self):
        word = 'helloo'
        result = simplestring.add_ce(word)
        expected = 'helceloo'
        self.assertEqual(result, expected)

    def test_that_ce_is_Added(self):
        word = 'joy'
        result = simplestring.add_ce(word)
        expected = 'joyce'
        self.assertEqual(result, expected)

    def test_that_i_can_input_a_word_and_arrange_the_uppercase_first(self):
        word = "sEmIColOn"
        result = simplestring.arrange_case(word)
        expected = "EICOsmoln"
        self.assertEqual(result,expected)

    def test_to_remove_any_special_character_or_punctuation_in_a_string_character(self):
        word= "he,ll.o"
        result = simplestring.removeCharacter(word)
        expected = "hello"
        self.assertEqual(result,expected)




if __name__ == '__main__':
    unittest.main()
