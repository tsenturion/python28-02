age = 22
has_ticket = True
is_blocked = False
is_adult = age >= 18
can_enter = is_adult and has_ticket and not is_blocked
if can_enter:
    print("Вход разрешён")
else:
    print("Вход запрещён")