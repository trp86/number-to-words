from num2words import num2words
import importlib
import pkgutil
import num2words as n2w

def get_all_supported_languages():
    # Test each language with a simple number
    working_languages = {}
    test_number = 42
    
    # Try to get all language modules from num2words
    # This approach uses the CONVERTER_CLASSES dictionary from num2words
    try:
        from num2words.lang import CONVERTER_CLASSES
        languages = list(CONVERTER_CLASSES.keys())
    except ImportError:
        # Fallback to a predefined list of languages to try
        languages = [
            'am', 'ar', 'az', 'be', 'bn', 'ca', 'ce', 'cs', 'cy', 'da', 'de', 'en', 'es', 'et',
            'eu', 'fa', 'fi', 'fr', 'he', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'ka', 'kn', 'ko',
            'lt', 'lv', 'mk', 'mr', 'ms', 'mt', 'nl', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl',
            'sq', 'sr', 'sv', 'te', 'th', 'tr', 'uk', 'vi'
        ]
    
    print(f"Testing {len(languages)} languages...")
    
    for lang in sorted(languages):
        try:
            result = num2words(test_number, lang=lang)
            print(f"{lang}: {result}")
            working_languages[lang] = True
        except NotImplementedError:
            print(f"{lang}: Not implemented")
        except Exception as e:
            print(f"{lang}: Error - {str(e)}")
    
    return working_languages

# Get language names mapping
def get_language_names():
    return {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'pt': 'Portuguese',
        'ru': 'Russian',
        'ja': 'Japanese',
        'nl': 'Dutch',
        'ar': 'Arabic',
        'cs': 'Czech',
        'pl': 'Polish',
        'tr': 'Turkish',
        'ko': 'Korean',
        'he': 'Hebrew',
        'id': 'Indonesian',
        'uk': 'Ukrainian',
        'vi': 'Vietnamese',
        'lt': 'Lithuanian',
        'lv': 'Latvian',
        'ro': 'Romanian',
        'sl': 'Slovenian',
        'sr': 'Serbian',
        'sv': 'Swedish',
        'no': 'Norwegian',
        'da': 'Danish',
        'fi': 'Finnish',
        'hu': 'Hungarian',
        'az': 'Azerbaijani',
        'be': 'Belarusian',
        'bn': 'Bengali',
        'ca': 'Catalan',
        'cy': 'Welsh',
        'et': 'Estonian',
        'eu': 'Basque',
        'fa': 'Persian',
        'hy': 'Armenian',
        'is': 'Icelandic',
        'ka': 'Georgian',
        'kn': 'Kannada',
        'mk': 'Macedonian',
        'mr': 'Marathi',
        'ms': 'Malay',
        'mt': 'Maltese',
        'sk': 'Slovak',
        'sq': 'Albanian',
        'te': 'Telugu',
        'th': 'Thai',
        'am': 'Amharic',
        'ce': 'Chechen',
    }

# Get flag emojis for languages
def get_language_flags():
    return {
        'en': '🇺🇸',  # English - USA flag
        'es': '🇪🇸',  # Spanish - Spain flag
        'fr': '🇫🇷',  # French - France flag
        'de': '🇩🇪',  # German - Germany flag
        'it': '🇮🇹',  # Italian - Italy flag
        'pt': '🇵🇹',  # Portuguese - Portugal flag
        'ru': '🇷🇺',  # Russian - Russia flag
        'ja': '🇯🇵',  # Japanese - Japan flag
        'nl': '🇳🇱',  # Dutch - Netherlands flag
        'ar': '🇸🇦',  # Arabic - Saudi Arabia flag
        'cs': '🇨🇿',  # Czech - Czech Republic flag
        'pl': '🇵🇱',  # Polish - Poland flag
        'tr': '🇹🇷',  # Turkish - Turkey flag
        'ko': '🇰🇷',  # Korean - South Korea flag
        'he': '🇮🇱',  # Hebrew - Israel flag
        'id': '🇮🇩',  # Indonesian - Indonesia flag
        'uk': '🇺🇦',  # Ukrainian - Ukraine flag
        'vi': '🇻🇳',  # Vietnamese - Vietnam flag
        'lt': '🇱🇹',  # Lithuanian - Lithuania flag
        'lv': '🇱🇻',  # Latvian - Latvia flag
        'ro': '🇷🇴',  # Romanian - Romania flag
        'sl': '🇸🇮',  # Slovenian - Slovenia flag
        'sr': '🇷🇸',  # Serbian - Serbia flag
        'sv': '🇸🇪',  # Swedish - Sweden flag
        'no': '🇳🇴',  # Norwegian - Norway flag
        'da': '🇩🇰',  # Danish - Denmark flag
        'fi': '🇫🇮',  # Finnish - Finland flag
        'hu': '🇭🇺',  # Hungarian - Hungary flag
        'az': '🇦🇿',  # Azerbaijani - Azerbaijan flag
        'be': '🇧🇾',  # Belarusian - Belarus flag
        'bn': '🇧🇩',  # Bengali - Bangladesh flag
        'ca': '🇪🇸',  # Catalan - Spain flag (using Spain as fallback)
        'cy': '🇬🇧',  # Welsh - UK flag
        'et': '🇪🇪',  # Estonian - Estonia flag
        'eu': '🇪🇸',  # Basque - Spain flag (using Spain as fallback)
        'fa': '🇮🇷',  # Persian - Iran flag
        'hy': '🇦🇲',  # Armenian - Armenia flag
        'is': '🇮🇸',  # Icelandic - Iceland flag
        'ka': '🇬🇪',  # Georgian - Georgia flag
        'kn': '🇮🇳',  # Kannada - India flag
        'mk': '🇲🇰',  # Macedonian - North Macedonia flag
        'mr': '🇮🇳',  # Marathi - India flag
        'ms': '🇲🇾',  # Malay - Malaysia flag
        'mt': '🇲🇹',  # Maltese - Malta flag
        'sk': '🇸🇰',  # Slovak - Slovakia flag
        'sq': '🇦🇱',  # Albanian - Albania flag
        'te': '🇮🇳',  # Telugu - India flag
        'th': '🇹🇭',  # Thai - Thailand flag
        'am': '🇪🇹',  # Amharic - Ethiopia flag
        'ce': '🇷🇺',  # Chechen - Russia flag (using Russia as fallback)
    }

if __name__ == "__main__":
    # Get all supported languages
    supported_languages = get_all_supported_languages()
    language_names = get_language_names()
    language_flags = get_language_flags()
    
    print("\nSupported Languages:")
    for code in sorted(supported_languages.keys()):
        name = language_names.get(code, code.upper())
        flag = language_flags.get(code, '')
        print(f"    '{code}': '{name}',  # {flag}")
    
    print("\nLanguage Flags:")
    for code in sorted(supported_languages.keys()):
        flag = language_flags.get(code, '')
        if flag:
            print(f"    '{code}': '{flag}',")
        else:
            print(f"    '{code}': '',  # No flag found")