import os

def top_py_fayllar(papka_yol):
    py_fayllar = []
    for papka, kataloglar, fayllar in os.walk(papka_yol):
        for fayl in fayllar:
            if fayl.endswith('.py'):
                py_fayllar.append(os.path.join(papka, fayl))
    return py_fayllar

papka_yol = '/path/to/papka'  # papka_yolni o'zgartiring
print(top_py_fayllar(papka_yol))
```

Kodni ishlatish uchun, `/path/to/papka` ni o'z papkangizga o'zgartiring.
