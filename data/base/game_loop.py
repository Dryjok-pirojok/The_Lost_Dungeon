import sys

import pygame
from data.base.load_image import load_image
from data.izometry_eng.grid_ground import Grid
import threading
import multiprocessing
from data.base.floor_title_group import Floor, ChangeLevel
from data.entities.player.player import Player
from levels.TEST_LEVELS.test_level_01 import Test_level_01
from data.base.wall_title_group import Wall_up, Wall_top
from data.entities.enemies.test_npc_enemy import Test_Npc_Enemy
from data.base.config import button_keys, FPS, levels, curr_level, SIZE
from data.base.inventory import show_inventory
from data.items.misc.test_item import Test_item
from data.base.menu import show_menu
from data.base.game_interface import show_game_int
from data.base.characteristics_interface import show_characteristics
from data.izometry_eng.A_star import a_star, create_graph
from data.items.misc.bottle_c4m import C4m_bottle
from data.items.weapons.melee.Lash import Lash

global player
global a11


def change_level_func(to_level):
    global curr_level
    curr_level = to_level


# def draw_ground_grid(grid: Grid, cam_pos_x: int, cam_pos_y: int):
#     cols_x = grid.cols_xre
#     cols_y = grid.cols_y
#     width = grid.width
#     height = grid.height
#
#     for t in range(cols_x * cols_y):
#         tx = t % cols_x
#         ty = t // cols_x
#         x = 2 * 16 * ty - 3 * 16 * tx
#         y = 2 * 12 * ty + 12 * tx
#         x_to_draw = x + width + cam_pos_x
#         y_to_draw = y + cam_pos_y
#         if -height * 0.2 < y_to_draw <= height * 1.2 and -width * 0.2 < x_to_draw <= width * 1.2:
#             grid.draw_test_rect_ground(x + width + cam_pos_x, y + cam_pos_y)


