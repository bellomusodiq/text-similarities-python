# text-similarities-python

This is a word count based text similarities implemented in pyton

It is used to run query search on list of dictionary of text, ranks them based on how frequent
word occurs both on the list and the query.

It is independent of position of words and sequence of words in the search string.


## example

```
# here is a list of sentences/words/strings that you want to run search on

list_or_words = [
{'id': 1, 'text':"""
I ate dinner.
We had a three-course meal.
Brad came to dinner with us.
He loves fish tacos.
In the end, we all felt like we ate too much.
We all agreed; it was a magnificent evening.
I hope that, when I've built up my savings, I'll be able to travel to Mexico.
Did you know that, along with gorgeous architecture, it's home to the largest tamale?
Wouldn't it be lovely to enjoy a week soaking up the culture?
Oh, how I'd love to go!
Of all the places to travel, Mexico is at the top of my list.
Would you like to travel with me?
Isn't language learning fun?
There is so much to understand.
I love learning!
Sentences come in many shapes and sizes.
Nothing beats a complete sentence.
Once you know all the elements, it's not difficult to pull together a sentence."""
},
{'id': 2, 'text': """The art of crafting a single sentence brings together subjects, verbs, and objects with cohesion. 
Punctuation also makes its mark, too. A period indicates a declarative or informative sentence. 
An exclamation mark indicates an exclamatory sentence. And, of course, our friend the question 
mark indicates an interrogative sentence. You've also got simple sentences that merely contain 
subjects and verbs, and more complex sentences that contain more than one clause, connected by 
commas, colons or semi-colons.
"""},
{'id': 3, 'text':"""
As long as you remember to include these crucial components -
and a healthy dose of punctuation - you'll be well on your way to sentence mastery. 
A handful of words form a sentence. 
A handful of sentences form a paragraph. Before you know it, you've got the next great 
American novel in the works!
"""},
{'id': 4, 'text': """
Recently, a close friend sent me an e-mail with the subject line 
“Things I’ve Noticed As I Get Older.” The ten numbered observations ranged 
from the mundane (politics is getting stupider) to the poignant (the distant 
melancholy of Facebook’s News Feed, with its dispatches from lives that were 
once, and now no longer, close to one’s own). But with all due respect to the 
observational chops of my correspondent, it wasn’t so much the content of the 
message that impressed me as its form. It was an e-mail in the shape of a listicle, 
a personal correspondence structured for the purposes of frictionless social-media 
sharing.
"""},
{'id': 5, 'text': """
At some level, it seemed, my friend intended his e-mail to go viral within 
the highly targeted demographic of me. I couldn’t help feeling that some basic epistolary 
protocol had been breached, that I was seeing an early sign of what could be a shift in the 
way people communicate. In the not too distant future, all human interactions, written or 
otherwise, might well be conducted in the form of lists—for ease of assimilation, for catchiness, 
for optimal snap. I imagined myself, some decades from now, nervously perched on the papered 
leatherette of an examination bed, 
and my doctor directing her sad, humane eyes at me a moment before clearing her throat and 
saying, “Top Five Signs You Probably Have Pancreatic Cancer
"""}
]

# search below, is the search string
search = """ help feeling that some basic epistolary Pancreatic Cancer"""


# perform_search returns tupule of list_of_words in the order of similarity to the search string, along side their score
# score is a parameter that measures how similar text are.

perform_search(list_or_words, search)


# result

[({
      'id': 5,
      'text': '\nAt some level, it seemed, my friend intended his e-mail to go viral within \nthe highly targeted demographic of me. I couldn’t help feeling that some basic epistolary \nprotocol had been breached, that I was seeing an early sign of what could be a shift in the \nway people communicate. In the not too distant future, all human interactions, written or \notherwise, might well be conducted in the form of lists—for ease of assimilation, for catchiness, \nfor optimal snap. I imagined myself, some decades from now, nervously 
      perched on the papered\ nleatherette of an examination bed,
      \nand my doctor directing her sad,
      humane eyes at me a moment before clearing her throat and\ nsaying,
      “Top Five Signs You Probably Have Pancreatic Cancer\ n '}, 0.08163265306122448), ({'
      id ': 3, '
      text ': "\nAs long as you remember to include these crucial components -\nand a healthy dose of punctuation - you'
      ll be well on your way to sentence mastery.\nA handful of words form a sentence.\nA handful of sentences form a paragraph.Before you know it,
      you 've got the next great \nAmerican novel in the works!\n"}, 0.024390243902439025), ({'
      id ': 2, '
      text ': "The art of crafting a single sentence brings together subjects, verbs, and objects with cohesion. \nPunctuation also makes its mark, too. A period indicates a declarative or informative sentence. \nAn exclamation mark indicates an exclamatory sentence. And, of course, our friend the question \nmark indicates an interrogative sentence. You'
      ve also got simple sentences that merely contain\ nsubjects and verbs,
      and more complex sentences that contain more than one clause,
      connected by\ ncommas,
      colons or semi - colons.\n "}, 0.0196078431372549), ({'id': 4, 'text': '\nRecently, a close friend sent me an e-mail with 
      the subject line\ n“ Things I’ ve Noticed As I Get Older.”The ten numbered observations ranged\ nfrom the mundane(politics is getting stupider) to the poignant(the distant\ nmelancholy of Facebook’ s News Feed, with its dispatches from lives that were\ nonce, and now no longer, close to one’ s own).But with all due respect to the\ nobservational chops of my correspondent,
      it wasn’ t so much the content of the\ nmessage that impressed me as its form.It was an e - mail in the shape of a listicle,
      \na personal correspondence structured
      for the purposes of frictionless social - media\ nsharing.\n '}, 0.012987012987012988), ({'
      id ': 1, '
      text ': "\nI ate dinner.\nWe had a three-course meal.\nBrad came to dinner with us.\nHe loves fish tacos.\nIn the end, we all felt like we ate too much.\nWe all agreed; it was a magnificent evening.\nI hope that, when I'
      ve built up my savings,
      I 'll be able to travel to Mexico.\nDid you know that, along with gorgeous architecture, it'
      s home to the largest tamale ? \nWouldn 't it be lovely to enjoy a week soaking up the culture?\nOh, how I'
      d love to go!\nOf all the places to travel,
      Mexico is at the top of my list.\nWould you like to travel with me ? \nIsn 't language learning fun?\nThere is so much to understand.\nI love learning!\nSentences come in many shapes and sizes.\nNothing beats a complete sentence.\nOnce you know all the elements, it'
      s not difficult to pull together a sentence.
      "}, 0.011235955056179775)]

```
