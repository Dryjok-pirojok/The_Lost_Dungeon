import pygame
from data.base.load_image import load_image

global past_button
past_button = False


def show_characteristics(screen: pygame.surface.Surface, player, wight, height, mouse_pos, mouse_left_button):
    global past_button
    screen.blit(load_image("textures/arts/interface/character.png"), (wight // 2 - 400, height // 2 - 300))

    font = pygame.font.SysFont('Times New Roman Ms', 60)

    text_surface = font.render(f"{player.strength}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 164, height // 2 - 300 + 85))

    text_surface = font.render(f"{player.luck}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 164, height // 2 - 300 + 145))

    text_surface = font.render(f"{player.agility}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 164, height // 2 - 300 + 206))

    text_surface = font.render(f"{player.voice}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 164, height // 2 - 300 + 265))

    text_surface = font.render(f"{player.endurance}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 164, height // 2 - 300 + 327))

    text_surface = font.render(f"{player.level}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 209, height // 2 - 300 + 414))

    font = pygame.font.SysFont('Times New Roman Ms', 40)

    text_surface = font.render(f"{player.curr_xp}/{player.need_xp}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 131, height // 2 - 300 + 456))

    text_surface = font.render(f"{player.free_points_char}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 336, height // 2 - 300 + 496))

    text_surface = font.render(f"{player.free_points_abil}", False, (112, 57, 0))
    screen.blit(text_surface, (wight // 2 - 400 + 324, height // 2 - 300 + 533))



    data = [player.melee, player.crushing, player.fists, player.lash, player.firearms, player.one_handed,
            player.two_handed, player.heavy_gun, player.grenades, player.speech, player.steal, player.repair,
            player.science]
    k = 0
    for i in data:
        text_surface = font.render(f"{i}", False, (112, 57, 0))
        screen.blit(text_surface, (wight // 2 - 400 + 685, height // 2 - 300 + 76 + 39.1 * k))
        k += 1

    if (wight // 2 - 400 + 764 <= mouse_pos[0] <= wight // 2 - 400 + 795 and height // 2 - 300 + 4 <= mouse_pos[1] <=
            height // 2 - 300 + 51 and mouse_left_button):
        return -1
    if player.free_points_char:
        if (wight // 2 - 400 + 323 <= mouse_pos[0] <= wight // 2 - 400 + 392 and height // 2 - 300 + 71 <= mouse_pos[1]
                <= height // 2 - 300 + 135 and past_button != mouse_left_button and mouse_left_button):
            player.strength += 1
            player.calculate_abilities()
            player.free_points_char -= 1
        elif (wight // 2 - 400 + 323 <= mouse_pos[0] <= wight // 2 - 400 + 392 and height // 2 - 300 + 135 <= mouse_pos[1]
                <= height // 2 - 300 + 194 and past_button != mouse_left_button and mouse_left_button):
            player.luck += 1
            player.calculate_abilities()
            player.free_points_char -= 1
        elif (wight // 2 - 400 + 323 <= mouse_pos[0] <= wight // 2 - 400 + 392 and height // 2 - 300 + 194 <= mouse_pos[1]
                <= height // 2 - 300 + 255 and past_button != mouse_left_button and mouse_left_button):
            player.agility += 1
            player.calculate_abilities()
            player.free_points_char -= 1
        elif (wight // 2 - 400 + 323 <= mouse_pos[0] <= wight // 2 - 400 + 392 and height // 2 - 300 + 255 <= mouse_pos[1]
                <= height // 2 - 300 + 317 and past_button != mouse_left_button and mouse_left_button):
            player.voice += 1
            player.calculate_abilities()
            player.free_points_char -= 1
        elif (wight // 2 - 400 + 323 <= mouse_pos[0] <= wight // 2 - 400 + 392 and height // 2 - 300 + 317 <= mouse_pos[1]
                <= height // 2 - 300 + 375 and past_button != mouse_left_button and mouse_left_button):
            player.endurance += 1
            player.calculate_abilities()
            player.free_points_char -= 1
    data = ['player.add_to_melee', 'player.add_to_crushing', 'player.add_to_fists', 'player.add_to_lash',
            'player.add_to_firearms', 'player.add_to_one_handed', 'player.add_to_two_handed', 'player.add_to_heavy_gun',
            'player.add_to_grenades', 'player.add_to_speech', 'player.add_to_steal', 'player.add_to_repair',
            'player.add_to_science']
    if player.free_points_abil:
        if (wight // 2 - 400 + 747 <= mouse_pos[0] <= wight // 2 - 400 + 774 and
                past_button != mouse_left_button and mouse_left_button and height // 2 - 300 + 76 <= mouse_pos[1]
                <= height // 2 - 300 + 568):
            wor_dir_y = mouse_pos[1] - height // 2 + 300 - 75
            if wor_dir_y % 39 < 27:
                button = wor_dir_y // 38
                exec(f"{data[button]} += 1")
                player.calculate_abilities()
                player.free_points_abil -= 1



    past_button = mouse_left_button