def selected_title(screen, weight: int, cam_pos_x: int, cam_pos_y: int, tx: int, ty: int):
    x = 2 * 16 * ty - 3 * 16 * tx
    y = 2 * 12 * ty + 12 * tx
    x = x + weight + cam_pos_x
    y = y + cam_pos_y
    __cell_size_x__: int = 80
    __cell_size_y__: int = 36
    z = __cell_size_y__ // 2
    a = __cell_size_x__ // 2
    pygame.draw.line( screen, pygame.Color("0xFF0000"), (x - a +  __cell_size_x__ // 5 * 3,
                                                             y - z), (x - a, y - z +  __cell_size_y__ // 3), 1)
    pygame.draw.line( screen, pygame.Color("0xFF0000"),
                     (x - a, y - z +  __cell_size_y__ // 3), (x - a +  __cell_size_x__ // 5 * 2,
                                                                  y + z), 1)
    pygame.draw.line( screen, pygame.Color("0xFF0000"), (x - a +  __cell_size_x__ // 5 * 2, y + z),
                     (x + a, y - z +  __cell_size_y__ // 3 * 2), 1)
    pygame.draw.line( screen, pygame.Color("0xFF0000"), (x + a, y - z +  __cell_size_y__ // 3 * 2),
                     (x - a +  __cell_size_x__ // 5 * 3, y - z), 1)


# def draw_walls_grid(grid: Grid, cam_pos_x: int, cam_pos_y: int, side: int = 0):
#     cols_x = grid.cols_x
#     cols_y = grid.cols_y
#     width = grid.width
#     height = grid.height
#     for t in range(cols_x * cols_y):
#         tx = t % cols_x
#         ty = t // cols_x
#         x = 2 * 16 * ty - 3 * 16 * tx
#         y = 2 * 12 * ty + 12 * tx
#         x_to_draw = x + width + cam_pos_x
#         y_to_draw = y + cam_pos_y
#         if ty == 0:
#             if -height * 0.2 < y_to_draw <= height * 1.2 and -width * 0.2 < x_to_draw <= width * 1.2:
#                 grid.draw_test_wall(x_to_draw, y_to_draw, 1)
#         if tx == 0:
#             if -height * 0.2 < y_to_draw <= height * 1.2 and -width * 0.2 < x_to_draw <= width * 1.2:
#                 grid.draw_test_wall(x_to_draw, y_to_draw, 2)


def Loop(queue: multiprocessing.Queue, screen, clock):
    global player
    global a11
    move_to_numer = None
    size = weight, height = SIZE
    screen = screen
    clock = clock
    running = True
    level = curr_level
    cols_x = level.col_x
    cols_y = level.col_y
    cam_pos_x = 0
    cam_pos_y = 0
    zo = level.walls
    grid = Grid(size[0], size[1], cols_x, cols_y, zo)
    grid_level = create_graph(level.grid)

    fps = FPS
    k = 0
    base_x = 0
    base_y = 0
    ev_x = 0
    ev_y = 0
    right_button = False
    left_button = False
    tx = 0
    ty = 0
    dt = 0
    floor_sprites = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    change_room_sprites = pygame.sprite.Group()
    misc_sprites = pygame.sprite.Group()
    entities = []
    inv_showed = False
    cons_showed = False
    menu_showed = False
    char_showed = False
    k = 0
    is_fight = False
    player.tp_to(0, 0)
    aim = load_image("textures/arts/interface/aim.png")
    curr_turn = player
    left_button_past = False
    right_button_past = False
    past_inv = False
    fight_entities = []
    fight_counter = -1
    propusk_turn = False
    want_attack = False

    for t in range(cols_x * cols_y):
        tx = t % cols_x
        ty = t // cols_x
        Floor(floor_sprites, tx, ty, level.cells[t], weight, height)
    if level.to_nest_level:
        for i in level.to_nest_level:
            ChangeLevel(change_room_sprites, i[0], i[1], 5, weight, height, i[2])

    # Wall_up(wall_sprites, 0, 1, (3, 4), weight, height)
    # Wall_top(wall_sprites, 0, 1, (7, 8), weight, height)
    if level.walls:
        for i in level.walls:
            if i[2] == 1:
                Wall_up(wall_sprites, i[0], i[1], i[3], weight, height)
    test_npc = Test_Npc_Enemy(weight, height, 3, 3, load_image("textures/entities/test_npc_en.png"),
                              load_image("textures/entities/test_npc_en_dead.png"))
    entities.append(player)
    entities.append(test_npc)
    new_Text = ""

    to_draw = {}
    for i in range(0, level.col_y):
        to_draw[i] = []
    for i in wall_sprites:
        z = i.return_tx_and_ty()[1]
        to_draw[z].append(i)

    test_item = Lash()
    test_item2 = C4m_bottle()
    test_item3 = Test_item()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                queue.put({"status_end": "game_ended"})
                return False

            if event.type == pygame.MOUSEMOTION:
                ev_x = event.pos[0]
                ev_y = event.pos[1]
                if not (menu_showed or cons_showed or inv_showed or char_showed):
                    if right_button:
                        cam_pos_x = cam_pos_x + (base_x - ev_x)
                        cam_pos_y = cam_pos_y + (base_y - ev_y)
                        base_x = event.pos[0]
                        base_y = event.pos[1]
                    else:
                        x, y = event.pos[0], event.pos[1]
                        x = x - cam_pos_x - weight
                        y = y - cam_pos_y
                        x -= 8
                        y += 20
                        tx = - int((x - 4 * y / 3) / 64)
                        ty = int((x + 4 * y) / 128)
                        if tx < 0:
                            tx = 0
                        if ty < 0:
                            ty = 0
                        if tx > level.col_x - 1:
                            tx = level.col_x - 1
                        if ty > level.col_y - 1:
                            ty = level.col_y - 1
                        if is_fight:
                            z = a_star(grid_level, player.return_tx_and_ty(), (tx, ty))
                            if z:
                                distance = len(z) - 1
                            else:
                                distance = "x"
                            font = pygame.font.SysFont('Times New Roman Ms', 25)
                            move_to_numer = font.render(f"{distance}", False, (255, 255, 255))

                            screen.blit(move_to_numer, (x, y))
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == pygame.BUTTON_RIGHT:
                    right_button = True
                    if not (menu_showed or cons_showed or inv_showed or char_showed):
                        base_x = event.pos[0]
                        base_y = event.pos[1]
                        ev_x = event.pos[0]
                        ev_y = event.pos[1]
                if event.button == pygame.BUTTON_LEFT:
                    left_button = True
                    if ev_y <= (height - height // 5):
                        if not (menu_showed or cons_showed or inv_showed or char_showed or is_fight):
                            z = a_star(grid_level, player.return_tx_and_ty(), (tx, ty))
                            if z:
                                player.go_to(z[0:])

                            # player.move(tx, ty)
                        if is_fight and not inv_showed:
                            z = a_star(grid_level, player.return_tx_and_ty(), (tx, ty))
                            if z:
                                distance = len(z) - 1
                            else:
                                distance = -1
                            if distance <= player.current_ap and not want_attack and distance != -1:
                                z = a_star(grid_level, player.return_tx_and_ty(), (tx, ty))
                                player.go_to(z[0:])
                                player.current_ap -= distance
                            want_attack = False

            if event.type == pygame.KEYDOWN:
                if event.key == button_keys["inventory"]:
                    inv_showed = not inv_showed

                if event.key == button_keys["console"]:
                    cons_showed = not cons_showed

                if event.key == button_keys["menu"]:
                    menu_showed = not menu_showed

                if event.key == button_keys["char"]:
                    char_showed = not char_showed

                if event.key == pygame.K_o:
                    player.add_to_inventory(test_item)
                    player.add_to_inventory(test_item2)
                    player.add_to_inventory(test_item3)


                if event.key == pygame.K_h:
                    new_Text = "а я клавиша h " + str(k)
                    k += 1


            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_RIGHT:
                    right_button = False
                if event.button == pygame.BUTTON_LEFT:
                    left_button = False
        screen.fill("black")
        # thread_ground = threading.Thread(target=draw_ground_grid, args=(grid, cam_pos_x, cam_pos_y))
        # thread_wall = threading.Thread(target=draw_walls_grid, args=(grid, cam_pos_x, cam_pos_y))
        # thread_ground.start()
        # thread_ground.join()
        # thread_wall.start()
        #
        # thread_wall.join()
        change_room_sprites.draw(screen)
        if not menu_showed:
            for i in entities:
                if grid.test_can_see(i.return_tx_and_ty(), player.return_tx_and_ty()):
                    a1 = i.update(dt, True, player.return_tx_and_ty(), player)
                else:
                    a1 = i.update(dt, False, None, player)
                if a1:
                    if a1[0] == "start" and not is_fight:
                        print("fight start")
                        curr_turn = a1[1]
                        is_fight = True

            floor_sprites.update(cam_pos_x, cam_pos_y)
            wall_sprites.update(cam_pos_x, cam_pos_y, [player.return_tx_and_ty()])
            change_room_sprites.update(cam_pos_x, cam_pos_y, player, change_level_func)
        floor_sprites.draw(screen)
        selected_title(screen, weight, cam_pos_x, cam_pos_y, tx, ty)
        change_room_sprites.draw(screen)


        for i in entities:
            to_draw[i.return_tx_and_ty()[1]].append(i)
            to_draw[i.return_tx_and_ty()[1]].sort(key=lambda po: - po.return_tx_and_ty()[0] if str(po) ==
                                                                                               "NPC" else -9999999)
        to_remove = []
        for key, items in to_draw.items():
            for i in items:
                if str(i) == "NPC" or str(i) == "player":
                    i.draw(screen, cam_pos_x, cam_pos_y)
                    to_remove.append((key, i))

                else:
                    i.draw(screen)

        for key, i in to_remove:
            to_draw[key].remove(i)

        game_interface = show_game_int(screen, player, weight, height, (ev_x, ev_y), left_button, new_Text)

        new_Text = ""

        if game_interface == 1:
            inv_showed = True

        if game_interface == 2:
            menu_showed = True

        if game_interface == 3:
            char_showed = True
        if game_interface == 6 and is_fight and str(curr_turn) == "player":
            propusk_turn = True


        if move_to_numer and is_fight and not want_attack:
            screen.blit(move_to_numer, (ev_x + 10, ev_y + 10))

        if char_showed:
            a = show_characteristics(screen, player, weight, height, (ev_x, ev_y), left_button)

            if a == -1:
                char_showed = False

        if inv_showed and (not is_fight or curr_turn == player) and player.current_ap >= 3:
            a = show_inventory(screen, player, weight, height, (ev_x, ev_y), left_button)
            if is_fight and not past_inv:
                player.current_ap -= 3
            if not a:
                inv_showed = False

        if menu_showed:
            a = show_menu(screen, weight, height, (ev_x, ev_y), left_button)
            if a == 1:
                queue.put({"status_end": "game_ended"})
                return False
            if a == 2:
                menu_showed = False
        if is_fight:

            fight_entities.append(player)

            for i in entities:
                if grid.test_can_see(player.return_tx_and_ty(), i.return_tx_and_ty()):
                    if i.angry:
                        if not i.is_dead:
                            fight_entities.append(i)

            z = [s for s in entities if pygame.rect.Rect(s.rect.x + cam_pos_x - s.rect.width // 2, cam_pos_y +
                                                         s.rect.y - s.rect.height,
                                                         s.rect.width, s.rect.height).collidepoint(ev_x, ev_y)]



            fight_entities.sort(key=lambda po1: (po1.agility, po1.level, po1.luck))
            if len(fight_entities) == 1:
                is_fight = False
            if str(curr_turn) == 'player' and is_fight:
                if z:
                    if z[0] != player:
                        if not z[0].is_dead:
                            screen.blit(aim, (ev_x - 12, ev_y - 12))
                            if player.selected_hand:
                                if player.selected_hand.type == "attackable":
                                    class_1, class_2 = player.selected_hand.class_firearm
                                    a11 = 0
                                    exec(f"a11 = a11 + player.{class_1} // 2", globals())
                                    exec(f"a11 = a11 + player.{class_2}", globals())
                                    chance_to_attack = a11 + player.luck
                                    font = pygame.font.SysFont('Times New Roman Ms', 25)
                                    if chance_to_attack >= 95:
                                        chance_to_attack = 95
                                    move_to_numer = font.render(f"{chance_to_attack}%", False, (255, 0, 0))
                                    screen.blit(move_to_numer, (ev_x + 10, ev_y + 10))
                            else:
                                chance_to_attack = player.melee // 2 + player.fists + player.luck
                                font = pygame.font.SysFont('Times New Roman Ms', 25)
                                if chance_to_attack >= 95:
                                    chance_to_attack = 95
                                move_to_numer = font.render(f"{chance_to_attack}%", False, (255, 0, 0))
                                screen.blit(move_to_numer, (ev_x + 10, ev_y + 10))
                            want_attack = True
                            if left_button and left_button_past != left_button:
                                if player.selected_hand:
                                    if player.selected_hand.type == "attackable":
                                        can_att = grid.test_can_attack(player.return_tx_and_ty(),
                                                             z[0].return_tx_and_ty(), player.selected_hand.range)
                                    else:
                                        can_att = False
                                else:
                                    can_att = grid.test_can_attack(player.return_tx_and_ty(),
                                                                   z[0].return_tx_and_ty(), 1)
                                if can_att:
                                    new_Text, is_killed, *args = player.attack(z[0], chance_to_attack)

                                    if is_killed:
                                        new_Text += "\n Вы убили"
                                else:
                                    new_Text += "не достаточно дистанции"
                if (player.current_ap <= 0 or propusk_turn) and player.move_is_done:
                    fight_counter += 1
                    if fight_counter >= len(fight_entities):
                        fight_counter = 0
                    curr_turn = fight_entities[fight_counter]
                    player.current_ap = player.max_ap
                    propusk_turn = False
                    print(111)
            else:

                new_Text = curr_turn.fight(grid, player, grid_level)

                if curr_turn.current_ap == 0 and curr_turn.move_is_done:
                    curr_turn.current_ap = curr_turn.max_ap
                    fight_counter += 1
                    if fight_counter >= len(fight_entities):
                        fight_counter = 0
                    curr_turn = fight_entities[fight_counter]
                    print(curr_turn)

                    print("ход компа закончен")
            fight_entities = []


        pygame.display.flip()
        clock.tick(fps)
        dt = clock.tick(fps) / 1000
        if level != curr_level:
            player.tp_to(0, 0)
            entities = []
            return True
        left_button_past = left_button
        right_button_past = right_button
        past_inv = inv_showed
        if not is_fight:
            player.current_ap = player.max_ap
            fight_counter = -1
        if player.is_dead:
            print("Вы мертвы")
            sys.exit()

def Game_main(queue):
    icon = load_image("textures/arts/icon.bmp", colorkey=(255, 255, 255))
    pygame.display.set_icon(icon)
    pygame.display.set_caption("The Lost Dungeon")
    pygame.init()
    screen = pygame.display.set_mode(SIZE, pygame.SRCALPHA)
    clock = pygame.time.Clock()
    weight, height = SIZE
    global player
    player = Player(weight, height, 0, 1)
    pygame.font.init()
    while True:
        a = Loop(queue, screen, clock)
        if not a:
            break

