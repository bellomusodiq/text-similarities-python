import threading
import string

class TextSimilarity:

    def __init__(self, text, search):
        super().__init__()
        self.text = text
        self.search = search
        self.text_hash = {}
        self.search_hash = {}
        self.threads = []
        self.alphabets = self.init_alphabets()

    def init_alphabets(self):
        alphabets = {}
        for char in string.ascii_lowercase:
            alphabets[char] = char
        return alphabets

    def word_cleaning(self, word):
        new_word = ''
        for char in word.lower():
            if char in self.alphabets:
                new_word += char
        return new_word

    def str_to_hash(self, string, hash_):
        word_list = string.split(" ")
        for word in word_list:
            if not self.word_cleaning(word) in hash_:
                hash_[self.word_cleaning(word)] = 1
    
    def text_to_hash(self):
        self.str_to_hash(self.text, self.text_hash)
        
    def search_to_hash(self):
        self.str_to_hash(self.search, self.search_hash)

    def split_to_hash(self):
        thread1 = threading.Thread(target=self.search_to_hash)
        self.threads.append(thread1)
        thread1.start()
        thread2 = threading.Thread(target=self.text_to_hash)
        self.threads.append(thread2)
        thread2.start()

    def evaluate(self):
        self.split_to_hash()
        for thread in self.threads:
            thread.join()
        word_count = 0
        for word in self.search_hash:
            if word in self.text_hash:
                word_count += 1
        return word_count / len(self.text_hash)


def perform_search(queryset, search_text):
    sorted_query = []
    for query in queryset:
        score = TextSimilarity(query['text'], search)
        score = score.evaluate()
        sorted_query.append((query, score))

    sorted_query = sorted(sorted_query, key=lambda query: query[1], reverse=True)
    print([s[0]['id'] for s in sorted_query])
    

    


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

search = """At some level, it seemed, my friend intended his e-mail to go viral within 
the highly targeted demographic of me. I couldn’t help feeling that some basic epistolary 
protocol had been breached, that I was seeing an early sign of what could be a shift in the 
way people communicate. In the not too distant future, all human interactions, written or 
otherwise, might well be conducted in the form of lists—for ease of assimilation, for catchiness, 
for optimal snap. I imagined myself, some decades from now, nervously perched on the papered 
leatherette of an examination bed, 
and my doctor directing her sad, humane eyes at me a moment before clearing her throat and 
saying, “Top Five Signs You Probably Have Pancreatic Cancer"""



perform_search(list_or_words, search)
# a = TextSimilarity(list_or_words[0]['text'], search)
# print(a.evaluate())