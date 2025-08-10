from flask import Flask, jsonify, request
from flask_cors import CORS
from num2words import num2words
import json

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# List of languages supported by num2words based on testing
# These languages are confirmed to be implemented in the num2words library
SUPPORTED_LANGUAGES = {
    'am': 'Amharic',
    'ar': 'Arabic',
    'az': 'Azerbaijani',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'ca': 'Catalan',
    'ce': 'Chechen',
    'cs': 'Czech',
    'cy': 'Welsh',
    'da': 'Danish',
    'de': 'German',
    'en': 'English',
    'es': 'Spanish',
    'fa': 'Persian',
    'fi': 'Finnish',
    'fr': 'French',
    'he': 'Hebrew',
    'hu': 'Hungarian',
    'id': 'Indonesian',
    'is': 'Icelandic',
    'it': 'Italian',
    'ja': 'Japanese',
    'kn': 'Kannada',
    'ko': 'Korean',
    'lt': 'Lithuanian',
    'lv': 'Latvian',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'sr': 'Serbian',
    'sv': 'Swedish',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'vi': 'Vietnamese'
}

# Language to flag emoji mapping
LANGUAGE_FLAGS = {
    'am': '🇪🇹',  # Amharic - Ethiopia flag
    'ar': '🇸🇦',  # Arabic - Saudi Arabia flag
    'az': '🇦🇿',  # Azerbaijani - Azerbaijan flag
    'be': '🇧🇾',  # Belarusian - Belarus flag
    'bn': '🇧🇩',  # Bengali - Bangladesh flag
    'ca': '🇪🇸',  # Catalan - Spain flag (using Spain as fallback)
    'ce': '🇷🇺',  # Chechen - Russia flag (using Russia as fallback)
    'cs': '🇨🇿',  # Czech - Czech Republic flag
    'cy': '🇬🇧',  # Welsh - UK flag
    'da': '🇩🇰',  # Danish - Denmark flag
    'de': '🇩🇪',  # German - Germany flag
    'en': '🇺🇸',  # English - USA flag
    'es': '🇪🇸',  # Spanish - Spain flag
    'fa': '🇮🇷',  # Persian - Iran flag
    'fi': '🇫🇮',  # Finnish - Finland flag
    'fr': '🇫🇷',  # French - France flag
    'he': '🇮🇱',  # Hebrew - Israel flag
    'hu': '🇭🇺',  # Hungarian - Hungary flag
    'id': '🇮🇩',  # Indonesian - Indonesia flag
    'is': '🇮🇸',  # Icelandic - Iceland flag
    'it': '🇮🇹',  # Italian - Italy flag
    'ja': '🇯🇵',  # Japanese - Japan flag
    'kn': '🇮🇳',  # Kannada - India flag
    'ko': '🇰🇷',  # Korean - South Korea flag
    'lt': '🇱🇹',  # Lithuanian - Lithuania flag
    'lv': '🇱🇻',  # Latvian - Latvia flag
    'nl': '🇳🇱',  # Dutch - Netherlands flag
    'no': '🇳🇴',  # Norwegian - Norway flag
    'pl': '🇵🇱',  # Polish - Poland flag
    'pt': '🇵🇹',  # Portuguese - Portugal flag
    'ro': '🇷🇴',  # Romanian - Romania flag
    'ru': '🇷🇺',  # Russian - Russia flag
    'sk': '🇸🇰',  # Slovak - Slovakia flag
    'sl': '🇸🇮',  # Slovenian - Slovenia flag
    'sr': '🇷🇸',  # Serbian - Serbia flag
    'sv': '🇸🇪',  # Swedish - Sweden flag
    'te': '🇮🇳',  # Telugu - India flag
    'th': '🇹🇭',  # Thai - Thailand flag
    'tr': '🇹🇷',  # Turkish - Turkey flag
    'uk': '🇺🇦',  # Ukrainian - Ukraine flag
    'vi': '🇻🇳'   # Vietnamese - Vietnam flag
}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/languages', methods=['GET'])
def get_languages():
    languages = []
    for code, name in SUPPORTED_LANGUAGES.items():
        languages.append({
            'code': code,
            'name': name,
            'flag': LANGUAGE_FLAGS.get(code, '')
        })
    return jsonify(languages)

@app.route('/api/convert', methods=['POST'])
def convert_number():
    data = request.get_json()
    
    if not data or 'number' not in data or 'language' not in data:
        return jsonify({'error': 'Missing number or language parameter'}), 400
    
    try:
        number = float(data['number'])
        language = data['language']
        
        if language not in SUPPORTED_LANGUAGES:
            return jsonify({'error': f'Language {language} not supported'}), 400
        
        # Check if the number is too large
        if abs(number) > 10**15:
            return jsonify({'error': 'Number too large (max 15 digits)'}), 400
        
        # Convert the number to words
        words = num2words(number, lang=language)
        
        return jsonify({
            'number': data['number'],
            'language': language,
            'words': words
        })
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400
    except NotImplementedError:
        return jsonify({'error': f'Language {language} not implemented'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)