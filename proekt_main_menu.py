import sys

import cv2
import pygame

from button import Buttons

pygame.init()

WIDTH, HEIGHT = 864, 576
VOLUME = 0.5  # нужно будет создать базу данных и в дальнейшем брать данные из неё, чтобы при повторном входе не менять настройки
SOUND_MAIN = pygame.mixer.Sound('sounds/mainwindow_sound.mp3')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maim menu')


def text_create(text, size, x, y, color='white'):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def main_menu():
    start_btn = Buttons(15, 150, 252, 74, 'Играть', 'images/btn_main_window1.jpg', 'images/btn_main_window2.jpg',
                        'sounds/btn_sound.mp3')
    settings_btn = Buttons(15, 250, 252, 74, 'Настройки', 'images/btn_main_window1.jpg', 'images/btn_main_window2.jpg',
                           'sounds/btn_sound.mp3')
    exit_btn = Buttons(15, 350, 252, 74, 'Выйти', 'images/btn_main_window1.jpg', 'images/btn_main_window2.jpg',
                       'sounds/btn_sound.mp3')

    running = True
    # sound1 = pygame.mixer.Sound('sound/mainwindow_sound.mp3')
    SOUND_MAIN.play(-1)

    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(pygame.image.load('images/image_mainwindow.jpg'), (864, 576)), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()  #

            if event.type == pygame.USEREVENT and event.button == settings_btn:
                print(0)
                setting_menu()

            if event.type == pygame.USEREVENT and event.button == exit_btn:
                running = False
                pygame.quit()
                sys.exit()  #

            if event.type == pygame.USEREVENT and event.button == start_btn:
                SOUND_MAIN.stop()
                pygame.mixer.Sound('sounds/sound_loading.mp3').play()
                video = cv2.VideoCapture("video/video_downloads.mp4")
                success, video_image = video.read()
                fps = video.get(cv2.CAP_PROP_FPS)

                window = pygame.display.set_mode((864, 576))
                clock = pygame.time.Clock()

                run = success
                while run:
                    clock.tick(fps)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False

                    success, video_image = video.read()
                    # video_image_2 = video_image, (840, 523))
                    if success:
                        video_surf = pygame.transform.scale(pygame.image.frombuffer(
                            video_image.tobytes(), video_image.shape[1::-1], "BGR"), (864, 576))
                    else:
                        run = False
                    window.blit(video_surf, (0, 0))
                    pygame.display.flip()

                pygame.quit()

            for btn in [start_btn, settings_btn, exit_btn]:  #
                btn.handle_event(event)
        for btn in [start_btn, settings_btn, exit_btn]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        pygame.display.flip()


def setting_menu():
    exit_btn = Buttons(15, 350, 252, 74, 'Выйти', 'images/btn_main_window1.jpg', 'images/btn_main_window2.jpg',
                       'sounds/btn_sound.mp3')

    exit_bthn = Buttons(500, 350, 252, 252, 'Выйти', 'images/btn_plus.jpg', 'images/btn_main_window2.jpg',
                        'sounds/btn_sound.mp3')

    running = True
    # sound1 = pygame.mixer.Sound('test_sound.mp3')
    # sound1.play()
    while running:
        screen.fill((0, 0, 0))
        # sound1.set_volume(F)
        screen.blit(pygame.image.load('images/image_settings.jpg'), (0, 0))
        text_create('НАСТРОЙКИ', 55, WIDTH / 2, 100)
        text_create('Звук', 40, WIDTH / 9, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()  #

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == exit_btn:
                # fade()
                running = False

            if event.type == pygame.USEREVENT and event.button == exit_bthn:
                SOUND_MAIN.set_volume(0.5)

            for btn in [exit_btn, exit_bthn]:  #
                btn.handle_event(event)
        for btn in [exit_btn, exit_bthn]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)
        pygame.display.flip()


def fade():
    running = True
    fade_alpha = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))
        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False


if __name__ == '__main__':
    main_menu()
