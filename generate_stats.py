from datetime import datetime

class AboutMe:
    def __init__(self):
        self.name = "Nyctophile Schizophrenia."
        self.username = "NyctophileXNIKA"
        self.birth_year = 2009
        self.age = datetime.now().year - self.birth_year
        self.language = ["Python", "Bash", "JavaScript"]
        self.interests = ["Automation", "Obfuscation", "Cybersecurity"]
        self.hobby = ["Listening to Lofi 🎧", "Coding at night 🌙"]

    def contact(self):
        socials = {
            "🐙 GitHub"    : "https://github.com/NyctophileXNIKA",
            "📸 Instagram" : "https://instagram.com/v3n.ryougaa",
            "📘 Facebook"  : "https://www.facebook.com/Nyctophile.Schizophrenia",
            }
        return socials

me = AboutMe()
print(f"Hi, I'm {me.name}, {me.age} years old! 🚀")
print("Feel free to explore my repositories and connect with me online ✨")
