#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NxYFLuX Nick Oluşturma Tool
==========================
Normal ve şekilli nick oluşturma aracı
Version: 1.0
License: MIT
by SeRCaN BeY
Telegram@nxyflux
"""

import random
import sys
import os
from datetime import datetime

class NickGenerator:
    def __init__(self):
        
        self.stylish_fonts = {
            'bold': {
                'a': '𝗮', 'b': '𝗯', 'c': '𝗰', 'd': '𝗱', 'e': '𝗲', 'f': '𝗳',
                'g': '𝗴', 'h': '𝗵', 'i': '𝗶', 'j': '𝗷', 'k': '𝗸', 'l': '𝗹',
                'm': '𝗺', 'n': '𝗻', 'o': '𝗼', 'p': '𝗽', 'q': '𝗾', 'r': '𝗿',
                's': '𝘀', 't': '𝘁', 'u': '𝘂', 'v': '𝘃', 'w': '𝘄', 'x': '𝘅',
                'y': '𝘆', 'z': '𝘇',
                'A': '𝗔', 'B': '𝗕', 'C': '𝗖', 'D': '𝗗', 'E': '𝗘', 'F': '𝗙',
                'G': '𝗚', 'H': '𝗛', 'I': '𝗜', 'J': '𝗝', 'K': '𝗞', 'L': '𝗟',
                'M': '𝗠', 'N': '𝗡', 'O': '𝗢', 'P': '𝗣', 'Q': '𝗤', 'R': '𝗥',
                'S': '𝗦', 'T': '𝗧', 'U': '𝗨', 'V': '𝗩', 'W': '𝗪', 'X': '𝗫',
                'Y': '𝗬', 'Z': '𝗭'
            },
            'italic': {
                'a': '𝘢', 'b': '𝘣', 'c': '𝘤', 'd': '𝘥', 'e': '𝘦', 'f': '𝘧',
                'g': '𝘨', 'h': '𝘩', 'i': '𝘪', 'j': '𝘫', 'k': '𝘬', 'l': '𝘭',
                'm': '𝘮', 'n': '𝘯', 'o': '𝘰', 'p': '𝘱', 'q': '𝘲', 'r': '𝘳',
                's': '𝘴', 't': '𝘵', 'u': '𝘶', 'v': '𝘷', 'w': '𝘸', 'x': '𝘹',
                'y': '𝘺', 'z': '𝘻',
                'A': '𝘈', 'B': '𝘉', 'C': '𝘊', 'D': '𝘋', 'E': '𝘌', 'F': '𝘍',
                'G': '𝘎', 'H': '𝘏', 'I': '𝘐', 'J': '𝘑', 'K': '𝘒', 'L': '𝘓',
                'M': '𝘔', 'N': '𝘕', 'O': '𝘖', 'P': '𝘗', 'Q': '𝘘', 'R': '𝘙',
                'S': '𝘚', 'T': '𝘛', 'U': '𝘜', 'V': '𝘝', 'W': '𝘞', 'X': '𝘟',
                'Y': '𝘠', 'Z': '𝘡'
            },
            'script': {
                'a': '𝓪', 'b': '𝓫', 'c': '𝓬', 'd': '𝓭', 'e': '𝓮', 'f': '𝓯',
                'g': '𝓰', 'h': '𝓱', 'i': '𝓲', 'j': '𝓳', 'k': '𝓴', 'l': '𝓵',
                'm': '𝓶', 'n': '𝓷', 'o': '𝓸', 'p': '𝓹', 'q': '𝓺', 'r': '𝓻',
                's': '𝓼', 't': '𝓽', 'u': '𝓾', 'v': '𝓿', 'w': '𝔀', 'x': '𝔁',
                'y': '𝔂', 'z': '𝔃',
                'A': '𝓐', 'B': '𝓑', 'C': '𝓒', 'D': '𝓓', 'E': '𝓔', 'F': '𝓕',
                'G': '𝓖', 'H': '𝓗', 'I': '𝓘', 'J': '𝓙', 'K': '𝓚', 'L': '𝓛',
                'M': '𝓜', 'N': '𝓝', 'O': '𝓞', 'P': '𝓟', 'Q': '𝓠', 'R': '𝓡',
                'S': '𝓢', 'T': '𝓣', 'U': '𝓤', 'V': '𝓥', 'W': '𝓦', 'X': '𝓧',
                'Y': '𝓨', 'Z': '𝓩'
            },
            'fraktur': {
                'a': '𝔞', 'b': '𝔟', 'c': '𝔠', 'd': '𝔡', 'e': '𝔢', 'f': '𝔣',
                'g': '𝔤', 'h': '𝔥', 'i': '𝔦', 'j': '𝔧', 'k': '𝔨', 'l': '𝔩',
                'm': '𝔪', 'n': '𝔫', 'o': '𝔬', 'p': '𝔭', 'q': '𝔮', 'r': '𝔯',
                's': '𝔰', 't': '𝔱', 'u': '𝔲', 'v': '𝔳', 'w': '𝔴', 'x': '𝔵',
                'y': '𝔶', 'z': '𝔷',
                'A': '𝔄', 'B': '𝔅', 'C': 'ℭ', 'D': '𝔇', 'E': '𝔈', 'F': '𝔉',
                'G': '𝔊', 'H': 'ℌ', 'I': 'ℑ', 'J': '𝔍', 'K': '𝔎', 'L': '𝔏',
                'M': '𝔐', 'N': '𝔑', 'O': '𝔒', 'P': '𝔓', 'Q': '𝔔', 'R': 'ℜ',
                'S': '𝔖', 'T': '𝔗', 'U': '𝔘', 'V': '𝔙', 'W': '𝔚', 'X': '𝔛',
                'Y': '𝔜', 'Z': 'ℨ'
            },
            'double_struck': {
                'a': '𝕒', 'b': '𝕓', 'c': '𝕔', 'd': '𝕕', 'e': '𝕖', 'f': '𝕗',
                'g': '𝕘', 'h': '𝕙', 'i': '𝕚', 'j': '𝕛', 'k': '𝕜', 'l': '𝕝',
                'm': '𝕞', 'n': '𝕟', 'o': '𝕠', 'p': '𝕡', 'q': '𝕢', 'r': '𝕣',
                's': '𝕤', 't': '𝕥', 'u': '𝕦', 'v': '𝕧', 'w': '𝕨', 'x': '𝕩',
                'y': '𝕪', 'z': '𝕫',
                'A': '𝔸', 'B': '𝔹', 'C': 'ℂ', 'D': '𝔻', 'E': '𝔼', 'F': '𝔽',
                'G': '𝔾', 'H': 'ℍ', 'I': '𝕀', 'J': '𝕁', 'K': '𝕂', 'L': '𝕃',
                'M': '𝕄', 'N': 'ℕ', 'O': '𝕆', 'P': 'ℙ', 'Q': 'ℚ', 'R': 'ℝ',
                'S': '𝕊', 'T': '𝕋', 'U': '𝕌', 'V': '𝕍', 'W': '𝕎', 'X': '𝕏',
                'Y': '𝕐', 'Z': 'ℤ'
            },
            'cursive': {
                'a': '𝒶', 'b': '𝒷', 'c': '𝒸', 'd': '𝒹', 'e': '𝑒', 'f': '𝒻',
                'g': '𝑔', 'h': '𝒽', 'i': '𝒾', 'j': '𝒿', 'k': '𝓀', 'l': '𝓁',
                'm': '𝓂', 'n': '𝓃', 'o': '𝑜', 'p': '𝓅', 'q': '𝓆', 'r': '𝓇',
                's': '𝓈', 't': '𝓉', 'u': '𝓊', 'v': '𝓋', 'w': '𝓌', 'x': '𝓍',
                'y': '𝓎', 'z': '𝓏',
                'A': '𝒜', 'B': 'ℬ', 'C': '𝒞', 'D': '𝒟', 'E': 'ℰ', 'F': 'ℱ',
                'G': '𝒢', 'H': 'ℋ', 'I': 'ℐ', 'J': '𝒥', 'K': '𝒦', 'L': 'ℒ',
                'M': 'ℳ', 'N': '𝒩', 'O': '𝒪', 'P': '𝒫', 'Q': '𝒬', 'R': 'ℛ',
                'S': '𝒮', 'T': '𝒯', 'U': '𝒰', 'V': '𝒱', 'W': '𝒲', 'X': '𝒳',
                'Y': '𝒴', 'Z': '𝒵'
            },
            'small_caps': {
                'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ғ',
                'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ',
                'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ',
                's': 's', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x',
                'y': 'ʏ', 'z': 'ᴢ'
            },
            'bubble': {
                'a': 'ⓐ', 'b': 'ⓑ', 'c': 'ⓒ', 'd': 'ⓓ', 'e': 'ⓔ', 'f': 'ⓕ',
                'g': 'ⓖ', 'h': 'ⓗ', 'i': 'ⓘ', 'j': 'ⓙ', 'k': 'ⓚ', 'l': 'ⓛ',
                'm': 'ⓜ', 'n': 'ⓝ', 'o': 'ⓞ', 'p': 'ⓟ', 'q': 'ⓠ', 'r': 'ⓡ',
                's': 'ⓢ', 't': 'ⓣ', 'u': 'ⓤ', 'v': 'ⓥ', 'w': 'ⓦ', 'x': 'ⓧ',
                'y': 'ⓨ', 'z': 'ⓩ',
                'A': 'Ⓐ', 'B': 'Ⓑ', 'C': 'Ⓒ', 'D': 'Ⓓ', 'E': 'Ⓔ', 'F': 'Ⓕ',
                'G': 'Ⓖ', 'H': 'Ⓗ', 'I': 'Ⓘ', 'J': 'Ⓙ', 'K': 'Ⓚ', 'L': 'Ⓛ',
                'M': 'Ⓜ', 'N': 'Ⓝ', 'O': 'Ⓞ', 'P': 'Ⓟ', 'Q': 'Ⓠ', 'R': 'Ⓡ',
                'S': 'Ⓢ', 'T': 'Ⓣ', 'U': 'Ⓤ', 'V': 'Ⓥ', 'W': 'Ⓦ', 'X': 'Ⓧ',
                'Y': 'Ⓨ', 'Z': 'Ⓩ'
            },
            'square': {
                'a': '🄰', 'b': '🄱', 'c': '🄲', 'd': '🄳', 'e': '🄴', 'f': '🄵',
                'g': '🄶', 'h': '🄷', 'i': '🄸', 'j': '🄹', 'k': '🄺', 'l': '🄻',
                'm': '🄼', 'n': '🄽', 'o': '🄾', 'p': '🄿', 'q': '🅀', 'r': '🅁',
                's': '🅂', 't': '🅃', 'u': '🅄', 'v': '🅅', 'w': '🅆', 'x': '🅇',
                'y': '🅈', 'z': '🅉'
            }
        }
        
        self.prefixes = [
            'xX', 'Xx', 'The', 'Mr', 'Ms', 'Dr', 'Pro', 'Noob', 'King', 'Queen',
            'Lord', 'Dark', 'Light', 'Shadow', 'Ghost', 'Night', 'Day', 'Cyber',
            'Neo', 'Super', 'Ultra', 'Mega', 'Hyper', 'i', 'e', 'o', 'a'
        ]
        
        self.suffixes = [
            'Xx', 'xX', 'TR', 'TM', 'HQ', 'OP', 'GG', 'YT', 'TV', 'HQ',
            'Pro', 'Noob', 'God', 'Dev', 'Mod', 'Admin', 'User', 'Gamer',
            '123', '007', '999', '666', '777', '88', '21', '99', '01'
        ]
        
        self.symbols = ['☆', '★', '♛', '♚', '♕', '♔', '⚡', '🔥', '❄️', '☠️', 
                       '⚔️', '🛡️', '🎯', '🎮', '👑', '💀', '🐉', '🐺', '🦅', '🦁']
        
        self.adjectives = [
            'Dark', 'Light', 'Shadow', 'Ghost', 'Silent', 'Deadly', 'Swift',
            'Fierce', 'Brave', 'Clever', 'Wild', 'Crazy', 'Cool', 'Hot',
            'Frozen', 'Burning', 'Hidden', 'Secret', 'Mystic', 'Magic'
        ]
        
        self.nouns = [
            'Hunter', 'Warrior', 'Ninja', 'Samurai', 'Knight', 'Dragon',
            'Wolf', 'Eagle', 'Tiger', 'Lion', 'Bear', 'Shark', 'Snake',
            'Raven', 'Phoenix', 'Demon', 'Angel', 'Ghost', 'Shadow', 'Storm'
        ]
        
        self.generated_nicks = []
    
    def clear_screen(self):
        """Ekranı temizle"""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def print_banner(self):
        """Banner göster"""
        banner = """
