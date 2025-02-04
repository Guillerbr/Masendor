from gamescript import menu
from gamescript.common import utility

load_image = utility.load_image
load_images = utility.load_images
make_bar_list = utility.make_bar_list


def make_option_menu(main_dir, screen_scale, screen_rect, screen_width, screen_height, image_list, mixer_volume,
                     updater):
    # v Create option menu button and icon
    back_button = menu.MenuButton(screen_scale, image_list, (screen_rect.width / 2, screen_rect.height / 1.2),
                                  updater, text="BACK")
    default_button = menu.MenuButton(screen_scale, image_list, (screen_rect.width / 1.5, screen_rect.height / 1.2),
                                     updater, text="Default")

    # Resolution changing bar that fold out the list when clicked
    image = load_image(main_dir, screen_scale, "drop_normal.jpg", "ui\\mainmenu_ui")
    image2 = image
    image3 = load_image(main_dir, screen_scale, "drop_click.jpg", "ui\\mainmenu_ui")
    image_list = [image, image2, image3]
    resolution_drop = menu.MenuButton(screen_scale, image_list, (screen_rect.width / 2, screen_rect.height / 2.3),
                                      updater, text=str(screen_width) + " x " + str(screen_height), size=30)
    resolution_list = ("2560 x 1440", "2048 x 1080", "1920 x 1080",
                       "1600 x 900", "1366 x 768", "1280 x 720", "1024 x 768")
    resolution_bar = make_bar_list(main_dir, screen_scale, resolution_list, resolution_drop, updater)
    image = load_image(main_dir, screen_scale, "resolution_icon.png", "ui\\mainmenu_ui")
    resolution_icon = menu.MenuIcon(image,
                                    (resolution_drop.pos[0] - (resolution_drop.pos[0] / 4.5), resolution_drop.pos[1]))
    # End resolution

    # Volume change scroll bar
    esc_menu_images = load_images(main_dir, screen_scale, ["ui", "battlemenu_ui", "slider"], load_order=False)
    volume_slider = menu.SliderMenu([esc_menu_images["scroller_box"], esc_menu_images["scroller"]],
                                    [esc_menu_images["scroll_button_normal"], esc_menu_images["scroll_button_click"]],
                                    (screen_rect.width / 2, screen_rect.height / 3), mixer_volume)
    value_box = [
        menu.ValueBox(esc_menu_images["value"], (volume_slider.rect.topright[0] * 1.1, volume_slider.rect.topright[1]),
                      mixer_volume)]

    image = load_image(main_dir, screen_scale, "volume_icon.png", "ui\\mainmenu_ui")
    volume_icon = menu.MenuIcon(image, (volume_slider.pos[0] - (volume_slider.pos[0] / 4.5), volume_slider.pos[1]))

    return {"back_button": back_button, "default_button": default_button, "resolution_drop": resolution_drop,
            "resolution_bar": resolution_bar, "resolution_icon": resolution_icon, "volume_slider": volume_slider,
            "value_box": value_box, "volume_icon": volume_icon}
