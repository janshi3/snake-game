import pygame
import sys
import random
import ast

pygame.init()
(monitor_width, monitor_height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

# Initialising variables
game_width = 800
game_height = 600
menu_width = 800
menu_height = 600
game_screen_set = False
menu_color = (0, 70, 0)
rect_color1 = menu_color
rect_color2 = menu_color
rect_color3 = menu_color
rect_color4 = menu_color
rect_color5 = menu_color
rect_color6 = menu_color
black_color = (0, 0, 0)
start_button_color = (100, 150, 0)
start_button_color1 = (100, 150, 0)
exit_button_color = (150, 0, 0)
exit_button_color1 = (150, 0, 0)
ok_button_color = (100, 149, 237)
hscores_button_color = (150, 150, 0)
hscores_button_color1 = (150, 150, 0)
button_outline_color = (0, 0, 0)
enter_name_color = (90, 90, 0)
food_tbox_color = (90, 90, 0)
speed_tbox_color = (90, 90, 0)
walls_tbox_color = (90, 90, 0)
resx_tbox_color = (90, 90, 0)
resy_tbox_color = (90, 90, 0)
gridx_tbox_color = (90, 90, 0)
gridy_tbox_color = (90, 90, 0)
cbox_on_color = (100, 0, 0)
cbox_off_color = (20, 20, 20)
snake_color = (255, 255, 0)
snake_color2 = (0, 255, 255)
wall_color = (160, 82, 45)
food_color = None
text_color = (255, 255, 0)
snake_size = [19, 19]
snake_direction = "right"
snake_direction2 = "left"
AI = False
snake_memory = []
checking = False
check_pos = [None, None]
stuck = False
check_count = 0
period = 0
rechecking = False
move = 0
hunger = 0
game_result = None
multiplayer = False
max_food = 3
food = 0
food_pos = []
wall_pos = []
speed = 5
walls = 0
no_walls = True
glued_wall_mode = False
game_over1 = False
game_over2 = False

clock = pygame.time.Clock()
score_font = pygame.font.SysFont("monospace", 35)
screen = pygame.display.set_mode([menu_width, menu_height])

menu = True
game_over = False
settings_menu = False
hscore_display = False
game_choice_menu = False
new_hscore = False
user_input = ""
not_fullscreen = False
save_game = False
load_game = False
load_map = False
new_map = False
choose_mode = False
error = False
checked_score = False


class Checkbox:
    def __init__(self, color, x, y, size):
        self.color = color
        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen):
        pygame.draw.ellipse(screen, (0, 0, 0), (self.x - 5, self.y - 5, self.size + 10, self.size + 10))
        pygame.draw.ellipse(screen, self.color, (self.x - 2, self.y - 2, self.size + 4, self.size + 4))

    def is_over(self, pos):
        # Check if mouse is hovering over
        if self.x < pos[0] < self.x + self.size:
            if self.y < pos[1] < self.y + self.size:
                return True


class TextBox:
    def __init__(self, color, x, y, width, height, text="", num_only=False):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = black_color
        self.num_only = num_only

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 5, self.y - 5, self.width + 10, self.height + 10))
        pygame.draw.rect(screen, self.color, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))

    def is_over(self, pos):
        # Check if mouse is hovering over
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

    # Display input in text box
    def display_input(self, text_length):
        user_input = ""
        tbox_focus = True
        while tbox_focus:

            # Display pressed number key
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        user_input += "0"
                    elif event.key == pygame.K_1:
                        user_input += "1"
                    elif event.key == pygame.K_2:
                        user_input += "2"
                    elif event.key == pygame.K_3:
                        user_input += "3"
                    elif event.key == pygame.K_4:
                        user_input += "4"
                    elif event.key == pygame.K_5:
                        user_input += "5"
                    elif event.key == pygame.K_6:
                        user_input += "6"
                    elif event.key == pygame.K_7:
                        user_input += "7"
                    elif event.key == pygame.K_8:
                        user_input += "8"
                    elif event.key == pygame.K_9:
                        user_input += "9"
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == pygame.K_ESCAPE:
                        tbox_focus = False
                    elif not self.num_only:

                        # If text box allows non numeric characters
                        if event.key == pygame.K_q:
                            user_input += "Q"
                        elif event.key == pygame.K_w:
                            user_input += "W"
                        elif event.key == pygame.K_e:
                            user_input += "E"
                        elif event.key == pygame.K_r:
                            user_input += "R"
                        elif event.key == pygame.K_t:
                            user_input += "T"
                        elif event.key == pygame.K_y:
                            user_input += "Y"
                        elif event.key == pygame.K_u:
                            user_input += "U"
                        elif event.key == pygame.K_i:
                            user_input += "I"
                        elif event.key == pygame.K_o:
                            user_input += "O"
                        elif event.key == pygame.K_p:
                            user_input += "P"
                        elif event.key == pygame.K_a:
                            user_input += "A"
                        elif event.key == pygame.K_s:
                            user_input += "S"
                        elif event.key == pygame.K_d:
                            user_input += "D"
                        elif event.key == pygame.K_f:
                            user_input += "F"
                        elif event.key == pygame.K_g:
                            user_input += "G"
                        elif event.key == pygame.K_h:
                            user_input += "H"
                        elif event.key == pygame.K_j:
                            user_input += "J"
                        elif event.key == pygame.K_k:
                            user_input += "K"
                        elif event.key == pygame.K_l:
                            user_input += "L"
                        elif event.key == pygame.K_z:
                            user_input += "Z"
                        elif event.key == pygame.K_x:
                            user_input += "X"
                        elif event.key == pygame.K_c:
                            user_input += "C"
                        elif event.key == pygame.K_v:
                            user_input += "V"
                        elif event.key == pygame.K_b:
                            user_input += "B"
                        elif event.key == pygame.K_n:
                            user_input += "N"
                        elif event.key == pygame.K_m:
                            user_input += "M"
                        elif event.key == pygame.K_SPACE:
                            user_input += " "

            # Display text
            tbox_font = pygame.font.SysFont("monospace", 50, bold=True)
            text = tbox_font.render(user_input, 1, black_color)
            screen.blit(text, (self.x, self.y))
            pygame.display.update()

            # Stop input if text exceeds max character limit
            if len(user_input) == text_length:
                tbox_focus = False
        return user_input


