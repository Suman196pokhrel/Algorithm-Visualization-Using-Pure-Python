import pygame, sys, random

pygame.init()


class BubbleSort:
    def __init__(self, window_width, window_height, width_of_bars, speed_of_sorting):
        self.win_height = window_height
        self.win_breadth = window_width
        self.win = pygame.display.set_mode((self.win_breadth, self.win_height))
        self.title = pygame.display.set_caption('BUBBLE SORT VISUALIZER')
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (9, 73, 236)
        self.win.fill(self.black)
        self.width_single_bar = width_of_bars
        self.number_of_bars = int(self.win_breadth / self.width_single_bar)
        self.height_arr = []
        self.state_of_bars_arr = []
        self.bars_height_state = []
        self.speed_of_sorting = speed_of_sorting
        self.number_of_swappings = 0
        self.font = pygame.font.SysFont(None, 24)

        for i in range(self.number_of_bars):
            self.bars_height_state.append([random.randint(10, self.win_height), '0'])


class LinearSearch:
    def __init__(self, window_width, window_height, width_of_bars, speed_of_sorting):
        self.win_width = window_width
        self.win_height = window_height
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.width_each_bar = width_of_bars
        self.number_of_bars = int(self.win_width / self.width_each_bar)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.blue = (9, 18, 236)
        self.yellow = (230, 236, 9)
        self.fps = speed_of_sorting
        self.font = pygame.font.SysFont(None, 30)
        self.font_1 = pygame.font.SysFont(None, 20)
        self.num_items_searched = 0

        # Data Structures for Algorithm
        self.bar_height_state = []

        # state = 0 >> normal bar
        # state = 1>> bar under evaluation
        # state = 2 >> bar to be searched for
        # state = 3 >> Found the final Bar

        # Initializing The Array
        for i in range(self.number_of_bars):
            self.bar_height_state.append([random.randint(10, self.win_height), '0'])

        self.element_to_search_for = random.randint(5, len(self.bar_height_state))


def bubble_start(window_width, window_height, width_of_bars, speed_of_sorting):
    pygame.init()
    clock = pygame.time.Clock()

    mainwin = BubbleSort(window_width, window_height, width_of_bars, speed_of_sorting)
    globals()['counter'] = len(mainwin.bars_height_state)
    globals()['count'] = len(mainwin.bars_height_state)
    globals()['state'] = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            # bullet = mixer.Sound('gunsound.wav')
            # bullet.play()

            mainwin.win.fill(mainwin.black)
            if globals()['counter'] > 0:
                for j in range(0, globals()['counter'] - 1):
                    if mainwin.bars_height_state[j][0] > mainwin.bars_height_state[j + 1][0]:
                        mainwin.bars_height_state[j][1] = '1'
                        mainwin.bars_height_state[j + 1][1] = '1'
                        mainwin.bars_height_state[j], mainwin.bars_height_state[j + 1] = mainwin.bars_height_state[
                                                                                             j + 1], \
                                                                                         mainwin.bars_height_state[j]

                        mainwin.number_of_swappings += 1

                    else:
                        mainwin.bars_height_state[j][1], mainwin.bars_height_state[j + 1][1] = '0', '0'

            globals()['counter'] -= 1

            # CHecking wether the bars are in corect place or not and assigining them the state

            if globals()['counter'] >= 0:
                mainwin.bars_height_state[globals()['counter'] - globals()['count']][1] = 'final_state'

            # Assigining Colors:

            for i in range(len(mainwin.bars_height_state)):
                if mainwin.bars_height_state[i][1] == '1':
                    color = mainwin.red
                elif mainwin.bars_height_state[i][1] == '0':
                    color = mainwin.blue
                else:
                    color = mainwin.white
                # color = mainwin.white

                # pygame.draw.line(mainwin.win,color,(mainwin.win_height - mainwin.bars_height_state[1][0]),i * mainwin.width_single_bar)

                pygame.draw.rect(mainwin.win, color, pygame.Rect(int(i * mainwin.width_single_bar),
                                                                 mainwin.win_height - mainwin.bars_height_state[i][0],
                                                                 mainwin.width_single_bar,
                                                                 mainwin.bars_height_state[i][0]))

        text = mainwin.font.render(
            f'Number of Swappings :: {mainwin.number_of_swappings}\n Rendering At {mainwin.speed_of_sorting} FPS  ',
            True,
            mainwin.white)
        mainwin.win.blit(text, (mainwin.win_breadth / 50, mainwin.win_height / 30))
        clock.tick(mainwin.speed_of_sorting)
        pygame.display.update()


