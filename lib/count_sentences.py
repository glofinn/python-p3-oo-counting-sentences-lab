#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  def get_value(self):
    return self._value

  def set_value(self, string):
    if (type(string) in (str,)):
      self._value = string
    else:
      print('The value must be a string.')

  def is_sentence(self):
    return self._value.endswith('.')
  
  def is_question(self):
    return self._value.endswith('?')
  
  def is_exclamation(self):
    return self._value.endswith('!')
  
  def count_sentences(self):
    value = self._value
    for punc in ['!', '?']:
      value = value.replace(punc, '. ')
      sentences = [sentence for sentence in value.split('.') if sentence]
      
      # print(len(sentences))
      return(len(sentences))
    


  value = property(get_value, set_value)

# test_string = MyString('Hello, my name is Finn. I am sad! Do I like food?')