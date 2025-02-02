import pygame
from data.base.load_image import load_image


global nazv
nazv = "Название"
opis = "Описание"

global scroll
scroll = 0

global past_button
past_button = False

global choosed_item


def show_inventory(screen: pygame.surface.Surface, player, wight, height, mouse_pos, mouse_left_button):
    global nazv
    global opis
    global scroll
    global past_button
    global choosed_item
    font = pygame.font.SysFont('Times New Roman Ms', 34)

    screen.blit(load_image("textures/arts/interface/inventory.png"), (wight // 2 - 400, height // 2 - 300))
    screen.blit(load_image("textures/arts/interface/inventory_close_button.png"), (wight // 2 + 307, height // 2 + 236))
    delta_h = height // 1080
    text_surface = font.render(f"{nazv}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 220, height // 2 - 300 + 110))
    to_render_opis = opis.split("\n")
    font = pygame.font.SysFont('Times New Roman Ms', 25)
    k = 0
    for i in to_render_opis:
        text_surface = font.render(f"{i}", False, (112, 57, 0))
        screen.blit(text_surface, (wight // 2 - 400 + 220, height // 2 - 300 + 170 + 22.5 * k))
        k += 1
    k = 0
    data = []
    font = pygame.font.SysFont('Times New Roman Ms', 25)
    for i, count in player.return_inv().items():
        data.append(i)
        if scroll <= k <= 4 + scroll:
            screen.blit(i.texture_inv, (wight // 2 - 400 + 50, height // 2 - 300 + 100 + (k - scroll) * 80))
            text_surface = font.render(f"x {count}", False, (112, 57, 0))
            screen.blit(text_surface, (wight // 2 - 400 + 100, height // 2 - 300 + 100 + (k - scroll) * 80 + 60))

        k += 1

    if wight // 2 + 307 <= mouse_pos[0] <= wight // 2 + 356 and height // 2 + 236 <= mouse_pos[1] <= height // 2 + 281 \
            and mouse_left_button:

        return False

    if wight // 2 - 400 + 43 <= mouse_pos[0] <= wight // 2 - 400 + 151 and height // 2 - 200 <= mouse_pos[1] <= \
            height // 2 - 300 + 497:
        work_pos = mouse_pos[1] - height // 2 + 200
        sel_item = work_pos // 80
        sel_item += scroll

        if sel_item <= k - 1:
            if k != 0:
                pygame.draw.rect(screen, (193, 187, 0),
                                 (wight // 2 - 400 + 50, height // 2 - 200 + sel_item * 80, 80, 80), 1)
                if mouse_left_button:
                    nazv = data[sel_item].name
                    opis = data[sel_item].description

                choosed_item = sel_item

    if wight // 2 - 400 + 158 <= mouse_pos[0] <= wight // 2 - 400 + 188 and height // 2 - 300 + 95 <= mouse_pos[1] <= \
            height // 2 - 300 + 124 and past_button != mouse_left_button and mouse_left_button:
        scroll -= 1
        if scroll < 0:
            scroll = 0

    if wight // 2 - 400 + 158 <= mouse_pos[0] <= wight // 2 - 400 + 188 and height // 2 - 300 + 126 <= mouse_pos[1] <= \
            height // 2 - 300 + 155 and past_button != mouse_left_button and mouse_left_button:
        scroll += 1
        if scroll > len(data) - 1:
            scroll = len(data) - 1

    if wight // 2 - 400 + 40 <= mouse_pos[0] <= wight // 2 - 400 + 239 and height // 2 - 300 + 528 <= mouse_pos[1] <= \
            height // 2 - 300 + 577 and past_button != mouse_left_button and mouse_left_button:
        try:
            player.remove_from_inventory(data[choosed_item])

        except Exception as err:
            print(err)

    if wight // 2 - 400 + 259 <= mouse_pos[0] <= wight // 2 - 400 + 458 and height // 2 - 300 + 528 <= mouse_pos[1] <= \
            height // 2 - 300 + 577 and past_button != mouse_left_button and mouse_left_button:
        try:
            if data[choosed_item].name == "Тестовый предмет":
                print("1")
            if data[choosed_item].type == "medicine":
                player.heal(data[choosed_item].add_to_hp)
                player.remove_from_inventory(data[choosed_item])

        except Exception as err:
            print(err)

    if player.left_hand:
        screen.blit(player.left_hand.texture_inv, (wight // 2 - 400 + 233, height // 2 - 300 + 348))

    if player.right_hand:
        screen.blit(player.right_hand.texture_inv, (wight // 2 - 400 + 400, height // 2 - 300 + 348))

    if wight // 2 - 400 + 259 <= mouse_pos[0] <= wight // 2 - 400 + 383 and height // 2 - 300 + 450 <= mouse_pos[1] <= \
            height // 2 - 300 + 466 and past_button != mouse_left_button and mouse_left_button:
        if not player.left_hand:
            try:
                player.remove_from_inventory(data[choosed_item])
                player.left_hand = data[choosed_item]

            except Exception as err:
                print(err)
        else:
            try:
                player.add_to_inventory(player.left_hand)
                player.left_hand = None

            except Exception as err:
                print(err)

    if wight // 2 - 400 + 386 <= mouse_pos[0] <= wight // 2 - 400 + 539 and height // 2 - 300 + 450 <= mouse_pos[1] <= \
            height // 2 - 300 + 466 and past_button != mouse_left_button and mouse_left_button:
        if not player.right_hand:
            try:
                player.remove_from_inventory(data[choosed_item])
                player.right_hand = data[choosed_item]

            except Exception as err:
                print(err)
        else:
            try:
                player.add_to_inventory(player.right_hand)
                player.right_hand = None
            except Exception as err:
                print(err)

    past_button = mouse_left_button

    return True
