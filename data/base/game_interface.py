import pygame
from data.base.load_image import load_image

global hand
global past_button
global Text
global scroll_in
scroll_in = 0
Text = []
past_button = False
hand = 0


def show_game_int(screen: pygame.surface.Surface, player, wight, height, mouse_pos, mouse_left_button, new_text=None):
    global hand
    global past_button
    global Text
    global scroll_in

    image = load_image("textures/arts/interface/game_interface.png")

    scaled_image = pygame.transform.scale(image, (wight, height // 5))
    delta_w = wight / 1920
    delta_h = height / 1080
    screen.blit(scaled_image, (0, height - height // 5))


    if new_text:
        stroka = "    • "
        for i in new_text.split("\n"):
            stroka += i
            Text.append(stroka)
            stroka = ""



    if len(Text) > 30:
        Text.pop(0)

    to_render = []

    font = pygame.font.SysFont('Times New Roman Ms', int(25 * (delta_w + delta_h) // 2))

    text_surface = font.render(f"{player.current_hp} / {player.max_hp}", False, (112, 57, 0) if \
        player.current_hp / player.max_hp > 0.25 else (255, 57, 0))

    screen.blit(text_surface, (152 * delta_w, height - height // 5 + 34 * delta_h))

    text_surface = font.render(f"{player.current_ap} / {player.max_ap}", False, (112, 57, 0))

    screen.blit(text_surface, (152 * delta_w, height - height // 5 + 82 * delta_h))
    if new_text:
        scroll_in += 1

    if len(Text) - 9 < scroll_in:
        scroll_in = len(Text) - 9 if len(Text) - 9 > 0 else 0

    if 0 > scroll_in:
        scroll_in = 0

    for i in range(len(Text)):
        if scroll_in <= i <= scroll_in + 8:
            to_render.append(Text[i])
        elif to_render:
            break
    k = 0
    for i in to_render:
        text_surface = font.render(f"{i}", False, (112, 200, 0))
        screen.blit(text_surface, (675 * delta_w, height - height // 5 + 18 * delta_h + 20 * k * delta_h))
        k += 1

    if hand % 2 == 0:
        if player.right_hand:
            screen.blit(player.right_hand.texture_inv, (392 * delta_w, height - height // 5 + 42 * delta_h))
        player.selected_hand = player.right_hand
    else:
        if player.left_hand:
            screen.blit(player.left_hand.texture_inv, (392 * delta_w, height - height // 5 + 42 * delta_h))
        player.selected_hand = player.left_hand

    if 319 * delta_w <= mouse_pos[0] <= 548 * delta_w and height - height // 5 + 151 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 203 * delta_h and past_button != mouse_left_button and mouse_left_button:
        hand += 1
        if hand == 2:
            hand = 0

    if 1679 * delta_w <= mouse_pos[0] <= 1774 * delta_w and height - height // 5 + 13 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 49 * delta_h and past_button != mouse_left_button and mouse_left_button:
        return 1

    if 1679 * delta_w <= mouse_pos[0] <= 1774 * delta_w and height - height // 5 + 60 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 93 * delta_h and past_button != mouse_left_button and mouse_left_button:
        return 2

    if 1679 * delta_w <= mouse_pos[0] <= 1774 * delta_w and height - height // 5 + 107 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 143 * delta_h and past_button != mouse_left_button and mouse_left_button:
        return 3

    if 1679 * delta_w <= mouse_pos[0] <= 1774 * delta_w and height - height // 5 + 158 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 194 * delta_h and past_button != mouse_left_button and mouse_left_button:
        return 4

    if 1435 * delta_w <= mouse_pos[0] <= 1664 * delta_w and height - height // 5 + 149 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 201 * delta_h and past_button != mouse_left_button and mouse_left_button:
        return 5

    if 145 * delta_w <= mouse_pos[0] <= 240 * delta_w and height - height // 5 + 121 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 155 * delta_h and past_button != mouse_left_button and mouse_left_button:
        past_button = mouse_left_button
        return 6

    if 145 * delta_w <= mouse_pos[0] <= 240 * delta_w and height - height // 5 + 156 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 201 * delta_h and past_button != mouse_left_button and mouse_left_button:
        return 7

    if 640 * delta_w <= mouse_pos[0] <= 665 * delta_w and height - height // 5 + 146 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 171 * delta_h and past_button != mouse_left_button and mouse_left_button:
        scroll_in -= 1

    if 640 * delta_w <= mouse_pos[0] <= 665 * delta_w and height - height // 5 + 176 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 201 * delta_h and past_button != mouse_left_button and mouse_left_button:
        scroll_in += 1

    if 320 * delta_w <= mouse_pos[0] <= 546 * delta_w and height - height // 5 + 22 * delta_h <= mouse_pos[1] <= \
            height - height // 5 + 140 * delta_h and past_button != mouse_left_button and mouse_left_button:
        if player.selected_hand:
            if player.selected_hand.type == "medicine":
                player.heal(player.selected_hand.add_to_hp)
                if player.selected_hand == player.left_hand:
                    player.left_hand = None
                if player.selected_hand == player.right_hand:
                    player.right_hand = None
                print(player.selected_hand)
    past_button = mouse_left_button