class Button:
    def __init__(self, color, x, y, width, height, text="", button_text_color=black_color):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = button_text_color

    def draw(self, screen, outline=None, shape="ellipse"):

        if shape == "ellipse":
            if outline:
                pygame.draw.ellipse(screen, outline, (self.x - 5, self.y - 5, self.width + 10, self.height + 10))
            pygame.draw.ellipse(screen, self.color, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))

        if shape == "rectangle":
            if outline:
                pygame.draw.rect(screen, outline, (self.x - 5, self.y - 5, self.width + 10, self.height + 10))
            pygame.draw.rect(screen, self.color, (self.x - 2, self.y - 2, self.width + 4, self.height + 4))

        # Display text inside button
        if self.text != "":
            menu_font = pygame.font.SysFont('comicsans', 60)
            text = menu_font.render(self.text, 1, self.text_color)
            screen.blit(text, (self.x + (self.width // 2 - (len(self.text * 10))),
                               self.y + (self.height // 2 - text.get_height() // 2)))

    def is_over(self, pos):
        # Check if mouse is hovering over
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True


def draw_walls(walls):
    if no_walls:
        for count in range(0, walls):
            colliding = True
            # Mode where walls are created in groups
            if glued_wall_mode:
                while colliding:
                    check_pos = True
                    # Generate random position
                    width = (random.randint(1, (game_width // 20))) * 20 - 20
                    height = (random.randint(1, (game_height // 20))) * 20 - 20

                    # Check if wall isn't near center
                    if game_width // 2 - 100 < width < game_width // 2 + 100 and game_height // \
                            2 - 80 < height < game_height // 2 + 80:
                        check_pos = False

                    # Check if wall doesn't already exist
                    for pos in wall_pos:
                        if pos == [width, height]:
                            check_pos = False

                    if not check_pos:
                        continue

                    # Add the main wall to the wall list
                    wall_pos.append([width, height])
                    base_wall = [width, height]
                    wall_amount = random.randint(1, 8)

                    # Add a wall in a random direction next to the previous wall
                    for count1 in range(0, wall_amount):
                        not_finished = True
                        iteration_count = 0
                        while not_finished:
                            iteration_count += 1

                            # Break if can't place wall next to the previous wall
                            if iteration_count > 30:
                                break

                            detect_col = False
                            width = base_wall[0]
                            height = base_wall[1]
                            check = random.randint(1, 4)

                            # Choose a random direction
                            if check == 1:
                                width += 20
                            elif check == 2:
                                width -= 20
                            elif check == 3:
                                height += 20
                            elif check == 4:
                                height -= 20

                            # Check if new wall ins't near center
                            if game_width // 2 - 100 < width < game_width // 2 + 100 and \
                                    game_height // 2 - 80 < height < game_height // 2 + 80:
                                detect_col = True

                            # Check if new wall isn't outside of map borders
                            if width < 0 or height < 0 or width > game_width or height > game_height:
                                detect_col = True

                            # Check if new wall isn't inside an already existing wall
                            for pos in wall_pos:
                                if pos == [width, height]:
                                    detect_col = True

                            if not detect_col:
                                # Add the new wall to the wall list
                                wall_pos.append([width, height])
                                base_wall = [width, height]
                                not_finished = False
                    colliding = False

            else:
                # If glued wall mode is off, walls spawn as random squares on the map
                while colliding:
                    detect_col = False

                    # Generate wall position
                    width = (random.randint(1, (game_width // 20))) * 20 - 20
                    height = (random.randint(1, (game_height // 20))) * 20 - 20

                    # Check if wall is near center, so that the player doesn't instantly run into it
                    if game_width // 2 - 100 < width < game_width // 2 + 100 and game_height // \
                            2 - 80 < height < game_height // 2 + 80:
                        detect_col = True

                    # Check if such wall already exists
                    for pos in wall_pos:
                        if pos == [width, height]:
                            detect_col = True

                    if detect_col:
                        pass
                    else:
                        # Add to the wall list
                        wall_pos.append([width, height])
                        colliding = False
    # Draw walls
    for wall in wall_pos:
        pygame.draw.rect(screen, wall_color, (wall[0], wall[1], 20, 20))


def draw_food(food, max_food, food_pos):
    # If no food exists
    food_count = food
    if food < max_food:
        for times in range(0, max_food-food):
            # Generate random color
            rand_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))

            colliding = True
            food_loop_count = 0
            while colliding:
                food_loop_count += 1
                detect_col = False

                # Generate random food position
                food_pos_temp = [(random.randint(1, (game_width // 20))) * 20 - 20,
                                 (random.randint(1, (game_height // 20))) * 20 - 20]

                # Check if food spawns inside snake's head
                if food_pos_temp == snake_pos:
                    continue
                if food_pos_temp == snake_pos2:
                    continue

                # Check if food spawns inside snake's tail or inside already existing food
                for pos in p1_tail_pos:
                    if food_pos_temp == pos:
                        detect_col = True

                for pos in p2_tail_pos:
                    if food_pos_temp == pos:
                        detect_col = True

                for pos in food_pos:
                    if food_pos_temp == pos[0]:
                        detect_col = True

                # Check if food spawns inside a wall
                wall_count = 0
                for pos in wall_pos:
                    if food_pos_temp == pos:
                        detect_col = True
                        # Check if food isn't stuck between walls

                    elif [food_pos_temp[0] + 20, food_pos_temp[1]] == pos or [food_pos_temp[0] - 20, food_pos_temp[1]] \
                            == pos or [food_pos_temp[0], food_pos_temp[1] + 20] == pos\
                            or [food_pos_temp[0], food_pos_temp[1] - 20] == pos:
                        wall_count += 1

                if not detect_col and wall_count < 3:
                    colliding = False

                # Break if can't find a spot to place food
                if food_loop_count > 99 and food_count != 0:
                    break

            # Add food to the food list
            food_pos.append([food_pos_temp, rand_color])
            food_count += 1

        # Draw food
    for pos in food_pos:
        pygame.draw.ellipse(screen, pos[1], (pos[0][0], pos[0][1], snake_size[0], snake_size[1]))
    return food_pos, food_count


def eat_food(player, score, color, pos, food, hunger):
    if player == "human":
        score += 1

        # Change color whenever food gets eaten
        (R, G, B) = color
        if score - 1 < 100 and R > 0:
            R -= 5
        if score - 1 >= 50 and G > 0:
            G -= 5
        if score - 1 >= 100 and R < 255:
            R += 5
        if score - 1 >= 150 and B < 255:
            B += 5
        color = (R, G, B)

        # Add tail
        p1_tail_pos.insert(0, p1_tail_pos[0])
        food_pos.pop(food_pos.index(pos))
        food -= 1

    if player == "AI":
        score += 1
        # Reset hunger
        hunger = 0

        # Change color whenever food gets eaten
        (R, G, B) = color
        if score - 1 < 100 and B > 0:
            B -= 5
        if score - 1 >= 50 and G > 0:
            G -= 5
        if score - 1 >= 100 and B < 255:
            B += 5
        if score - 1 >= 150 and R < 255:
            R += 5
        color = (R, G, B)

        # Add tail
        p2_tail_pos.insert(0, p2_tail_pos[0])
        food_pos.pop(food_pos.index(pos))
        food -= 1

    if player == "human2":
        score += 1

        # Change color whenever food gets eaten
        (R, G, B) = color
        if score - 1 < 100 and B > 0:
            B -= 5
        if score - 1 >= 50 and G > 0:
            G -= 5
        if score - 1 >= 100 and B < 255:
            B += 5
        if score - 1 >= 150 and R < 255:
            R += 5
        color = (R, G, B)

        # Add tail
        p2_tail_pos.insert(0, p2_tail_pos[0])
        food_pos.pop(food_pos.index(pos))
        food -= 1
    return score, food, color, hunger


def draw_snake(player):
    if player == "human":
        pygame.draw.rect(screen, snake_color, (snake_pos[0], snake_pos[1], snake_size[0], snake_size[1]))

    if player == "human2" or player == "AI":
        pygame.draw.rect(screen, snake_color2, (snake_pos2[0], snake_pos2[1], snake_size[0], snake_size[1]))


def draw_snake_tail(player):
    if player == "human":
        for pos in p1_tail_pos:
            pygame.draw.rect(screen, snake_color, (pos[0], pos[1], snake_size[0], snake_size[1]))

    if player == "human2" or player == "AI":
        for pos in p2_tail_pos:
            pygame.draw.rect(screen, snake_color2, (pos[0], pos[1], snake_size[0], snake_size[1]))


def snake_move(pressed_key, player):

    if player == "human":

        # Remove the last square and add a new square to the front
        p1_tail_pos.pop(0)
        p1_tail_pos.insert(score, [snake_pos[0], snake_pos[1]])

        # Move in the chosen direction
        if pressed_key == pygame.K_UP:
            snake_pos[1] -= 20
            snake_direction = "up"

        elif pressed_key == pygame.K_DOWN:
            snake_pos[1] += 20
            snake_direction = "down"

        elif pressed_key == pygame.K_RIGHT:
            snake_pos[0] += 20
            snake_direction = "right"

        elif pressed_key == pygame.K_LEFT:
            snake_pos[0] -= 20
            snake_direction = "left"

        elif pressed_key == "quit":
            return True, False, None

        # Move snake to the other side of the map if snake crosses map border
        if snake_pos[0] > game_width - 20:
            snake_pos[0] = 0

        elif snake_pos[0] < 0:
            snake_pos[0] = game_width - 20

        elif snake_pos[1] > game_height - 20:
            snake_pos[1] = 0

        elif snake_pos[1] < 0:
            snake_pos[1] = game_height - 20

        # Check if head collides with wall or tail
        if snake_pos == snake_pos2:
            return True, True, None

        for pos in wall_pos:
            if snake_pos == pos:
                return True, False, None

        for pos in p1_tail_pos:
            if snake_pos == pos:
                return True, False, None

        for pos in p2_tail_pos:
            if snake_pos == pos:
                return True, False, None

    elif player == "human2":

        # Remove the last square and add a new square to the front
        p2_tail_pos.pop(0)
        p2_tail_pos.insert(score2, [snake_pos2[0], snake_pos2[1]])

        # Move in the chosen direction
        if pressed_key == pygame.K_w:
            snake_pos2[1] -= 20
            snake_direction = "up"

        elif pressed_key == pygame.K_s:
            snake_pos2[1] += 20
            snake_direction = "down"

        elif pressed_key == pygame.K_d:
            snake_pos2[0] += 20
            snake_direction = "right"

        elif pressed_key == pygame.K_a:
            snake_pos2[0] -= 20
            snake_direction = "left"

    elif player == "AI":

        # Remove the last square and add a new square to the front
        p2_tail_pos.pop(0)
        p2_tail_pos.insert(score2, [snake_pos2[0], snake_pos2[1]])

        # Move in the chosen direction
        if pressed_key == "up":
            snake_pos2[1] -= 20
            snake_direction = "up"

        elif pressed_key == "down":
            snake_pos2[1] += 20
            snake_direction = "down"

        elif pressed_key == "right":
            snake_pos2[0] += 20
            snake_direction = "right"

        elif pressed_key == "left":
            snake_pos2[0] -= 20
            snake_direction = "left"

    if player == "human2" or player == "AI":
        # Move snake to the other side of the map if snake crosses map border
        if snake_pos2[0] > game_width - 20:
            snake_pos2[0] = 0

        elif snake_pos2[0] < 0:
            snake_pos2[0] = game_width - 20

        elif snake_pos2[1] > game_height - 20:
            snake_pos2[1] = 0

        elif snake_pos2[1] < 0:
            snake_pos2[1] = game_height - 20

        # Check if head collides with wall or tail
        if snake_pos == snake_pos2:
            return True, True, None

        for pos in wall_pos:
            if snake_pos2 == pos:
                return True, False, None

        for pos in p1_tail_pos:
            if snake_pos2 == pos:
                return True, False, None

        for pos in p2_tail_pos:
            if snake_pos2 == pos:
                return True, False, None

    return False, False, snake_direction


def snake_look(direction, player_dead):
    # Returns the distance to the closest obstacle in a certain direction

    if direction == "up":
        distance = game_height
        if not player_dead:
            # If player 1 is alive

            # Check how far from head is the closest part of the player 1 tail in the chosen direction
            for pos in p1_tail_pos:

                if pos[0] == snake_pos2[0] and distance > snake_pos2[1] - pos[1] > 0:
                    distance = snake_pos2[1] - pos[1]

                elif pos[0] == snake_pos2[0] and pos[1] - snake_pos2[1] > 0 and \
                        game_height - (pos[1] - snake_pos2[1]) < distance:
                    distance = snake_pos2[1] - pos[1] + game_height

        # Check how far from head is the closest part of it's own tail in the chosen direction
        for pos in p2_tail_pos:

            if pos[0] == snake_pos2[0] and distance > snake_pos2[1] - pos[1] > 0:
                distance = snake_pos2[1] - pos[1]

            elif pos[0] == snake_pos2[0] and pos[1] - snake_pos2[1] > 0 and \
                    game_height - (pos[1] - snake_pos2[1]) < distance:
                distance = snake_pos2[1] - pos[1] + game_height

        # Check how far from head is the closest wall in the chosen direction
        for pos in wall_pos:

            if pos[0] == snake_pos2[0] and distance > snake_pos2[1] - pos[1] > 0:
                distance = snake_pos2[1] - pos[1]

            elif pos[0] == snake_pos2[0] and pos[1] - snake_pos2[1] > 0 and \
                    game_height - (pos[1] - snake_pos2[1]) < distance:
                distance = snake_pos2[1] - pos[1] + game_height

    if direction == "down":
        distance = game_height
        if not player_dead:

            for pos in p1_tail_pos:

                if pos[0] == snake_pos2[0] and distance > pos[1] - snake_pos2[1] > 0:
                    distance = pos[1] - snake_pos2[1]

                elif pos[0] == snake_pos2[0] and snake_pos2[1] - pos[1] > 0 and \
                        game_height - (snake_pos2[1] - pos[1]) < distance:
                    distance = pos[1] - snake_pos2[1] + game_height

        for pos in p2_tail_pos:

            if pos[0] == snake_pos2[0] and distance > pos[1] - snake_pos2[1] > 0:
                distance = pos[1] - snake_pos2[1]

            elif pos[0] == snake_pos2[0] and snake_pos2[1] - pos[1] > 0 and \
                    game_height - (snake_pos2[1] - pos[1]) < distance:
                distance = pos[1] - snake_pos2[1] + game_height

        for pos in wall_pos:

            if pos[0] == snake_pos2[0] and distance > pos[1] - snake_pos2[1] > 0:
                distance = pos[1] - snake_pos2[1]

            elif pos[0] == snake_pos2[0] and snake_pos2[1] - pos[1] > 0 and \
                    game_height - (snake_pos2[1] - pos[1]) < distance:
                distance = pos[1] - snake_pos2[1] + game_height

    if direction == "right":
        distance = game_width
        if not player_dead:

            for pos in p1_tail_pos:

                if pos[1] == snake_pos2[1] and distance > pos[0] - snake_pos2[0] > 0:
                    distance = pos[0] - snake_pos2[0]

                elif pos[1] == snake_pos2[1] and snake_pos2[0] - pos[0] > 0 and \
                        game_width - (snake_pos2[0] - pos[0]) < distance:
                    distance = pos[0] - snake_pos2[0] + game_width

        for pos in p2_tail_pos:

            if pos[1] == snake_pos2[1] and distance > pos[0] - snake_pos2[0] > 0:
                distance = pos[0] - snake_pos2[0]

            elif pos[1] == snake_pos2[1] and snake_pos2[0] - pos[0] > 0 and \
                    game_width - (snake_pos2[0] - pos[0]) < distance:
                distance = pos[0] - snake_pos2[0] + game_width

        for pos in wall_pos:

            if pos[1] == snake_pos2[1] and distance > pos[0] - snake_pos2[0] > 0:
                distance = pos[0] - snake_pos2[0]

            elif pos[1] == snake_pos2[1] and snake_pos2[0] - pos[0] > 0 and \
                    game_width - (snake_pos2[0] - pos[0]) < distance:
                distance = pos[0] - snake_pos2[0] + game_width

    if direction == "left":
        distance = game_width
        if not player_dead:

            for pos in p1_tail_pos:

                if pos[1] == snake_pos2[1] and distance > snake_pos2[0] - pos[0] > 0:
                    distance = snake_pos2[0] - pos[0]

                elif pos[1] == snake_pos2[1] and pos[0] - snake_pos2[0] > 0 and \
                        game_width - (pos[0] - snake_pos2[0]) < distance:
                    distance = snake_pos2[0] - pos[0] + game_width

        for pos in p2_tail_pos:

            if pos[1] == snake_pos2[1] and distance > snake_pos2[0] - pos[0] > 0:
                distance = snake_pos2[0] - pos[0]

            elif pos[1] == snake_pos2[1] and pos[0] - snake_pos2[0] > 0 and \
                    game_width - (pos[0] - snake_pos2[0]) < distance:
                distance = snake_pos2[0] - pos[0] + game_width

        for pos in wall_pos:

            if pos[1] == snake_pos2[1] and distance > snake_pos2[0] - pos[0] > 0:
                distance = snake_pos2[0] - pos[0]

            elif pos[1] == snake_pos2[1] and pos[0] - snake_pos2[0] > 0 and \
                    game_width - (pos[0] - snake_pos2[0]) < distance:
                distance = snake_pos2[0] - pos[0] + game_width

    return distance


def is_stuck(check_pos, check_count, checking, rechecking, period):
    # Checks if snake is running in circles
    # only finds loops if they are not bigger than 7 times the size of the snake
    snake_memory_len = len(p2_tail_pos) * 7

    # If after checking, snake's head doesn't return to the same position again, stop checking
    if check_count >= snake_memory_len:
        checking = False

    if checking:
        check_count += 1

        # IF snake's head returns to the same position for the third time, start counting, if it takes the same period
        # Of time to get to the same location
        if check_pos == snake_pos2:
            period = len(snake_memory) - snake_memory.index(check_pos)
            checking = False
            rechecking = True
            check_count = 0

        result = (check_pos, check_count, checking, rechecking, period, False)

    elif rechecking:
        check_count += 1

        # If snake's head returns to the same location again, and it took as much time to return as last time,
        # Confirm that the snake is stuck and stop checking
        if check_count == period:
            if snake_pos2 == check_pos:
                rechecking = False
                result = (check_pos, check_count, checking, rechecking, period, True)

            # If it doesn't return to the same location in the same time, stop checking and confirm,
            # that snake isn't stuck
            else:
                rechecking = False
                result = (check_pos, check_count, checking, rechecking, period, False)
        else:
            result = (check_pos, check_count, checking, rechecking, period, False)

    # If snake's head was already in this position in snake's memory, start checking if snake is looping
    elif snake_pos2 in snake_memory:
        check_pos = [snake_pos2[0], snake_pos2[1]]
        checking = True
        check_count = 0
        result = (check_pos, check_count, checking, rechecking, period, False)

    else:
        # If didn't find anythong
        result = (check_pos, check_count, checking, rechecking, period, False)

    # If snake memory is full, delete the oldest snake position
    if len(snake_memory) >= snake_memory_len:
        snake_memory.pop(0)

    # Add the current snake head position to the snake memory list
    snake_memory.append([snake_pos2[0], snake_pos2[1]])
    return result


def check_sides(direction, distance, player_dead):
    # Check if snake isn't moving into a dead end, works only with straight 1 block wide tunnels
    # Stops AI from making some stupid decisions

    if direction == "up":

        for p in range(1, distance // 20):
            check1 = [snake_pos2[0] + 20, snake_pos2[1] - 20 * p]
            check2 = [snake_pos2[0] - 20, snake_pos2[1] - 20 * p]

            if check1[0] > game_width:
                check1 = [check1[0] - game_width, check1[1]]
            if check1[0] < 0:
                check1 = [check1[0] + game_width, check1[1]]
            if check2[0] > game_width:
                check2 = [check2[0] - game_width, check2[1]]
            if check2[0] < 0:
                check2 = [check2[0] + game_width, check2[1]]
            if check1[1] > game_height:
                check1 = [check1[0], check1[1] - game_height]
            if check1[1] < 0:
                check1 = [check1[0], check1[1] + game_height]
            if check2[1] > game_height:
                check2 = [check2[0], check2[1] - game_height]
            if check2[1] < 0:
                check2 = [check2[0], check2[1] + game_height]

            check1_col = False
            check2_col = False

            for pos in wall_pos:
                if pos == check1:
                    check1_col = True
                if pos == check2:
                    check2_col = True

            if not player_dead:
                for pos in p1_tail_pos:
                    if pos == check1:
                        check1_col = True
                    if pos == check2:
                        check2_col = True

            for pos in p2_tail_pos:
                if pos == check1:
                    check1_col = True
                if pos == check2:
                    check2_col = True

            if check1_col and check2_col:
                pass
            else:
                return False
        return True

    elif direction == "down":

        for p in range(1, distance // 20):
            check1 = [snake_pos2[0] + 20, snake_pos2[1] + 20 * p]
            check2 = [snake_pos2[0] - 20, snake_pos2[1] + 20 * p]

            if check1[0] > game_width:
                check1 = [check1[0] - game_width, check1[1]]
            if check1[0] < 0:
                check1 = [check1[0] + game_width, check1[1]]
            if check2[0] > game_width:
                check2 = [check2[0] - game_width, check2[1]]
            if check2[0] < 0:
                check2 = [check2[0] + game_width, check2[1]]
            if check1[1] > game_height:
                check1 = [check1[0], check1[1] - game_height]
            if check1[1] < 0:
                check1 = [check1[0], check1[1] + game_height]
            if check2[1] > game_height:
                check2 = [check2[0], check2[1] - game_height]
            if check2[1] < 0:
                check2 = [check2[0], check2[1] + game_height]

            check1_col = False
            check2_col = False

            for pos in wall_pos:
                if pos == check1:
                    check1_col = True
                if pos == check2:
                    check2_col = True

            if not player_dead:
                for pos in p1_tail_pos:
                    if pos == check1:
                        check1_col = True
                    if pos == check2:
                        check2_col = True

            for pos in p2_tail_pos:
                if pos == check1:
                    check1_col = True
                if pos == check2:
                    check2_col = True

            if check1_col and check2_col:
                pass
            else:
                return False
        return True

    elif direction == "left":

        for p in range(1, distance // 20):
            check1 = [snake_pos2[0] - 20 * p, snake_pos2[1] + 20]
            check2 = [snake_pos2[0] - 20 * p, snake_pos2[1] - 20]

            if check1[0] > game_width:
                check1 = [check1[0] - game_width, check1[1]]
            if check1[0] < 0:
                check1 = [check1[0] + game_width, check1[1]]
            if check2[0] > game_width:
                check2 = [check2[0] - game_width, check2[1]]
            if check2[0] < 0:
                check2 = [check2[0] + game_width, check2[1]]
            if check1[1] > game_height:
                check1 = [check1[0], check1[1] - game_height]
            if check1[1] < 0:
                check1 = [check1[0], check1[1] + game_height]
            if check2[1] > game_height:
                check2 = [check2[0], check2[1] - game_height]
            if check2[1] < 0:
                check2 = [check2[0], check2[1] + game_height]

            check1_col = False
            check2_col = False

            for pos in wall_pos:
                if pos == check1:
                    check1_col = True
                if pos == check2:
                    check2_col = True

            if not player_dead:
                for pos in p1_tail_pos:
                    if pos == check1:
                        check1_col = True
                    if pos == check2:
                        check2_col = True

            for pos in p2_tail_pos:
                if pos == check1:
                    check1_col = True
                if pos == check2:
                    check2_col = True

            if check1_col and check2_col:
                pass
            else:
                return False
        return True

    elif direction == "right":

        for p in range(1, distance // 20):
            check1 = [snake_pos2[0] + 20 * p, snake_pos2[1] + 20]
            check2 = [snake_pos2[0] + 20 * p, snake_pos2[1] - 20]

            if check1[0] > game_width:
                check1 = [check1[0] - game_width, check1[1]]
            if check1[0] < 0:
                check1 = [check1[0] + game_width, check1[1]]
            if check2[0] > game_width:
                check2 = [check2[0] - game_width, check2[1]]
            if check2[0] < 0:
                check2 = [check2[0] + game_width, check2[1]]
            if check1[1] > game_height:
                check1 = [check1[0], check1[1] - game_height]
            if check1[1] < 0:
                check1 = [check1[0], check1[1] + game_height]
            if check2[1] > game_height:
                check2 = [check2[0], check2[1] - game_height]
            if check2[1] < 0:
                check2 = [check2[0], check2[1] + game_height]

            check1_col = False
            check2_col = False

            for pos in wall_pos:
                if pos == check1:
                    check1_col = True
                if pos == check2:
                    check2_col = True

            if not player_dead:
                for pos in p1_tail_pos:
                    if pos == check1:
                        check1_col = True
                    if pos == check2:
                        check2_col = True

            for pos in p2_tail_pos:
                if pos == check1:
                    check1_col = True
                if pos == check2:
                    check2_col = True

            if check1_col and check2_col:
                pass
            else:
                return False
        return True


def AI_move(stuck, move, hunger, player_dead):
    # AI choosing direction to move

    # If snake doesn't eat, it gets hungry
    hunger += 1
    # Checks the distance to the closest obstacle in each direction
    obst_up = snake_look("up", player_dead)
    obst_down = snake_look("down", player_dead)
    obst_left = snake_look("left", player_dead)
    obst_right = snake_look("right", player_dead)

    # If snake starts looping, move to the farthest open location
    if stuck:
        if move == 0:
            move = [obst_up, "up"]
            if obst_down > move[0]:
                move = [obst_down, "down"]
            if obst_left > move[0]:
                move = [obst_left, "left"]
            if obst_right > move[0]:
                move = [obst_right, "right"]

        if move[0] > 40:
            move = [move[0] - 20, move[1]]
            return move[1], move, stuck, hunger

        if move[0] == 40:
            temp = move[1]
            move = 0
            stuck = False
            return temp, move, stuck, hunger

    # If snake doesn't eat for 300 moves, it starts moving randomly until it finds food
    if hunger > 300:
        rand = 0

        while rand < 20:
            rand += 1
            choice = random.randint(1, 4)
            if choice == 1 and obst_up > 20 and not check_sides("up", obst_up, player_dead):
                return "up", move, stuck, hunger
            elif choice == 2 and obst_left > 20 and not check_sides("left", obst_left, player_dead):
                return "left", move, stuck, hunger
            elif choice == 3 and obst_down > 20 and not check_sides("down", obst_down, player_dead):
                return "down", move, stuck, hunger
            elif choice == 4 and obst_right > 20 and not check_sides("right", obst_right, player_dead):
                return "right", move, stuck, hunger

    # Choose the closest food as target
    x = snake_pos2[0] - food_pos[0][0][0]
    y = snake_pos2[1] - food_pos[0][0][1]
    target = [x, y]

    if x < 0:
        x *= -1
    if y < 0:
        y *= -1

    food_distance = x + y
    for pos in food_pos:
        x = snake_pos2[0] - pos[0][0]
        y = snake_pos2[1] - pos[0][1]

        if x < 0:
            x *= -1
        x1 = game_width - x
        if x1 < x:
            x = x1

        if y < 0:
            y *= -1
        y1 = game_height - y
        if y1 < y:
            y = y1

        if x + y <= food_distance:
            food_distance = x + y
            target = [snake_pos2[0] - pos[0][0], snake_pos2[1] - pos[0][1]]

    # Decide to move  directly to target or teleport through map borders
    if target[0] > game_width//2:
        target = [target[0] - game_width, target[1]]
    elif target[0] * -1 > game_width // 2:
        target = [target[0] + game_width, target[1]]
    if target[1] > game_height//2:
        target = [target[0], target[1] - game_height]
    elif target[1] * -1 > game_width // 2:
        target = [target[0], target[1] + game_height]

    # Move choosing part
    # If snake can move closer to target food and it's not going into a dead end, go
    if target[0] < 0 and obst_right > 20 and not check_sides("right", obst_right, player_dead):
        return "right", move, stuck, hunger
    if target[0] > 0 and obst_left > 20 and not check_sides("left", obst_left, player_dead):
        return "left", move, stuck, hunger
    if target[1] < 0 and obst_down > 20 and not check_sides("down", obst_down, player_dead):
        return "down", move, stuck, hunger
    if target[1] > 0 and obst_up > 20 and not check_sides("up", obst_up, player_dead):
        return "up", move, stuck, hunger

    # If one direction is way more open than others, move in that direction to avoid getting stuck
    if obst_up > obst_down + obst_left + obst_right:
        return "up", move, stuck, hunger
    if obst_down > obst_up + obst_left + obst_right:
        return "down", move, stuck, hunger
    if obst_left > obst_up + obst_down + obst_right:
        return "left", move, stuck, hunger
    if obst_right > obst_up + obst_left + obst_down:
        return "right", move, stuck, hunger

    # If there's no obstacle in the way, and not going into a dead end, move
    if obst_up > 20 and not check_sides("up", obst_up, player_dead):
        return "up", move, stuck, hunger
    if obst_left > 20 and not check_sides("left", obst_left, player_dead):
        return "left", move, stuck, hunger
    if obst_down > 20 and not check_sides("down", obst_down, player_dead):
        return "down", move, stuck, hunger
    if obst_right > 20 and not check_sides("right", obst_right, player_dead):
        return "right", move, stuck, hunger

    # Move, even if going into a dead end, as long as not directly running into an obstacle
    if obst_left > 20:
        return "left", move, stuck, hunger
    if obst_right > 20:
        return "right", move, stuck, hunger
    if obst_up > 20:
        return "up", move, stuck, hunger
    if obst_down > 20:
        return "down", move, stuck, hunger


while True:

    # Save game screen
    while save_game:
        game_screen_set = False
        menu = True
        game_over = False
        screen = pygame.display.set_mode([menu_width, menu_height])

        screen.fill(menu_color)

        # Create button, text box and text labels
        ok_button = Button(hscores_button_color, menu_width // 2 - 100, menu_height // 8 * 6, 200, 100, "Save")
        ok_button.draw(screen, button_outline_color)

        enter_name = TextBox(enter_name_color, 100, 300, 600, 50, text=user_input)
        enter_name.draw(screen)
        enter_name_font = pygame.font.SysFont("arealblack", 70)

        tbox_font = pygame.font.SysFont("monospace", 50, bold=True)
        map_size_text = tbox_font.render("-- Save game --", 1, black_color)
        text = tbox_font.render("Enter save name:", 1, black_color)
        screen.blit(text, (110, 220))
        screen.blit(map_size_text, (180, 20))

        if error:
            # Display error text label
            error_label = tbox_font.render(error_msg, 1, (200, 0, 0))
            screen.blit(error_label, (50, 150))

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()

            # If mouse is hovering over, change color
            if event.type == pygame.MOUSEMOTION:

                if ok_button.is_over(mouse_pos):
                    hscores_button_color = (120, 120, 0)
                else:
                    hscores_button_color = (150, 150, 0)

                if enter_name.is_over(mouse_pos):
                    enter_name_color = (80, 50, 0)
                else:
                    enter_name_color = (90, 90, 0)

            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                if ok_button.is_over(mouse_pos) or event.type == pygame.QUIT:
                    if user_input == "":
                        user_input = "QUICKSAVE"

                    # Try reading from the save file, create the file if it doesn't exist
                    try:
                        save_file = open("game_saves.txt", "r")
                    except FileNotFoundError:
                        save_file = open("game_saves.txt", "x")
                        save_file = open("game_saves.txt", "r")

                    save_dictionary = save_file.read()
                    save_file.close()

                    try:
                        save_dictionary = ast.literal_eval(save_dictionary)
                    except Exception:
                        save_dictionary = {}

                    # If save name not taken, save game and open menu
                    if user_input not in save_dictionary.keys():
                        save_dictionary.update({user_input: save_data})
                        save_file = open("game_saves.txt", "w")
                        save_file.write(str(save_dictionary))
                        save_file.close()
                        game_over1 = False
                        game_over2 = False
                        save_game = False
                        menu = True
                        error = False

                    # If save name not given, save game as "QUICKSAVE" and delete the old quicksave
                    elif user_input == "QUICKSAVE":
                        save_dictionary.pop(user_input)
                        save_dictionary.update({user_input: save_data})
                        save_file = open("game_saves.txt", "w")
                        save_file.write(str(save_dictionary))
                        save_file.close()
                        game_over1 = False
                        game_over2 = False
                        save_game = False
                        menu = True
                        error = False

                    else:
                        # If save name is taken, display error
                        error = True
                        error_msg = "Name '" + user_input + "' taken!"

                # If clicked on text box, change color and receive input
                if enter_name.is_over(mouse_pos):
                    user_input = enter_name.display_input(20)
                    enter_name_color = (90, 90, 0)

        tbox_text = tbox_font.render(user_input, 1, black_color)
        screen.blit(tbox_text, (enter_name.x, enter_name.y))
        pygame.display.update()

    # Game over screen
    while game_over:
        if not checked_score:

            # Check who won
            if multiplayer and score2 > score:
                score = score2
                game_result = "p2"
                user_input = "PLAYER 2"

            elif AI and score2 > score:
                score = score2
                game_result = "AI"
                user_input = "AI"

            elif score2 == score:
                game_result = "tie"

            elif AI and score2 < score:
                game_result = "AI-p1"

            elif multiplayer:
                game_result = "p1"
                user_input = "PLAYER 1"

            else:
                game_result = "singleplayer"

            checked_score = True

        game_screen_set = False
        screen = pygame.display.set_mode([menu_width, menu_height])

        # Check if new high score
        new_hscore = True
        score_check = open("highscore.txt", "r")

        try:
            file_text = score_check.read()
            score_dictionary = ast.literal_eval(file_text)
            for old_score in score_dictionary.values():
                if score - 1 <= old_score:
                    new_hscore = False
        except Exception:
            new_hscore = True

        score_check.close()

        # Draw GUI
        screen.fill((110, 0, 0))
        ok_button = Button(ok_button_color, menu_width // 2 - 100, menu_height // 8 * 6, 200, 100, " OK ")
        ok_button.draw(screen, button_outline_color)
        game_over_font = pygame.font.SysFont("arealblack", 85)
        enter_name_font = pygame.font.SysFont("arealblack", 50, )

        if game_result == "p2":
            death_message_1 = game_over_font.render("Player 2 Won!", 1, black_color)
            death_message_2 = game_over_font.render("Player 2 score was: " + str(score - 1), 1, black_color)
            death_message_4 = enter_name_font.render("Enter your name:", 1, black_color)
            screen.blit(death_message_4, (20, 350))
            screen.blit(death_message_2, (120, 100))
            screen.blit(death_message_1, (220, 20))

        elif game_result == "AI":
            death_message_1 = game_over_font.render("Computer Won!", 1, black_color)
            death_message_2 = game_over_font.render("Computer score was: " + str(score - 1), 1, black_color)
            death_message_4 = enter_name_font.render("Enter your name:", 1, black_color)
            screen.blit(death_message_2, (70, 100))
            screen.blit(death_message_1, (170, 20))

        elif game_result == "AI-p1":
            death_message_1 = game_over_font.render(" You Won!", 1, black_color)
            death_message_2 = game_over_font.render("Your score was: " + str(score - 1), 1, black_color)
            death_message_4 = enter_name_font.render("Enter your name:", 1, black_color)
            screen.blit(death_message_4, (20, 350))
            screen.blit(death_message_1, (270, 20))
            screen.blit(death_message_2, (170, 100))

        elif game_result == "tie":
            death_message_1 = game_over_font.render("You Tied!", 1, black_color)
            death_message_2 = game_over_font.render("Your score was: " + str(score - 1), 1, black_color)
            death_message_4 = enter_name_font.render("Enter your name:", 1, black_color)
            screen.blit(death_message_4, (20, 350))
            screen.blit(death_message_2, (170, 100))
            screen.blit(death_message_1, (270, 20))

        elif game_result == "p1":
            death_message_1 = game_over_font.render("Player 1 Won!", 1, black_color)
            death_message_2 = game_over_font.render("Player 1 score was: " + str(score - 1), 1, black_color)
            death_message_4 = enter_name_font.render("Enter your name:", 1, black_color)
            screen.blit(death_message_4, (20, 350))
            screen.blit(death_message_2, (120, 100))
            screen.blit(death_message_1, (220, 20))

        elif game_result == "singleplayer":
            death_message_1 = game_over_font.render("You Died!", 1, black_color)
            death_message_2 = game_over_font.render("Your score was: " + str(score - 1), 1, black_color)
            death_message_4 = enter_name_font.render("Enter your name:", 1, black_color)
            screen.blit(death_message_4, (20, 350))
            screen.blit(death_message_1, (270, 20))
            screen.blit(death_message_2, (170, 100))

        enter_name = TextBox(enter_name_color, 350, 345, 400, 50)
        enter_name.draw(screen)

        if new_hscore:
            death_message_3 = game_over_font.render("New High Score!", 1, (150, 150, 0))
            screen.blit(death_message_3, (185, 180))

        for event in pygame.event.get():
            # Get mouse position
            mouse_pos = pygame.mouse.get_pos()

            # If click (x) go to main menu
            if event.type == pygame.QUIT:
                if user_input == "":
                    user_input = "UNKNOWN"

                # Save high score onto file
                score_check = open("highscore.txt", "r")
                try:
                    if user_input in score_dictionary.keys() and score - 1 > score_dictionary[user_input]:
                        score_dictionary[user_input] = score - 1
                    elif user_input not in list(score_dictionary.keys()):
                        score_dictionary.update({user_input: score - 1})
                except Exception:
                    score_dictionary = {user_input: score - 1}

                score_check.close()
                score_check = open("highscore.txt", "w")
                score_check.write(str(score_dictionary))
                score_check.close()
                user_input = ""
                game_over1 = False
                game_over2 = False
                AI = False
                multiplayer = False
                checked_score = False
                new_hscore = False
                menu = True
                game_over = False

                # Action when mouse button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If click on ok button
                if ok_button.is_over(mouse_pos):
                    if user_input == "":
                        user_input = "UNKNOWN"

                    # Save high score onto file
                    score_check = open("highscore.txt", "r")
                    try:
                        if user_input in score_dictionary.keys() and score - 1 > score_dictionary[user_input]:
                            score_dictionary[user_input] = score - 1
                        elif user_input not in list(score_dictionary.keys()):
                            score_dictionary.update({user_input: score - 1})
                    except Exception:
                        score_dictionary = {user_input: score - 1}

                    score_check.close()
                    score_check = open("highscore.txt", "w")
                    score_check.write(str(score_dictionary))
                    score_check.close()
                    user_input = ""
                    game_over1 = False
                    game_over2 = False
                    AI = False
                    multiplayer = False
                    checked_score = False
                    new_hscore = False
                    menu = True
                    game_over = False

                # If click on Text box
                if enter_name.is_over(mouse_pos):
                    if game_result == "AI":
                        tbox_font = pygame.font.SysFont("monospace", 50, bold=True)
                        text = tbox_font.render(user_input, 1, black_color)
                        screen.blit(text, (enter_name.x, enter_name.y))
                    else:
                        user_input = enter_name.display_input(13)
                    enter_name_color = (90, 90, 0)

            # Change color when mouse hovers over
            if event.type == pygame.MOUSEMOTION:
                if ok_button.is_over(mouse_pos):
                    ok_button_color = (65, 114, 202)
                else:
                    ok_button_color = (100, 149, 237)

                if enter_name.is_over(mouse_pos):
                    enter_name_color = (80, 50, 0)
                else:
                    enter_name_color = (90, 90, 0)
            # Display user input
            tbox_font = pygame.font.SysFont("monospace", 50, bold=True, italic=True)
            tbox_text = tbox_font.render(user_input, 1, black_color)
            screen.blit(tbox_text, (enter_name.x, enter_name.y))
            pygame.display.update()

    # Main Menu
    while menu:
        screen.fill(menu_color)

        # Check if High score exists
        try:
            score_check = open("highscore.txt", "r")
        except FileNotFoundError:
            score_check = open("highscore.txt", "x")
            score_check = open("highscore.txt", "r")

        try:
            file_text = score_check.read()
            score_dictionary = ast.literal_eval(file_text)
            max_name = ("NOBODY", 0)
            for item in score_dictionary.items():
                if item[1] > max_name[1]:
                    max_name = item
            hiscore = str(max_name[1])
            hiscore_player = max_name[0]
        except Exception:
            hiscore = "0"
            hiscore_player = "NOBODY"
        score_check.close()

        # Write text (high score, player name)
        title_font = pygame.font.SysFont("monospace", 85, bold=True)
        hiscore_font = pygame.font.SysFont("monospace", 40, bold=True)
        hiscore_text = hiscore_font.render(("High score: " + hiscore + " by " + hiscore_player), 1, black_color)
        screen.blit(hiscore_text, (10, 100))
        title = title_font.render("Snake", 1, (190, 0, 0))
        screen.blit(title, (270, 10))

        # Define and draw buttons
        ok_button = Button(ok_button_color, menu_width // 2 - 100, menu_height // 8 * 6, 200, 100, " OK ")
        play_button = Button(start_button_color, menu_width // 2 - 125, 200, 250, 125, "Play!")
        exit_button = Button(exit_button_color, menu_width // 2 - 100, 470, 200, 100, "Exit")
        settings_button = Button(ok_button_color, menu_width // 2 + 100, 350, 200, 100, "Settings")
        hscores_button = Button(hscores_button_color, menu_width // 2 - 300, 350, 200, 100, "Scores")

        exit_button.draw(screen, button_outline_color)
        settings_button.draw(screen, button_outline_color)
        hscores_button.draw(screen, button_outline_color)
        play_button.draw(screen, button_outline_color)

        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                sys.exit()

            # Action when mouse button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.is_over(mouse_pos):
                    game_choice_menu = True

                if exit_button.is_over(mouse_pos):
                    sys.exit()

                if settings_button.is_over(mouse_pos):
                    settings_menu = True

                if hscores_button.is_over(mouse_pos):
                    hscore_display = True

                # Change color when mouse hovers over
            if event.type == pygame.MOUSEMOTION:

                if exit_button.is_over(mouse_pos):
                    exit_button_color = (100, 10, 0)
                else:
                    exit_button_color = (150, 0, 0)

                if play_button.is_over(mouse_pos):
                    start_button_color = (50, 100, 0)
                else:
                    start_button_color = (100, 150, 0)

                if settings_button.is_over(mouse_pos):
                    ok_button_color = (65, 114, 202)
                else:
                    ok_button_color = (100, 149, 237)

                if hscores_button.is_over(mouse_pos):
                    hscores_button_color = (120, 120, 0)
                else:
                    hscores_button_color = (150, 150, 0)

        # Settings menu
        while settings_menu:
            screen.fill(menu_color)
            ok_button = Button(ok_button_color, 550, 465, 200, 100, " OK ")
            ok_button.draw(screen, black_color)

            # Create text labels
            tbox_font = pygame.font.SysFont("monospace", 50, bold=True)
            tbox_small_font = pygame.font.SysFont("monospace", 40)
            small_label_font = pygame.font.SysFont("monospace", 35, bold=True)

            map_size_text = tbox_font.render("--Change map size--", 1, black_color)
            screen.blit(map_size_text, (100, 20))

            by_grid_text = tbox_small_font.render("by grid size:", 1, black_color)
            screen.blit(by_grid_text, (450, 70))

            by_res_text = tbox_small_font.render("by resolution:", 1, black_color)
            screen.blit(by_res_text, (50, 70))

            speed_text = tbox_font.render("Speed:", 1, black_color)
            screen.blit(speed_text, (70, 370))

            walls_text = tbox_font.render("Walls:", 1, black_color)
            screen.blit(walls_text, (70, 290))

            walls_text = tbox_font.render(" Food:", 1, black_color)
            screen.blit(walls_text, (70, 450))

            wall_mode_text1 = small_label_font.render("Glued wall", 1, black_color)
            screen.blit(wall_mode_text1, (530, 280))

            wall_mode_text2 = small_label_font.render("mode:", 1, black_color)
            screen.blit(wall_mode_text2, (590, 310))

            x_text = tbox_font.render("X:", 1, black_color)
            screen.blit(x_text, (70, 130))
            screen.blit(x_text, (470, 130))

            y_text = tbox_font.render("Y:", 1, black_color)
            screen.blit(y_text, (70, 200))
            screen.blit(y_text, (470, 200))

            # Draw text boxes
            food_tbox = TextBox(food_tbox_color, 280, 450, 200, 50, num_only=True)
            food_tbox.draw(screen)

            speed_tbox = TextBox(speed_tbox_color, 280, 370, 200, 50, num_only=True)
            speed_tbox.draw(screen)

            walls_tbox = TextBox(walls_tbox_color, 280, 290, 200, 50, num_only=True)
            walls_tbox.draw(screen)

            resx_tbox = TextBox(resx_tbox_color, 140, 130, 200, 50, num_only=True)
            resx_tbox.draw(screen)

            resy_tbox = TextBox(resy_tbox_color, 140, 200, 200, 50, num_only=True)
            resy_tbox.draw(screen)

            gridx_tbox = TextBox(gridx_tbox_color, 540, 130, 200, 50, num_only=True)
            gridx_tbox.draw(screen)

            gridy_tbox = TextBox(gridy_tbox_color, 540, 200, 200, 50, num_only=True)
            gridy_tbox.draw(screen)

            if glued_wall_mode:
                wall_mode = Checkbox(cbox_on_color, 610, 370, 50)
            else:
                wall_mode = Checkbox(cbox_off_color, 610, 370, 50)
            wall_mode.draw(screen)

            # Text box text
            speed_tbox_text = tbox_font.render(str(speed), 1, black_color)
            screen.blit(speed_tbox_text, (speed_tbox.x, speed_tbox.y))

            food_tbox_text = tbox_font.render(str(max_food), 1, black_color)
            screen.blit(food_tbox_text, (food_tbox.x, food_tbox.y))

            walls_tbox_text = tbox_font.render(str(walls), 1, black_color)
            screen.blit(walls_tbox_text, (walls_tbox.x, walls_tbox.y))

            resx_tbox_text = tbox_font.render(str(game_width), 1, black_color)
            screen.blit(resx_tbox_text, (resx_tbox.x, resx_tbox.y))

            resy_tbox_text = tbox_font.render(str(game_height), 1, black_color)
            screen.blit(resy_tbox_text, (resy_tbox.x, resy_tbox.y))

            gridx_tbox_text = tbox_font.render(str(game_width // 20), 1, black_color)
            screen.blit(gridx_tbox_text, (gridx_tbox.x, gridx_tbox.y))

            gridy_tbox_text = tbox_font.render(str(game_height // 20), 1, black_color)
            screen.blit(gridy_tbox_text, (gridy_tbox.x, gridy_tbox.y))

            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()

                # Change color if mouse hovers over
                if event.type == pygame.MOUSEMOTION:

                    if ok_button.is_over(mouse_pos):
                        ok_button_color = (65, 114, 202)
                    else:
                        ok_button_color = (100, 149, 237)

                    if food_tbox.is_over(mouse_pos):
                        food_tbox_color = (80, 50, 0)
                    else:
                        food_tbox_color = (90, 90, 0)

                    if speed_tbox.is_over(mouse_pos):
                        speed_tbox_color = (80, 50, 0)
                    else:
                        speed_tbox_color = (90, 90, 0)

                    if walls_tbox.is_over(mouse_pos):
                        walls_tbox_color = (80, 50, 0)
                    else:
                        walls_tbox_color = (90, 90, 0)

                    if resx_tbox.is_over(mouse_pos):
                        resx_tbox_color = (80, 50, 0)
                    else:
                        resx_tbox_color = (90, 90, 0)

                    if resy_tbox.is_over(mouse_pos):
                        resy_tbox_color = (80, 50, 0)
                    else:
                        resy_tbox_color = (90, 90, 0)

                    if gridx_tbox.is_over(mouse_pos):
                        gridx_tbox_color = (80, 50, 0)
                    else:
                        gridx_tbox_color = (90, 90, 0)

                    if gridy_tbox.is_over(mouse_pos):
                        gridy_tbox_color = (80, 50, 0)
                    else:
                        gridy_tbox_color = (90, 90, 0)

                    if wall_mode.is_over(mouse_pos) and glued_wall_mode:
                        cbox_on_color = (80, 0, 0)
                    elif wall_mode.is_over(mouse_pos):
                        cbox_off_color = (40, 40, 40)

                    elif glued_wall_mode:
                        cbox_on_color = (100, 0, 0)
                    else:
                        cbox_off_color = (20, 20, 20)

                # If mouse button pressed
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if ok_button.is_over(mouse_pos):
                        settings_menu = False

                    # Change settings
                    if food_tbox.is_over(mouse_pos):
                        food_tbox.draw(screen)
                        temp = food_tbox.display_input(4)
                        if not temp == "":
                            max_food = int(temp)
                        if max_food > ((game_width//20) * (game_height//20)) // 100 * 30:
                            max_food = ((game_width//20) * (game_height//20)) // 100 * 30
                        if max_food == 0:
                            max_food = 1

                    if speed_tbox.is_over(mouse_pos):
                        speed_tbox.draw(screen)
                        temp = speed_tbox.display_input(3)
                        if not temp == "":
                            speed = int(temp)
                        if speed > 100:
                            speed = 100

                    if walls_tbox.is_over(mouse_pos):
                        walls_tbox.draw(screen)
                        temp = walls_tbox.display_input(4)
                        if not temp == "":
                            walls = int(temp)
                        if walls > (game_height // 20 * (game_width // 20) // 2) and not glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 2)
                        elif walls > (game_height // 20 * (game_width // 20) // 10) and glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 10)

                    if resx_tbox.is_over(mouse_pos):
                        resx_tbox.draw(screen)
                        temp = resx_tbox.display_input(5)
                        if not temp == "":
                            game_width = int(temp)
                        if game_width > monitor_width:
                            game_width = monitor_width
                        if not game_width % 20 == 0:
                            game_width = game_width // 20 * 20
                        if game_width < 400:
                            game_width = 400
                        if walls > (game_height // 20 * (game_width // 20) // 2) and not glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 2)
                        elif walls > (game_height // 20 * (game_width // 20) // 10) and glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 10)
                        if max_food > ((game_width//20) * (game_height//20)) // 100 * 30:
                            max_food = ((game_width//20) * (game_height//20)) // 100 * 30

                    if resy_tbox.is_over(mouse_pos):
                        resy_tbox.draw(screen)
                        temp = resy_tbox.display_input(5)
                        if not temp == "":
                            game_height = int(temp)
                        if game_height > monitor_height:
                            game_height = monitor_height
                        if not game_height % 20 == 0:
                            game_height = game_height // 20 * 20
                        if game_height < 400:
                            game_height = 400
                        if walls > (game_height // 20 * (game_width // 20) // 2) and not glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 2)
                        elif walls > (game_height // 20 * (game_width // 20) // 10) and glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 10)
                        if max_food > ((game_width//20) * (game_height//20)) // 100 * 30:
                            max_food = ((game_width//20) * (game_height//20)) // 100 * 30

                    if gridx_tbox.is_over(mouse_pos):
                        gridx_tbox.draw(screen)
                        temp = gridx_tbox.display_input(3)
                        if not temp == "":
                            grid_size = int(temp)
                            game_width = grid_size * 20
                        if game_width > monitor_width:
                            game_width = monitor_width
                        if not game_width % 20 == 0:
                            game_width = game_width // 20 * 20
                        if game_width < 400:
                            game_width = 400
                        if walls > (game_height // 20 * (game_width // 20) // 2) and not glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 2)
                        elif walls > (game_height // 20 * (game_width // 20) // 10) and glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 10)
                        if max_food > ((game_width//20) * (game_height//20)) // 100 * 30:
                            max_food = ((game_width//20) * (game_height//20)) // 100 * 30

                    if gridy_tbox.is_over(mouse_pos):
                        gridy_tbox.draw(screen)
                        temp = gridy_tbox.display_input(3)
                        if not temp == "":
                            grid_size = int(temp)
                            game_height = grid_size * 20
                        if game_height > monitor_height:
                            game_height = monitor_height
                        if game_height < 400:
                            game_height = 400
                        if walls > (game_height // 20 * (game_width // 20) // 2) and not glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 2)
                        elif walls > (game_height // 20 * (game_width // 20) // 10) and glued_wall_mode:
                            walls = (game_height // 20 * (game_width // 20) // 10)
                        if max_food > ((game_width//20) * (game_height//20)) // 100 * 30:
                            max_food = ((game_width//20) * (game_height//20)) // 100 * 30

                    if wall_mode.is_over(mouse_pos) and glued_wall_mode:
                        glued_wall_mode = False
                    elif wall_mode.is_over(mouse_pos):
                        glued_wall_mode = True
                        if walls > (game_height // 20 * (game_width // 20) // 10):
                            walls = (game_height // 20 * (game_width // 20) // 10)

            pygame.display.update()

        # High score list
        while hscore_display:
            screen.fill(menu_color)

            score_check = open("highscore.txt", "r")
            try:
                sorted_dictionary = []
                file_text = score_check.read()
                score_dictionary = ast.literal_eval(file_text)
                sorted_scores = list(score_dictionary.values())
                sorted_scores.sort(reverse=True)
                sorted_scores = list(dict.fromkeys(sorted_scores))
                for num in sorted_scores:
                    for name in list(score_dictionary.keys()):
                        if score_dictionary[name] == num:
                            sorted_dictionary.append([name, num])

            except Exception:
                sorted_dictionary = [["NOBODY", 0]]
            score_check.close()

            tbox_font = pygame.font.SysFont("monospace", 50, bold=True)
            title = tbox_font.render("-- Top 10 Players --", 1, black_color)
            screen.blit(title, (100, 0))

            count = 0
            y = 60
            # Display top 10 players by high score
            for item in sorted_dictionary:
                count += 1
                score_text = hiscore_font.render(str(count) + ". " + item[0], 1, black_color)
                score_text1 = hiscore_font.render(": " + str(item[1]), 1, black_color)
                screen.blit(score_text, (130, y))
                screen.blit(score_text1, (560, y))
                y += 45
                if count == 10:
                    break

            ok_button = Button(ok_button_color, menu_width // 8, menu_height // 8 * 7, 600, 50, " OK ")
            ok_button.draw(screen, black_color, shape="rectangle")

            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEMOTION:
                    if ok_button.is_over(mouse_pos):
                        ok_button_color = (65, 114, 202)
                    else:
                        ok_button_color = (100, 149, 237)

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if ok_button.is_over(mouse_pos):
                        hscore_display = False

            pygame.display.update()

        # Game choice menu
        while game_choice_menu:
            screen.fill(menu_color)

            back_button = Button(exit_button_color, 0, 500, 200, 100, "Back")
            new_game_button = Button(start_button_color, 100, 50, 300, 200, "")
            new_map_button = Button(start_button_color1, 400, 50, 300, 200, "")
            load_game_button = Button(hscores_button_color, 100, 250, 300, 200, "")
            load_map_button = Button(hscores_button_color1, 400, 250, 300, 200, "")
            back_button.draw(screen, button_outline_color, shape="rectangle")
            new_game_button.draw(screen, button_outline_color, shape="rectangle")
            new_map_button.draw(screen, button_outline_color, shape="rectangle")
            load_game_button.draw(screen, button_outline_color, shape="rectangle")
            load_map_button.draw(screen, button_outline_color, shape="rectangle")

            button_font = pygame.font.SysFont('comicsans', 70)
            new_text = button_font.render("New", 1, black_color)
            load_text = button_font.render("Load", 1, black_color)
            map_text = button_font.render("Map", 1, black_color)
            game_text = button_font.render("Game", 1, black_color)

            screen.blit(new_text, (200, 90))
            screen.blit(new_text, (500, 90))
            screen.blit(game_text, (180, 150))
            screen.blit(map_text, (495, 150))
            screen.blit(load_text, (190, 290))
            screen.blit(load_text, (490, 290))
            screen.blit(game_text, (175, 350))
            screen.blit(map_text, (495, 350))

            hint_font = pygame.font.SysFont("monospace", 25, bold=True)
            hint_text1 = hint_font.render("Click \"Enter\" to save while playing", 1, text_color)
            hint_text2 = hint_font.render("or while creating a new map!", 1, text_color)
            screen.blit(hint_text1, (230, 500))
            screen.blit(hint_text2, (230, 540))

            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    game_choice_menu = False

                elif event.type == pygame.MOUSEMOTION:

                    if back_button.is_over(mouse_pos):
                        exit_button_color = (100, 10, 0)
                    else:
                        exit_button_color = (150, 0, 0)

                    if new_game_button.is_over(mouse_pos):
                        start_button_color = (50, 100, 0)
                    else:
                        start_button_color = (100, 150, 0)

                    if new_map_button.is_over(mouse_pos):
                        start_button_color1 = (50, 100, 0)
                    else:
                        start_button_color1 = (100, 150, 0)

                    if load_game_button.is_over(mouse_pos):
                        hscores_button_color = (120, 120, 0)
                    else:
                        hscores_button_color = (150, 150, 0)

                    if load_map_button.is_over(mouse_pos):
                        hscores_button_color1 = (120, 120, 0)
                    else:
                        hscores_button_color1 = (150, 150, 0)

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if back_button.is_over(mouse_pos):
                        game_choice_menu = False

                    if new_game_button.is_over(mouse_pos):
                        choose_mode = True
                        game_type = "new"

                    if new_map_button.is_over(mouse_pos):
                        new_map = True
                        wall_pos = []
                        auto_draw = False
                        auto_delete = False

                    if load_game_button.is_over(mouse_pos):
                        load_game = True

                    if load_map_button.is_over(mouse_pos):
                        load_map = True
                        open_page = 1
                        last_page_count = 0

            pygame.display.update()

            # Load game menu
            while load_game:

                screen.fill(menu_color)

                ok_button = Button(hscores_button_color, menu_width // 2 + 150, menu_height // 8 * 6, 200, 100, "Load")
                ok_button.draw(screen, button_outline_color)

                delete_button = Button(exit_button_color, menu_width // 2 - 100, menu_height // 8 * 6, 200, 100,
                                       "Delete")
                delete_button.draw(screen, button_outline_color)

                exit_button = Button(exit_button_color1, 0, menu_height - 100, 200, 100, "Back")
                exit_button.draw(screen, button_outline_color, shape="rectangle")

                enter_name = TextBox(enter_name_color, 100, 300, 600, 50)
                enter_name.draw(screen)
                enter_name_font = pygame.font.SysFont("arealblack", 70)

                tbox_font = pygame.font.SysFont("monospace", 50, bold=True)
                map_size_text = tbox_font.render("-- Load game --", 1, black_color)
                text = tbox_font.render("Enter save name:", 1, black_color)
                screen.blit(text, (110, 220))
                screen.blit(map_size_text, (180, 20))

                if error:
                    error_label = tbox_font.render(error_msg, 1, (200, 0, 0))
                    screen.blit(error_label, (50, 150))

                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        load_game = False

                    if event.type == pygame.MOUSEMOTION:

                        if ok_button.is_over(mouse_pos):
                            hscores_button_color = (120, 120, 0)
                        else:
                            hscores_button_color = (150, 150, 0)

                        if enter_name.is_over(mouse_pos):
                            enter_name_color = (80, 50, 0)
                        else:
                            enter_name_color = (90, 90, 0)

                        if delete_button.is_over(mouse_pos):
                            exit_button_color = (100, 10, 0)
                        else:
                            exit_button_color = (150, 0, 0)

                        if exit_button.is_over(mouse_pos):
                            exit_button_color1 = (100, 10, 0)
                        else:
                            exit_button_color1 = (150, 0, 0)

                    if event.type == pygame.MOUSEBUTTONDOWN:

                        if ok_button.is_over(mouse_pos):

                            if user_input == "":
                                user_input = "QUICKSAVE"

                            try:
                                save_file = open("game_saves.txt", "r")
                            except FileNotFoundError:
                                error = True
                                error_msg = "No saved games!"
                            else:
                                save_dictionary = save_file.read()
                                save_file.close()

                                try:
                                    save_dictionary = ast.literal_eval(save_dictionary)
                                except Exception:
                                    error = True
                                    error_msg = "No saved games!"
                                else:

                                    try:
                                        save_data = save_dictionary[user_input]
                                    except KeyError:
                                        error = True
                                        error_msg = "Save not found!"
                                    else:
                                        (game_width, game_height, speed, score, score2, snake_color, snake_color2,
                                         snake_direction, snake_direction2, snake_pos, snake_pos2, food_pos, wall_pos,
                                         p1_tail_pos, p2_tail_pos, food_color, max_food, food, hunger, AI, multiplayer,
                                         game_over1, game_over2) = save_data

                                        if snake_direction == "right":
                                            key_pressed = pygame.K_RIGHT
                                        elif snake_direction == "left":
                                            key_pressed = pygame.K_LEFT
                                        elif snake_direction == "up":
                                            key_pressed = pygame.K_UP
                                        elif snake_direction == "down":
                                            key_pressed = pygame.K_DOWN

                                        food_is = True
                                        no_walls = False
                                        menu = False
                                        game_choice_menu = False
                                        load_game = False
                                        error = False

                        if enter_name.is_over(mouse_pos):
                            user_input = enter_name.display_input(20)
                            enter_name_color = (80, 50, 0)

                        if delete_button.is_over(mouse_pos):
                            if user_input == "":
                                user_input = "QUICKSAVE"

                            try:
                                save_file = open("game_saves.txt", "r")
                            except FileNotFoundError:
                                error = True
                                error_msg = "No saved games!"
                            else:
                                save_dictionary = save_file.read()
                                save_file.close()

                                try:
                                    save_dictionary = ast.literal_eval(save_dictionary)
                                except Exception:
                                    error = True
                                    error_msg = "No saved games!"
                                else:

                                    try:
                                        save_dictionary.pop(user_input)
                                    except KeyError:
                                        error = True
                                        error_msg = "Save not found!"
                                    else:
                                        save_file = open("game_saves.txt", "w")
                                        save_file.write(str(save_dictionary))
                                        save_file.close()

                        if exit_button.is_over(mouse_pos):
                            load_game = False

                tbox_text = tbox_font.render(user_input, 1, black_color)
                screen.blit(tbox_text, (enter_name.x, enter_name.y))
                pygame.display.update()

            # Map creating screen
            while new_map:

                if game_width == monitor_width and game_height == monitor_height and not game_screen_set:
                    screen = pygame.display.set_mode([monitor_width, monitor_height], pygame.FULLSCREEN)
                    game_screen_set = True
                    width = 0
                    height = 0

                elif game_width < monitor_width and game_height < monitor_height and not game_screen_set:
                    screen = pygame.display.set_mode([game_width, game_height], pygame.DOUBLEBUF)
                    game_screen_set = True
                    width = 0
                    height = 0

                screen.fill(black_color)

                if [width, height] in wall_pos:
                    pygame.draw.rect(screen, (100, 0, 0), (width, height, 20, 20))
                else:
                    pygame.draw.rect(screen, (100, 100, 100), (width, height, 20, 20))

                for pos in wall_pos:
                    pygame.draw.rect(screen, wall_color, (pos[0], pos[1], 20, 20))

                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()

                    if event.type == pygame.QUIT:
                        new_map = False
                        game_screen_set = False
                        screen = pygame.display.set_mode([menu_width, menu_height])

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            new_map = False
                            game_screen_set = False
                            screen = pygame.display.set_mode([menu_width, menu_height])

                        if event.key == pygame.K_RETURN:
                            try:
                                save_file = open("saved_maps.txt", "r")
                            except Exception:
                                save_file = open("saved_maps.txt", "x")
                                save_dictionary = {}
                            else:

                                try:
                                    save_dictionary = save_file.read()
                                    save_dictionary = ast.literal_eval(save_dictionary)
                                except Exception:
                                    save_dictionary = {}

                            save_file.close()
                            save_data = game_width, game_height, wall_pos
                            count = len(save_dictionary) + 1
                            pygame.image.save(screen, "map_preview_" + str(count) + ".jpeg")
                            save_dictionary.update({count: save_data})
                            save_file = open("saved_maps.txt", "w")
                            save_file.write(str(save_dictionary))
                            save_file.close()
                            new_map = False
                            game_screen_set = False
                            screen = pygame.display.set_mode([menu_width, menu_height])

                    if event.type == pygame.MOUSEMOTION:

                        (width, height) = mouse_pos
                        width //= 20
                        height //= 20
                        width *= 20
                        height *= 20

                        if auto_draw and [width, height] not in wall_pos and not \
                                (game_width//2 - 70 < width < game_width//2 + 70 and
                                 game_height//2-30 < height < game_height//2+30):
                            wall_pos.append([width, height])

                        elif auto_delete and [width, height] in wall_pos:
                            wall_pos.pop(wall_pos.index([width, height]))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if [width, height] in wall_pos:
                            auto_delete = True
                        else:
                            auto_draw = True

                    if event.type == pygame.MOUSEBUTTONUP:
                        auto_draw = False
                        auto_delete = False

                pygame.display.update()

            # Map loading screen
            while load_map:
                screen.fill(menu_color)
                back_button = Button(exit_button_color, 0, 500, 200, 100, "Back")
                back_button.draw(screen, button_outline_color, "rectangle")
                next_button = Button(hscores_button_color, 600, 500, 200, 100, "Next")
                next_button.draw(screen, button_outline_color, "rectangle")
                prev_button = Button(hscores_button_color1, 300, 500, 200, 100, "Prev")
                prev_button.draw(screen, button_outline_color, "rectangle")

                try:
                    x = 50
                    y = 50
                    count_row = 0
                    save_file = open("saved_maps.txt", "r")
                    save_dictionary = save_file.read()
                    save_file.close()
                    save_dictionary = ast.literal_eval(save_dictionary)
                    map_count = len(save_dictionary)+1
                    page_count = (map_count-1)//6

                    if (map_count-1) % 6 != 0:
                        page_count += 1
                        last_page_count = (map_count-1) % 6

                    if last_page_count >= 1 or last_page_count == 0 or open_page < page_count:
                        pygame.draw.rect(screen, rect_color1, (40, 40, 220, 170))
                    if last_page_count >= 2 or last_page_count == 0 or open_page < page_count:
                        pygame.draw.rect(screen, rect_color2, (290, 40, 220, 170))
                    if last_page_count >= 3 or last_page_count == 0 or open_page < page_count:
                        pygame.draw.rect(screen, rect_color3, (540, 40, 220, 170))
                    if last_page_count >= 4 or last_page_count == 0 or open_page < page_count:
                        pygame.draw.rect(screen, rect_color4, (40, 240, 220, 170))
                    if last_page_count == 5 or last_page_count == 0 or open_page < page_count:
                        pygame.draw.rect(screen, rect_color5, (290, 240, 220, 170))
                    if last_page_count == 0 or open_page < page_count:
                        pygame.draw.rect(screen, rect_color6, (540, 240, 220, 170))

                    if open_page < page_count:

                        for count in range(6*open_page-5, 6*open_page+1):
                            map_preview = pygame.image.load("map_preview_" + str(count) + ".jpeg")
                            map_preview = pygame.transform.scale(map_preview, (200, 150))
                            screen.blit(map_preview, (x, y))
                            x += 250
                            count_row += 1

                            if count_row == 3:
                                count_row = 0
                                x = 50
                                y += 200
                    else:
                        if last_page_count == 0:
                            last_page_count = 6

                        for count in range(6*page_count-5, 6*page_count-5+last_page_count):
                            map_preview = pygame.image.load("map_preview_" + str(count) + ".jpeg")
                            map_preview = pygame.transform.scale(map_preview, (200, 150))
                            screen.blit(map_preview, (x, y))
                            x += 250
                            count_row += 1

                            if count_row == 3:
                                count_row = 0
                                x = 50
                                y += 200

                        if last_page_count == 6:
                            last_page_count = 0
                except Exception:
                    pass

                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()

                    if event.type == pygame.QUIT:
                        load_map = False

                    elif event.type == pygame.MOUSEMOTION:

                        if back_button.is_over(mouse_pos):
                            exit_button_color = (100, 10, 0)
                        else:
                            exit_button_color = (150, 0, 0)

                        if next_button.is_over(mouse_pos):
                            hscores_button_color = (120, 120, 0)
                        else:
                            hscores_button_color = (150, 150, 0)

                        if prev_button.is_over(mouse_pos):
                            hscores_button_color1 = (120, 120, 0)
                        else:
                            hscores_button_color1 = (150, 150, 0)

                        if 250 > mouse_pos[0] > 50 and 200 > mouse_pos[1] > 50:
                            rect_color1 = (200, 200, 200)
                        else:
                            rect_color1 = menu_color
                        if 500 > mouse_pos[0] > 300 and 200 > mouse_pos[1] > 50:
                            rect_color2 = (200, 200, 200)
                        else:
                            rect_color2 = menu_color
                        if 750 > mouse_pos[0] > 550 and 200 > mouse_pos[1] > 50:
                            rect_color3 = (200, 200, 200)
                        else:
                            rect_color3 = menu_color
                        if 250 > mouse_pos[0] > 50 and 400 > mouse_pos[1] > 250:
                            rect_color4 = (200, 200, 200)
                        else:
                            rect_color4 = menu_color
                        if 500 > mouse_pos[0] > 300 and 400 > mouse_pos[1] > 250:
                            rect_color5 = (200, 200, 200)
                        else:
                            rect_color5 = menu_color
                        if 750 > mouse_pos[0] > 550 and 400 > mouse_pos[1] > 250:
                            rect_color6 = (200, 200, 200)
                        else:
                            rect_color6 = menu_color

                    elif event.type == pygame.MOUSEBUTTONDOWN:

                        if back_button.is_over(mouse_pos):
                            load_map = False

                        if next_button.is_over(mouse_pos) and open_page < page_count:
                            open_page += 1

                        if prev_button.is_over(mouse_pos) and open_page > 1:
                            open_page -= 1

                        if 250 > mouse_pos[0] > 50 and 200 > mouse_pos[1] > 50 and \
                                (open_page < page_count or (open_page == page_count and
                                                            (last_page_count >= 1 or last_page_count == 0))):
                            save_data = save_dictionary[open_page*6-5]
                            (game_width, game_height, wall_pos) = save_data
                            game_type = "load map"
                            load_map = False
                            choose_mode = True

                        elif 500 > mouse_pos[0] > 300 and 200 > mouse_pos[1] > 50 and \
                                (open_page < page_count or (open_page == page_count and
                                                            (last_page_count >= 2 or last_page_count == 0))):
                            save_data = save_dictionary[open_page*6-4]
                            (game_width, game_height, wall_pos) = save_data
                            game_type = "load map"
                            load_map = False
                            choose_mode = True

                        elif 750 > mouse_pos[0] > 550 and 200 > mouse_pos[1] > 50 and \
                                (open_page < page_count or (open_page == page_count and
                                                            (last_page_count >= 3 or last_page_count == 0))):
                            save_data = save_dictionary[open_page*6-3]
                            (game_width, game_height, wall_pos) = save_data
                            game_type = "load map"
                            load_map = False
                            choose_mode = True

                        elif 250 > mouse_pos[0] > 50 and 400 > mouse_pos[1] > 250 and \
                                (open_page < page_count or (open_page == page_count and
                                                            (last_page_count >= 4 or last_page_count == 0))):
                            save_data = save_dictionary[open_page*6-2]
                            (game_width, game_height, wall_pos) = save_data
                            game_type = "load map"
                            load_map = False
                            choose_mode = True

                        elif 500 > mouse_pos[0] > 300 and 400 > mouse_pos[1] > 250 and \
                                (open_page < page_count or (open_page == page_count and
                                                            (last_page_count >= 5 or last_page_count == 0))):
                            save_data = save_dictionary[open_page*6-1]
                            (game_width, game_height, wall_pos) = save_data
                            game_type = "load map"
                            load_map = False
                            choose_mode = True

                        elif 750 > mouse_pos[0] > 550 and 400 > mouse_pos[1] > 250 \
                                and (open_page < page_count or (open_page == page_count and last_page_count == 0)):
                            save_data = save_dictionary[open_page*6]
                            (game_width, game_height, wall_pos) = save_data
                            game_type = "load map"
                            load_map = False
                            choose_mode = True

                pygame.display.update()

            # Opponent choosing screen
            while choose_mode:
                screen.fill(menu_color)

                back_button = Button(exit_button_color, 0, 500, 200, 100, "Back")
                singleplayer_button = Button(start_button_color, 100, 50, 600, 200, "Single player")
                twoplayer_button = Button(hscores_button_color, 100, 250, 300, 200, "2 Players")
                AI_button = Button(hscores_button_color1, 400, 250, 300, 200, "vs Computer  ")

                back_button.draw(screen, button_outline_color, shape="rectangle")
                singleplayer_button.draw(screen, button_outline_color, shape="rectangle")
                twoplayer_button.draw(screen, button_outline_color, shape="rectangle")
                AI_button.draw(screen, button_outline_color, shape="rectangle")

                hint_font = pygame.font.SysFont("monospace", 30, bold=True)
                hint_text1 = hint_font.render("P2:   W        P1:    ↑", 1, text_color)
                hint_text2 = hint_font.render("    A S D           ← ↓ →", 1, text_color)
                screen.blit(hint_text1, (250, 500))
                screen.blit(hint_text2, (250, 540))

                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()

                    if event.type == pygame.QUIT:
                        choose_mode = False

                    elif event.type == pygame.MOUSEMOTION:

                        if back_button.is_over(mouse_pos):
                            exit_button_color = (100, 10, 0)
                        else:
                            exit_button_color = (150, 0, 0)

                        if singleplayer_button.is_over(mouse_pos):
                            start_button_color = (50, 100, 0)
                        else:
                            start_button_color = (100, 150, 0)

                        if twoplayer_button.is_over(mouse_pos):
                            hscores_button_color = (120, 120, 0)
                        else:
                            hscores_button_color = (150, 150, 0)

                        if AI_button.is_over(mouse_pos):
                            hscores_button_color1 = (120, 120, 0)
                        else:
                            hscores_button_color1 = (150, 150, 0)

                    elif event.type == pygame.MOUSEBUTTONDOWN:

                        if back_button.is_over(mouse_pos):
                            choose_mode = False

                        if game_type == "new":

                            if twoplayer_button.is_over(mouse_pos):
                                multiplayer = True
                                score = 1
                                snake_pos = [game_width // 40 * 20 + 20, game_height // 40 * 20]
                                snake_color = (255, 255, 0)
                                p1_tail_pos = [snake_pos]
                                snake_color2 = (0, 255, 255)
                                snake_pos2 = [game_width // 40 * 20 - 20, game_height // 40 * 20]
                                p2_tail_pos = [snake_pos2]
                                score2 = 1
                                snake_direction2 = "left"
                                player1 = "human"
                                key_pressed2 = pygame.K_a
                                player2 = "human2"
                                key_pressed = pygame.K_RIGHT
                                snake_direction = "right"
                                food = 0
                                food_pos = []
                                no_walls = True
                                wall_pos = []
                                menu = False
                                game_choice_menu = False
                                choose_mode = False

                            if AI_button.is_over(mouse_pos):
                                AI = True
                                score = 1
                                snake_pos = [game_width // 40 * 20 + 20, game_height // 40 * 20]
                                snake_color = (255, 255, 0)
                                p1_tail_pos = [snake_pos]
                                snake_color2 = (0, 255, 255)
                                snake_pos2 = [game_width // 40 * 20 - 20, game_height // 40 * 20]
                                p2_tail_pos = [snake_pos2]
                                score2 = 1
                                snake_direction2 = "left"
                                player1 = "human"
                                key_pressed2 = "left"
                                player2 = "AI"
                                key_pressed = pygame.K_RIGHT
                                snake_direction = "right"
                                food = 0
                                food_pos = []
                                no_walls = True
                                wall_pos = []
                                hunger = 0
                                menu = False
                                game_choice_menu = False
                                choose_mode = False

                            if singleplayer_button.is_over(mouse_pos):
                                score = 1
                                snake_pos = [game_width // 40 * 20 + 20, game_height // 40 * 20]
                                snake_color = (255, 255, 0)
                                p1_tail_pos = [snake_pos]
                                snake_color2 = (0, 255, 255)
                                snake_pos2 = [None]
                                p2_tail_pos = [None]
                                score2 = None
                                snake_direction2 = None
                                player1 = "human"
                                key_pressed2 = None
                                player2 = None
                                key_pressed = pygame.K_RIGHT
                                snake_direction = "right"
                                food = 0
                                food_pos = []
                                no_walls = True
                                wall_pos = []
                                menu = False
                                game_choice_menu = False
                                choose_mode = False

                        if game_type == "load map":

                            if twoplayer_button.is_over(mouse_pos):
                                multiplayer = True
                                score = 1
                                snake_pos = [game_width // 40 * 20 + 20, game_height // 40 * 20]
                                snake_color = (255, 255, 0)
                                p1_tail_pos = [snake_pos]
                                snake_color2 = (0, 255, 255)
                                snake_pos2 = [game_width // 40 * 20 - 20, game_height // 40 * 20]
                                p2_tail_pos = [snake_pos2]
                                score2 = 1
                                snake_direction2 = "left"
                                player1 = "human"
                                key_pressed2 = pygame.K_a
                                player2 = "human2"
                                key_pressed = pygame.K_RIGHT
                                snake_direction = "right"
                                food = 0
                                food_pos = []
                                no_walls = True
                                menu = False
                                game_choice_menu = False
                                choose_mode = False

                            if AI_button.is_over(mouse_pos):
                                AI = True
                                score = 1
                                snake_pos = [game_width // 40 * 20 + 20, game_height // 40 * 20]
                                snake_color = (255, 255, 0)
                                p1_tail_pos = [snake_pos]
                                snake_color2 = (0, 255, 255)
                                snake_pos2 = [game_width // 40 * 20 - 20, game_height // 40 * 20]
                                p2_tail_pos = [snake_pos2]
                                score2 = 1
                                snake_direction2 = "left"
                                player1 = "human"
                                key_pressed2 = "left"
                                player2 = "AI"
                                key_pressed = pygame.K_RIGHT
                                snake_direction = "right"
                                food = 0
                                hunger = 0
                                food_pos = []
                                no_walls = True
                                menu = False
                                game_choice_menu = False
                                choose_mode = False

                            if singleplayer_button.is_over(mouse_pos):
                                score = 1
                                snake_pos = [game_width // 40 * 20 + 20, game_height // 40 * 20]
                                snake_color = (255, 255, 0)
                                p1_tail_pos = [snake_pos]
                                snake_color2 = (0, 255, 255)
                                snake_pos2 = [None]
                                p2_tail_pos = [None]
                                score2 = None
                                snake_direction2 = None
                                player1 = "human"
                                key_pressed2 = None
                                player2 = None
                                key_pressed = pygame.K_RIGHT
                                snake_direction = "right"
                                food = 0
                                food_pos = []
                                no_walls = True
                                menu = False
                                game_choice_menu = False
                                choose_mode = False

                pygame.display.update()

        pygame.display.update()

    # Change screen resolution from settings
    if game_width == monitor_width and game_height == monitor_height and not game_screen_set:
        screen = pygame.display.set_mode([monitor_width, monitor_height], pygame.FULLSCREEN)
        game_screen_set = True

    elif game_width < monitor_width and game_height < monitor_height and not game_screen_set:
        screen = pygame.display.set_mode([game_width, game_height], pygame.DOUBLEBUF)
        game_screen_set = True

    screen.fill(black_color)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

        # When arrow key pressed change direction
        elif event.type == pygame.KEYDOWN:

            # Check if not trying to go backwards
            if snake_direction == "right" and event.key == pygame.K_LEFT:
                pass
            elif snake_direction == "left" and event.key == pygame.K_RIGHT:
                pass
            elif snake_direction == "down" and event.key == pygame.K_UP:
                pass
            elif snake_direction == "up" and event.key == pygame.K_DOWN:
                pass
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or
                  event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                key_pressed = event.key
            elif event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_RETURN:
                save_game = True
                user_input = ""
                save_game = True
                save_data = (game_width, game_height, speed, score, score2, snake_color, snake_color2, snake_direction,
                             snake_direction2, snake_pos, snake_pos2, food_pos, wall_pos, p1_tail_pos, p2_tail_pos,
                             food_color, max_food, food, hunger, AI, multiplayer, game_over1, game_over2)

            if multiplayer:
                if snake_direction2 == "right" and event.key == pygame.K_a:
                    pass
                elif snake_direction2 == "left" and event.key == pygame.K_d:
                    pass
                elif snake_direction2 == "down" and event.key == pygame.K_w:
                    pass
                elif snake_direction2 == "up" and event.key == pygame.K_s:
                    pass
                elif (event.key == pygame.K_a or event.key == pygame.K_d or
                      event.key == pygame.K_w or event.key == pygame.K_s):
                    key_pressed2 = event.key

    if AI and key_pressed != "quit" and food > 0 and not game_over2:
        if not stuck:
            (check_pos, check_count, checking, rechecking, period, stuck) = \
                is_stuck(check_pos, check_count, checking, rechecking, period)

        try:
            AI_choice, move, stuck, hunger = AI_move(stuck, move, hunger, game_over1)
        except TypeError:
            pass

        if snake_direction2 == "right" and AI_choice == "left":
            pass
        elif snake_direction2 == "left" and AI_choice == "right":
            pass
        elif snake_direction2 == "down" and AI_choice == "up":
            pass
        elif snake_direction2 == "up" and AI_choice == "down":
            pass

        elif AI_choice == "left" or AI_choice == "right" or \
                AI_choice == "up" or AI_choice == "down":
            key_pressed2 = AI_choice
            game_over2, game_over_temp, snake_direction2 = snake_move(key_pressed2, player2)

            if not game_over1:
                game_over1 = game_over_temp

            if game_over2:
                snake_pos2 = [-40, -40]
                p2_tail_pos = [-40, -40]

    if AI and food == 0 and max_food > 1:
        game_over2, game_over_temp, snake_direction2 = snake_move(key_pressed2, player2)

    if not game_over1:
        game_over1, game_over_temp, snake_direction = snake_move(key_pressed, player1)
        if not game_over2:
            game_over2 = game_over_temp
        if game_over1:
            snake_pos = [-40, -40]
            p1_tail_pos = [-40, -40]

    if multiplayer and not game_over2:
        game_over2, game_over_temp, snake_direction2 = snake_move(key_pressed2, player2)
        if not game_over1:
            game_over1 = game_over_temp
        if game_over2:
            snake_pos2 = [-40, -40]
            p2_tail_pos = [-40, -40]

    try:
        for pos in food_pos:
            if pos[0] == snake_pos:
                (score, food, snake_color, hunger) = eat_food(player1, score, snake_color, pos, food, hunger)
            if pos[0] == snake_pos2 and (AI or multiplayer):
                (score2, food, snake_color2, hunger) = eat_food(player2, score2, snake_color2, pos, food, hunger)
    except ValueError:
        game_over1 = True
        game_over2 = True

    # Draw game objects
    draw_walls(walls)
    no_walls = False

    if not game_over1:
        draw_snake(player1)
        draw_snake_tail(player1)

    if (multiplayer or AI) and not game_over2:
        draw_snake(player2)
        draw_snake_tail(player2)

    (food_pos, food) = draw_food(food, max_food, food_pos)
    text = "Score:" + str(score - 1)
    label = score_font.render(text, 1, text_color)
    screen.blit(label, (game_width - 180, game_height - 40))

    if multiplayer or AI:
        text = "Score:" + str(score2 - 1)
        label = score_font.render(text, 1, text_color)
        screen.blit(label, (40, game_height - 40))

    pygame.display.update()

    if (game_over1 and game_over2) and (multiplayer or AI):
        game_over = True
    elif game_over1 and not (multiplayer or AI):
        game_over = True

    # Frame timer
    clock.tick(speed)
