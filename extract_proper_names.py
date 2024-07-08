import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords
from collections import defaultdict

def extract_proper_names(text):
    
    words = word_tokenize(text)
    tagged_words = pos_tag(words)
    named_entities = ne_chunk(tagged_words)
    proper_names = defaultdict(int)
    for entity in named_entities:
        if isinstance(entity, nltk.Tree):
            if entity.label() == 'PERSON':
                name = ' '.join([word for word, pos in entity.leaves()])
                proper_names[name] += 1
    
    return proper_names

def main():
    with open('document.txt', 'r') as file:
        document_text = file.read()
    proper_names = extract_proper_names(document_text)
    
    print("Proper names and their counts:")
    for name, count in proper_names.items():
        print(f"{name}: {count}")

if __name__ == "__main__":
    main()
