def langRu(): return "Привет, мир!"
def langEn(): return "Hello, World!"
def langJp(): return "「こんにちは世界!」"

def main(lang):
    if lang == "ru":
        return langRu
    
    elif lang == "en":
        return langEn
    
    elif lang == "jp":
        return langJp
    
    else:
        return langRu

result = main("ru")
print(result())

result = main("en")
print(result())

result = main("jp")
print(result())