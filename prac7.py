mystery = '\U0001f4a9'
print(mystery)


import unicodedata
print(unicodedata.name(mystery))


pop_bytes = mystery.encode('utf-8')
print(pop_bytes)


pop_string = pop_bytes.decode('utf-8')
print(pop_string)

print(pop_string == mystery)


poem = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s."""

print(poem % ('roast beef', 'ham', 'head', 'clam'))


letter = """Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""

response = {
    'salutation': 'Mr.',
    'name': 'Mellstroy',
    'product': 'toaster',
    'verbed': 'exploded',
    'room': 'bathroom',
    'animals': 'hamsters',
    'amount': '$15.00',
    'percent': '99',
    'spokesman': 'Drun',
    'job_title': 'Customer Success Manager'
}

print(letter.format(**response))


mammoth = """
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.
"""
import re
words_with_c = re.findall(r'\b[c]\w*', mammoth)
print(f"Починаються на 'с': {words_with_c}")


words4_with_c = re.findall(r'\b[c]\w{3}\b', mammoth)
print(f"Чотирибуквені на 'c': {words4_with_c}")


words_last_r = re.findall(r'\b\w*[r]\b', mammoth)
print(f"Закінчуються на 'r': {words_last_r}")


words_tripl = re.findall(r'\b\w*[aeiouAEIOU]{3}\w*\b', mammoth)
print(f"Три голосні підряд: {words_tripl}")


from binascii import unhexlify

hex_string = (
    '4749463839610100010080000000000000ffffff21f9' +
    '0401000000002c000000000100010000020144003b'
)

gif = unhexlify(hex_string)

print(f"Тип змінної: {type(gif)}")
print(f"Дані: {gif}")


header = gif[:6]
is_correct = header == b'GIF89a'

print(f"Заголовок: {header}")
print(f"Чи є файл коректним? {'Так' if is_correct else 'Ні'}")

import struct

width = struct.unpack_from('<H', gif, 6)[0]

height = struct.unpack_from('<H', gif, 8)[0]

print(f"Ширина: {width}")
print(f"Висота: {height}")
print(f"Чи дорівнюють вони 1? {'Так' if width == 1 and height == 1 else 'Ні'}")