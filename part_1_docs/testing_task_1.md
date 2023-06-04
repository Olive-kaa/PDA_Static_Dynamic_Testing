### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      # single "="is used to assign value, in order to make a condition that card.value is equal to 1, we need to use "=="
      return True
    else
    # missing ":" after "else"
      return False
   

  dif highest_card(self, card1 card2):
  # it should be "def" to set up a function not "dif"
  # ',' is missing between card1 and card2
  if card1.value > card2.value:
    #  indentation needed for the whole "if" statement
    return card
    #  here we want card1 returned, "card" is not defined here
  else:
    return card2
  


def cards_total(self, cards):
  # indentation is needed to include this function inside the scope of the class
  total
  # "total" variable is not assigned any value, it could be: total=0
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # python doesn't allow concatenation of strings and integers but we can convert the total value into a string by using str(total) method
  
```