╔══════════════════════════════════════════╗
║     🎮 NxYFLuX Nick Oluşturma Tool 🎮     ║
║                                          ║
║   Normal & Şekilli Nick Oluşturucu      ║
║          Version: 1.0                   ║
╚══════════════════════════════════════════╝
        """
        print(banner)
    
    def to_stylish(self, text, style='bold'):
        """Metni şekilli fonta çevir"""
        if style not in self.stylish_fonts:
            return text
        
        result = ''
        for char in text:
            result += self.stylish_fonts[style].get(char, char)
        return result
    
    def generate_normal_nick(self, base_name=None, add_numbers=True, 
                            add_prefix=False, add_suffix=False):
        """Normal nick oluştur"""
        if base_name is None:
            adj = random.choice(self.adjectives)
            noun = random.choice(self.nouns)
            base = adj + noun
        else:
            base = base_name
        
        if add_prefix and random.choice([True, False]):
            base = random.choice(self.prefixes) + base
        
        if add_suffix and random.choice([True, False]):
            base = base + random.choice(self.suffixes)
        
        if add_numbers and random.choice([True, False]):
            base += str(random.randint(1, 999))
        
        return base
    
    def generate_stylish_nick(self, text=None, style=None, add_symbols=True):
        """Şekilli nick oluştur"""
        if text is None:
            text = self.generate_normal_nick()
        
        if style is None:
            style = random.choice(list(self.stylish_fonts.keys()))
        
        stylish_text = self.to_stylish(text, style)
        
        if add_symbols and random.choice([True, False]):
            symbol = random.choice(self.symbols)
            position = random.choice(['prefix', 'suffix', 'both'])
            
            if position == 'prefix':
                stylish_text = symbol + stylish_text
            elif position == 'suffix':
                stylish_text = stylish_text + symbol
            else:
                stylish_text = symbol + stylish_text + symbol
        
        return stylish_text
    
    def generate_mixed_nick(self):
        """Karışık stil nick oluştur"""
        base = self.generate_normal_nick()
        
        
        mid = len(base) // 2
        first_half = self.to_stylish(base[:mid], random.choice(list(self.stylish_fonts.keys())))
        second_half = self.to_stylish(base[mid:], random.choice(list(self.stylish_fonts.keys())))
        
        result = first_half + second_half
        
        
        if random.choice([True, False]):
            result = random.choice(self.symbols) + result
        
        return result
    
    def generate_leet_nick(self, text=None):
        """Leet speak nick oluştur"""
        if text is None:
            text = self.generate_normal_nick()
        
        leet_map = {
            'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5',
            't': '7', 'l': '1', 'g': '9', 'b': '8', 'z': '2',
            'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5',
            'T': '7', 'L': '1', 'G': '9', 'B': '8', 'Z': '2'
        }
        
        result = ''
        for char in text:
            if random.choice([True, False]) and char in leet_map:
                result += leet_map[char]
            else:
                result += char
        
        return result
    
    def save_to_file(self, filename='generated_nicks.txt'):
        """Oluşturulan nickleri dosyaya kaydet"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 50 + "\n\n")
                for i, nick in enumerate(self.generated_nicks, 1):
                    f.write(f"{i}. {nick}\n")
            print(f"✅ Nickler '{filename}' dosyasına kaydedildi!")
        except Exception as e:
            print(f"❌ Kaydetme hatası: {e}")
    
    def show_menu(self):
        """Ana menü"""
        self.clear_screen()
        self.print_banner()
        
        print("""
┌─────────────────────────────────────┐
│         📋 ANA MENÜ                 │
├─────────────────────────────────────┤
│  [1] 🎲 Rastgele Normal Nick        │
│  [2] ✨ Rastgele Şekilli Nick       │
│  [3] 🎨 Belirli Stilde Nick         │
│  [4] 🔤 Kendi İsminle Nick          │
│  [5] 🔄 Karışık Stil Nick           │
│  [6] 💻 Leet Speak Nick             │
│  [7] 📊 Toplu Üret (10 adet)        │
│  [8] 💾 Dosyaya Kaydet              │
│  [9] 📜 Kayıtlı Nickleri Göster     │
│  [0] ❌ Çıkış                       │
└─────────────────────────────────────┘
        """)
        
        choice = input("➤ Seçiminiz: ").strip()
        return choice
    
    def run(self):
        """Ana program döngüsü"""
        while True:
            choice = self.show_menu()
            
            if choice == '1':
                nick = self.generate_normal_nick()
                self.generated_nicks.append(nick)
                print(f"\n🎲 Normal Nick: {nick}")
                input("\nDevam etmek için ENTER'a bas...")
            
            elif choice == '2':
                nick = self.generate_stylish_nick()
                self.generated_nicks.append(nick)
                print(f"\n✨ Şekilli Nick: {nick}")
                input("\nDevam etmek için ENTER'a bas...")
            
            elif choice == '3':
                print("\n📋 Mevcut Stiller:")
                styles = list(self.stylish_fonts.keys())
                for i, style in enumerate(styles, 1):
                    print(f"  {i}. {style.title()}")
                
                try:
                    style_idx = int(input("\nStil numarası: ")) - 1
                    if 0 <= style_idx < len(styles):
                        text = input("İsim girin (boş bırak=random): ").strip()
                        if not text:
                            text = None
                        nick = self.generate_stylish_nick(text, styles[style_idx])
                        self.generated_nicks.append(nick)
                        print(f"\n🎨 {styles[style_idx].title()} Nick: {nick}")
                    else:
                        print("❌ Geçersiz stil!")
                except ValueError:
                    print("❌ Geçersiz giriş!")
                input("\nDevam etmek için ENTER'a bas...")
            
            elif choice == '4':
                name = input("\nİsminizi girin: ").strip()
                if name:
                    print("\n🔄 Stil seçenekleri:")
                    print("  1. Normal")
                    print("  2. Şekilli (Random)")
                    print("  3. Leet Speak")
                    style_choice = input("Seçim (1-3): ").strip()
                    
                    if style_choice == '1':
                        nick = self.generate_normal_nick(name)
                    elif style_choice == '2':
                        nick = self.generate_stylish_nick(name)
                    elif style_choice == '3':
                        nick = self.generate_leet_nick(name)
                    else:
                        nick = self.generate_stylish_nick(name)
                    
                    self.generated_nicks.append(nick)
                    print(f"\n🔤 Sonuç: {nick}")
                else:
                    print("❌ İsim boş olamaz!")
                input("\nDevam etmek için ENTER'a bas...")
            
            elif choice == '5':
                nick = self.generate_mixed_nick()
                self.generated_nicks.append(nick)
                print(f"\n🔄 Karışık Stil: {nick}")
                input("\nDevam etmek için ENTER'a bas...")
            
            elif choice == '6':
                nick = self.generate_leet_nick()
                self.generated_nicks.append(nick)
                print(f"\n💻 Leet Speak: {nick}")
                input("\nDevam etmek için ENTER'a bas...")
            
            elif choice == '7':
                print("\n📊 10 Adet Rastgele Nick:")
                print("-" * 40)
                for i in range(10):
                    nick_type = random.choice(['normal', 'stylish', 'mixed', 'leet'])
                    if nick_type == 'normal':
                        nick = self.generate_normal_nick()
                    elif nick_type == 'stylish':
                        nick = self.generate_stylish_nick()
                    elif nick_type == 'mixed':
                        nick = self.generate_mixed_nick()
                    else:
                        nick = self.generate_leet_nick()
                    
                    self.generated_nicks.append(nick)
                    print(f"  {i+1}. {nick}")
                input("\nDevam etmek için ENTER'a bas...")
            
            elif choice == '8':
                if self.generated_nicks:
                    filename = input("Dosya adı (varsayılan: oyun_isimler.txt): ").strip()
                    if not filename:
                        filename = 'generated_nicks.txt'
                    self.save_to_file(filename)
                else:
                    print("❌ Kaydedilecek nick yok!")
                input("\nDevam etmek için ENTER'a bas...")
            
            elif choice == '9':
                if self.generated_nicks:
                    print("\n📜 Kayıtlı Nickler:")
                    print("-" * 40)
                    for i, nick in enumerate(self.generated_nicks[-20:], 1):
                        print(f"  {i}. {nick}")
                else:
                    print("❌ Henüz nick oluşturulmadı!")
                input("\nDevam etmek için ENTER'a bas...")
            
            elif choice == '0':
                print("\n👋 Güle güle!")
                sys.exit(0)
            
            else:
                print("❌ Geçersiz seçim!")
                input("\nDevam etmek için ENTER'a bas...")


def main():
    """Ana fonksiyon"""
    try:
        generator = NickGenerator()
        generator.run()
    except KeyboardInterrupt:
        print("\n\n👋 Program sonlandırıldı.")
        sys.exit(0)


if __name__ == "__main__":
    main()
    
