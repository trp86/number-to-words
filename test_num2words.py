from num2words import num2words

# Define a list of languages to test
languages_to_test = [
    'en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'ja', 'zh', 'hi',
    'nl', 'ar', 'cs', 'pl', 'tr', 'ko', 'he', 'id', 'uk', 'vi'
]

# Test conversion in different languages
test_number = 42
print(f"Testing conversion of {test_number} in different languages:")
for lang in languages_to_test:
    try:
        result = num2words(test_number, lang=lang)
        print(f"{lang}: {result}")
    except NotImplementedError:
        print(f"{lang}: Not implemented")
    except Exception as e:
        print(f"{lang}: Error - {str(e)}")