import json
import genanki
from gtts import gTTS
import os

# Define the Anki Note Model
MODEL_ID = 1607392319
DECK_ID = 2059400110

my_model = genanki.Model(
  MODEL_ID,
  'Simple Japanese Model',
  fields=[
    {'name': 'Kanji'},
    {'name': 'Hiragana'},
    {'name': 'Meaning'},
    {'name': 'Extra'},
    {'name': 'Audio'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '<div style="font-size: 30px;">{{Kanji}}</div>',
      'afmt': '''{{FrontSide}}
                 <hr id=answer>
                 <div style="font-size: 20px;">{{Hiragana}}</div>
                 <br>
                 <div>{{Meaning}}</div>
                 <br>
                 <div style="color: gray; font-size: 15px;">{{Extra}}</div>
                 <br>
                 {{Audio}}''',
    },
  ])

# Initialize the Deck
my_deck = genanki.Deck(
  DECK_ID,
  'Japanese Vocabulary')



def generate_audio(text, filename):
    """Generates Japanese audio for the given text using gTTS."""
    try:
        tts = gTTS(text=text, lang='ja')
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"Error in gTTS: {e}")
        return None

def main():
    # Load data
    data_path = 'data/counters.json'
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {data_path} not found.")
        return

    media_files = []

    for item in data:
        kanji = item.get('kanji', '')
        hiragana = item.get('hiragana', '')
        meaning = item.get('meaning', '')
        extra = item.get('extra', '')
        item_id = item.get('id', '')

        # Generate Audio
        # Using Kanji for audio to preserve pitch accent
        audio_source = kanji if kanji else hiragana
        # gTTS outputs MP3
        audio_filename = f'audio_{item_id}.mp3'
        
        print(f"Generating audio for: {audio_source}...")
        try:
            if generate_audio(audio_source, audio_filename):
                media_files.append(audio_filename)
            else:
                print(f"Warning: No audio generated for {audio_source}")
        except Exception as e:
            print(f"Error generating audio for {audio_source}: {e}")
            continue

        # Create Note
        note = genanki.Note(
            model=my_model,
            fields=[kanji, hiragana, meaning, extra, f'[sound:{audio_filename}]']
        )
        my_deck.add_note(note)

    # Export Deck
    output_file = 'japanese_deck.apkg'
    package = genanki.Package(my_deck)
    package.media_files = media_files
    package.write_to_file(output_file)
    
    print(f"Deck generated successfully: {output_file}")

    # Cleanup audio files
    print("Cleaning up temporary audio files...")
    for file in media_files:
        if os.path.exists(file):
            os.remove(file)
    print("Done.")

if __name__ == '__main__':
    main()
