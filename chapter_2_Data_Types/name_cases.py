person_name = "Eric"
print(f"Hello, {person_name}, would you like to learn some Python today?")

print(f"\n{person_name.title()}")
print(f"{person_name.lower()}")
print(f"{person_name.upper()}\n")
print(person_name.title())
print(person_name.lower())
print(person_name.upper())

famous_quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"
print(f'{author.title()} once said, "{famous_quote}"\n')

message = f'{author.title()} once said, "{famous_quote}"'
print(message)

person_name = "  Tim Horth  "
print(person_name.strip())
print(person_name.rstrip())
print(person_name.lstrip())