def linear_search_start(window_width, window_height, width_of_bars, speed_of_sorting):
    pygame.init()
    clock = pygame.time.Clock()
    color = None

    mainwin_1 = LinearSearch(window_width, window_height, width_of_bars, speed_of_sorting)
    globals()['counter'] = 0
    run = True

    while True:

        clock.tick(mainwin_1.fps)
        mainwin_1.bar_height_state[mainwin_1.element_to_search_for][1] = '2'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if globals()['counter'] <= len(mainwin_1.bar_height_state):
            mainwin_1.win.fill(mainwin_1.black)
            # Changing the initial color of the selected bars
            mainwin_1.bar_height_state[globals()['counter']][1] = '1'
            mainwin_1.num_items_searched += 1

            # CHecking the Condition

            if mainwin_1.bar_height_state[globals()['counter']] == mainwin_1.bar_height_state[
                mainwin_1.element_to_search_for]:
                mainwin_1.bar_height_state[mainwin_1.element_to_search_for][1] = '3'
                globals()['counter'] = len(mainwin_1.bar_height_state)

        # for Coloring The Bars

        globals()['counter'] += 1

        if run:

            for i in range(len(mainwin_1.bar_height_state)):
                if mainwin_1.bar_height_state[i][1] == '0':
                    color = mainwin_1.white
                elif mainwin_1.bar_height_state[i][1] == '1':
                    color = mainwin_1.red
                elif mainwin_1.bar_height_state[mainwin_1.element_to_search_for][1] == '2':
                    color = mainwin_1.yellow
                elif mainwin_1.bar_height_state[mainwin_1.element_to_search_for][1] == '3':
                    color = mainwin_1.blue
                    run = False

                pygame.draw.rect(mainwin_1.win, color, pygame.Rect(i * mainwin_1.width_each_bar,
                                                                   mainwin_1.win_height - mainwin_1.bar_height_state[i][
                                                                       0],
                                                                   mainwin_1.width_each_bar,
                                                                   mainwin_1.bar_height_state[i][0]))

        text = mainwin_1.font.render(
            f'Number of Items searched :: {mainwin_1.num_items_searched}', True, mainwin_1.white)
        mainwin_1.win.blit(text, (10, 5))

        text_1 = mainwin_1.font_1.render(
            f'Rendered at :: {mainwin_1.fps} FPS', True, mainwin_1.white)
        mainwin_1.win.blit(text_1, (10, 20))

        pygame.display.update()


class BinarySearch:

    def __init__(self, window_width, window_height, width_of_bars, speed_of_sorting):
        self.win_width = window_width
        self.win_height = window_height
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
        self.bar_width = width_of_bars
        self.number_of_bars = int(self.win_width / self.bar_width)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (9, 236, 231)
        self.purple = (236, 9, 225)
        self.bar_height_state = []
        for i in range(self.number_of_bars):
            self.bar_height_state.append([i * 1, '0'])

        self.element_to_search_for = random.randint(10, self.number_of_bars - 10)
        self.fps = speed_of_sorting

        # states of bars
        #  0 >> normal state
        # l >> left most
        # r >> right most
        # found_element >> element to search for
        # mid_element >> mid term


def binary_start(window_width, window_height, width_of_bars, speed_of_sorting):
    mainwin_3 = BinarySearch(window_width, window_height, width_of_bars, speed_of_sorting)
    globals()['state'] = True
    globals()['left'] = 0
    globals()['right'] = mainwin_3.number_of_bars - 1
    run = True
    running = True
    globals()['color'] = None
    clock = pygame.time.Clock()

    while True:
        # mainwin_3.win.fill(mainwin_3.black)
        clock.tick(mainwin_3.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if running:
            mainwin_3.bar_height_state[mainwin_3.element_to_search_for][1] = 'to_find'
            globals()['mid'] = (globals()['left'] + globals()['right']) // 2

            mainwin_3.bar_height_state[globals()['left']][1] = 'l'
            mainwin_3.bar_height_state[globals()['right']][1] = 'r'
            mainwin_3.bar_height_state[globals()['mid']][1] = 'm'

            if mainwin_3.bar_height_state[mainwin_3.element_to_search_for][0] == \
                    mainwin_3.bar_height_state[globals()['mid']][0]:
                mainwin_3.bar_height_state[mainwin_3.element_to_search_for][1] = 'f'


            elif mainwin_3.bar_height_state[mainwin_3.element_to_search_for][0] > \
                    mainwin_3.bar_height_state[globals()['mid']][0]:
                # for i in range(globals()['left']):
                #     mainwin_3.bar_height_state[i][1] = 'l'
                # for i in range(globals()['right'] , mainwin_3.number_of_bars - globals()['right']):
                #     mainwin_3.bar_height_state[i][1] = 'r'

                globals()['left'] = globals()['mid'] + 1


            elif mainwin_3.bar_height_state[mainwin_3.element_to_search_for][0] < \
                    mainwin_3.bar_height_state[globals()['mid']][0]:
                # for i in range(globals()['left']):
                #     mainwin_3.bar_height_state[i][1] = 'l'
                # for i in range(globals()['right'] , mainwin_3.number_of_bars - globals()['right']):
                #     mainwin_3.bar_height_state[i][1] = 'r'
                globals()['right'] = globals()['mid'] - 1

        if run:
            mainwin_3.win.fill(mainwin_3.black)
            for i in range(mainwin_3.number_of_bars):
                if mainwin_3.bar_height_state[i][1] == 'l':
                    globals()['color'] = mainwin_3.red
                if mainwin_3.bar_height_state[i][1] == 'r':
                    globals()['color'] = mainwin_3.blue
                # if mainwin_3.bar_height_state[i][1] == 'mid_element' and not(mainwin_3.bar_height_state[i][1] == 'found_element'):
                #     globals()['color'] = mainwin_3.blue
                if mainwin_3.bar_height_state[i][1] == '0':
                    globals()['color'] = mainwin_3.white
                if mainwin_3.bar_height_state[i][1] == 'f':
                    globals()['color'] = (236, 9, 225)
                if mainwin_3.bar_height_state[i][1] == 'to_find':
                    globals()['color'] = mainwin_3.black

                pygame.draw.rect(mainwin_3.win, globals()['color'], pygame.Rect(i * mainwin_3.bar_width,
                                                                                mainwin_3.win_height -
                                                                                mainwin_3.bar_height_state[i][0],
                                                                                mainwin_3.bar_width,
                                                                                mainwin_3.bar_height_state[i][0]))

        pygame.display.update()
