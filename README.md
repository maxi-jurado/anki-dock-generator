# Anki Deck Generator

This tool generates Anki flashcards from a JSON data source, including audio generated using Google Text-to-Speech (gTTS).

## 🇬🇧 English

### Description

A Python script that creates `.apkg` files for Anki. It reads vocabulary from a JSON file, generates audio for the Kanji (to preserve pitch accent), and packages it all into a deck.

### Installation

1. Ensure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Place your data in `data/counters.json`.
2. Run the script:
   ```bash
   python main.py
   ```
3. The deck will be saved as `japanese_deck.apkg`.

---

## 🇪🇸 Español

### Descripción

Un script de Python que crea archivos `.apkg` para Anki. Lee vocabulario desde un archivo JSON, genera audio para los Kanji (para preservar el acento tonal) y lo empaqueta todo en un mazo.

### Instalación

1. Asegúrate de tener Python instalado.
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

### Uso

1. Coloca tus datos en `data/counters.json`.
2. Ejecuta el script:
   ```bash
   python main.py
   ```
3. El mazo se guardará como `japanese_deck.apkg`.

---

## 🇯🇵 日本語 (Basic)

### 概要 (Overview)

JSON データから Anki デッキ (`.apkg`) を作成するツールです。gTTS を使って漢字の音声を生成します。

### インストール (Installation)

1. Python をインストールしてください。
2. 必要なライブラリをインストールします:
   ```bash
   pip install -r requirements.txt
   ```

### 使い方 (Usage)

1. `data/counters.json` にデータを置きます。
2. スクリプトを実行します:
   ```bash
   python main.py
   ```
3. `japanese_deck.apkg` というファイルが作成されます。
