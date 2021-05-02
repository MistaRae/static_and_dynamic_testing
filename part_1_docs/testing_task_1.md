### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

#there is no init statement or decleration of how instance variables are assigned.
#(the class is undefined)
class CardGame:

  def check_for_ace(self, card):
    if card.value = 1:
      return True
    #no : after else
    else
      return False
   
# dif should be def
#no comma seperating the parameters
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
  #there is no variable 'card' - should be card1
    return card
  else:
    return card2
  


def cards_total(self, cards):
  #total is an undefined variable
  total
  for card in cards:
    total += card.value
  #the return statement should be indented to the same level as the for loop declaration.
  #the return statement should use an f string to interpolate the value of total in the sentence
    return "You have a total of" + total
  
```
