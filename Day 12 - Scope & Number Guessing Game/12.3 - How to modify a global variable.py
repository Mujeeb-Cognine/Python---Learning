# Modifying Global Scope

enemies = 1


# def increase_enemies():
#     global enemies  # Without this line we cannot use next line enemies
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"Enemies outside function: {enemies}")


def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")
