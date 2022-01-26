import math
import random
import numpy as np

import pygame

def add_weapon_stat(self):
    """Combine weapon stat"""
    weapon_reload = 0
    base_range = []
    arrow_speed = []

    for index, weapon in enumerate([self.primary_main_weapon, self.primary_sub_weapon, self.secondary_main_weapon, self.secondary_sub_weapon]):
        if self.weapon_list.weapon_list[weapon[0]]["Range"] == 0:  # melee weapon if range 0
            self.melee_dmg[0] += self.weapon_list.weapon_list[weapon[0]]["Minimum Damage"] * \
                                 self.weapon_list.quality[weapon[1]] / (index + 1)
            self.melee_dmg[1] += self.weapon_list.weapon_list[weapon[0]]["Maximum Damage"] * \
                                 self.weapon_list.quality[weapon[1]] / (index + 1)

            self.melee_penetrate += self.weapon_list.weapon_list[weapon[0]]["Armour Penetration"] * \
                                    self.weapon_list.quality[weapon[1]] / (index + 1)
            self.weapon_speed += self.weapon_list.weapon_list[weapon[0]]["Speed"] / (index + 1)
        else:
            self.range_dmg[0] += self.weapon_list.weapon_list[weapon[0]]["Minimum Damage"] * \
                                 self.weapon_list.quality[weapon[1]]
            self.range_dmg[1] += self.weapon_list.weapon_list[weapon[0]]["Maximum Damage"] * \
                                 self.weapon_list.quality[weapon[1]]

            self.range_penetrate += self.weapon_list.weapon_list[weapon[0]]["Armour Penetration"] * \
                                    self.weapon_list.quality[weapon[1]] / (index + 1)
            self.magazine_size += self.weapon_list.weapon_list[weapon[0]][
                "Magazine"]  # can shoot how many times before have to reload
            weapon_reload += self.weapon_list.weapon_list[weapon[0]]["Speed"] * (index + 1)
            base_range.append(self.weapon_list.weapon_list[weapon[0]]["Range"] * self.weapon_list.quality[weapon[1]])
            arrow_speed.append(self.weapon_list.weapon_list[weapon[0]]["Travel Speed"])  # travel speed of range melee_attack
        self.base_melee_def += self.weapon_list.weapon_list[weapon[0]]["Defense"] / (index + 1)
        self.base_range_def += self.weapon_list.weapon_list[weapon[0]]["Defense"] / (index + 1)
        self.skill += self.weapon_list.weapon_list[weapon[0]]["Skill"]
        self.trait += self.weapon_list.weapon_list[weapon[0]]["Trait"]
        self.weight += self.weapon_list.weapon_list[weapon[0]]["Weight"]

        self.weapon_speed = int(self.weapon_speed)
        if self.melee_penetrate < 0:
            self.melee_penetrate = 0  # melee melee_penetrate cannot be lower than 0
        if self.range_penetrate < 0:
            self.range_penetrate = 0

        if base_range != []:
            self.base_range = np.mean(base_range)  # use average range
        if arrow_speed != []:
            self.arrow_speed = np.mean(arrow_speed)  # use average speed
        else:
            self.arrow_speed = 0
        self.base_reload = weapon_reload + ((50 - self.base_reload) * weapon_reload / 100)  # final reload speed from weapon and skill


def add_mount_stat(self):
    """Combine mount stat"""
    self.base_charge_def = 25  # charge defence only 25 for cav
    self.base_speed = (
            self.mount["Speed"] + self.mount_grade["Speed Bonus"])  # use mount base speed instead
    self.troop_health += (self.mount["Health Bonus"] * self.mount_grade["Health Effect"]) + \
                         self.mount_armour["Health"]  # Add mount health to the troop health
    self.base_charge += (self.mount["Charge Bonus"] +
                         self.mount_grade["Charge Bonus"])  # Add charge power of mount to troop
    self.base_morale += self.mount_grade["Morale Bonus"]
    self.base_discipline += self.mount_grade["Discipline Bonus"]
    self.stamina += self.mount["Stamina Bonus"]
    self.trait += self.mount["Trait"]  # Apply mount trait to subunit
    self.subunit_type = 2  # If subunit has a mount, count as cav for command buff
    self.feature_mod = 4  # the starting column in unit_terrainbonus of cavalry



def add_trait(self):
    """Add trait to base stat"""
    for trait in self.trait.values():  # add trait modifier to base stat
        self.base_melee_attack *= trait['Melee Attack Effect']
        self.base_melee_def *= trait['Melee Defence Effect']
        self.base_range_def *= trait['Ranged Defence Effect']
        self.base_armour += trait['Armour Bonus']
        self.base_speed *= trait['Speed Effect']
        self.base_accuracy *= trait['Accuracy Effect']
        self.base_range *= trait['Range Effect']
        self.base_reload *= trait['Reload Effect']
        self.base_charge *= trait['Charge Effect']
        self.base_charge_def += trait['Charge Defence Bonus']
        self.base_hp_regen += trait['HP Regeneration Bonus']
        self.base_stamina_regen += trait['Stamina Regeneration Bonus']
        self.base_morale += trait['Morale Bonus']
        self.base_discipline += trait['Discipline Bonus']
        self.crit_effect += trait['Critical Bonus']
        self.elem_res[0] += (trait['Fire Resistance'] / 100)  # percentage, 1 mean perfect resistance, 0 mean none
        self.elem_res[1] += (trait['Water Resistance'] / 100)
        self.elem_res[2] += (trait['Air Resistance'] / 100)
        self.elem_res[3] += (trait['Earth Resistance'] / 100)
        self.magic_res += (trait['Magic Resistance'] / 100)
        self.heat_res += (trait['Heat Resistance'] / 100)
        self.cold_res += (trait['Cold Resistance'] / 100)
        self.elem_res[4] += (trait['Poison Resistance'] / 100)
        self.mental += trait['Mental Bonus']
        if trait['Enemy Status'] != [0]:
            for effect in trait['Enemy Status']:
                self.base_inflict_status[effect] = trait['Buff Range']
        # self.base_elem_melee =
        # self.base_elem_range =

    if 3 in self.trait:  # Varied training
        self.base_melee_attack *= (random.randint(70, 120) / 100)
        self.base_melee_def *= (random.randint(70, 120) / 100)
        self.base_range_def *= (random.randint(70, 120) / 100)
        self.base_speed *= (random.randint(70, 120) / 100)
        self.base_accuracy *= (random.randint(70, 120) / 100)
        self.base_reload *= (random.randint(70, 120) / 100)
        self.base_charge *= (random.randint(70, 120) / 100)
        self.base_charge_def *= (random.randint(70, 120) / 100)
        self.base_morale += random.randint(-15, 10)
        self.base_discipline += random.randint(-20, 0)
        self.mental += random.randint(-20, 10)

    # v Change trait variable
    if 16 in self.trait:
        self.arc_shot = True  # can shoot in arc
    if 17 in self.trait:
        self.agile_aim = True  # gain bonus accuracy when shoot while moving
    if 18 in self.trait:
        self.shoot_move = True  # can shoot and move at same time
    if 29 in self.trait:
        self.ignore_charge_def = True  # ignore charge defence completely
    if 30 in self.trait:
        self.ignore_def = True  # ignore defence completely
    if 34 in self.trait:
        self.full_def = True  # full effective defence for all side
    if 33 in self.trait:
        self.backstab = True  # bonus on rear melee_attack
    if 47 in self.trait:
        self.flanker = True  # bonus on flank melee_attack
    if 55 in self.trait:
        self.oblivious = True  # more penalty on flank/rear defend
    if 73 in self.trait:
        self.no_range_penal = True  # no range penalty
    if 74 in self.trait:
        self.long_range_acc = True  # less range penalty
    if 111 in self.trait:
        self.unbreakable = True  # always unbreakable
        self.temp_unbreakable = True
    if 149 in self.trait:  # Impetuous
        self.base_auth_penalty += 0.5
    # ^ End change trait variable
# ^^ End add trait to stat


def create_sprite(self):
    # v Subunit image sprite
    image = self.unit_ui_images["ui_squad_player.png"].copy()  # Subunit block blue colour for team1 for shown in inspect ui
    if self.team == 2:
        image = self.unit_ui_images["ui_squad_enemy.png"].copy()  # red colour

    sprite_image = pygame.Surface((image.get_width() + 10, image.get_height() + 10), pygame.SRCALPHA)  # subunit sprite image
    pygame.draw.circle(sprite_image, self.unit.colour, (sprite_image.get_width() / 2, sprite_image.get_height() / 2), image.get_width() / 2)

    if self.subunit_type == 2:  # cavalry draw line on block
        pygame.draw.line(image, (0, 0, 0), (0, 0), (image.get_width(), image.get_height()), 2)
        radian = 45 * 0.0174532925  # top left
        start = (
            sprite_image.get_width() / 3 * math.cos(radian), sprite_image.get_width() / 3 * math.sin(radian))  # draw line from 45 degree in circle
        radian = 225 * 0.0174532925  # bottom right
        end = (sprite_image.get_width() * -math.cos(radian), sprite_image.get_width() * -math.sin(radian))  # draw line to 225 degree in circle
        pygame.draw.line(sprite_image, (0, 0, 0), start, end, 2)

    selected_image = pygame.Surface((image.get_width(), image.get_height()), pygame.SRCALPHA)
    pygame.draw.circle(selected_image, (255, 255, 255, 150), (image.get_width() / 2, image.get_height() / 2), image.get_width() / 2)
    pygame.draw.circle(selected_image, (0, 0, 0, 255), (image.get_width() / 2, image.get_height() / 2), image.get_width() / 2, 1)
    selected_image_original = selected_image.copy()
    selected_image_original2 = selected_image.copy()
    selected_image_rect = selected_image.get_rect(topleft=(0, 0))

    far_image = sprite_image.copy()
    pygame.draw.circle(far_image, (0, 0, 0), (far_image.get_width() / 2, far_image.get_height() / 2),
                       far_image.get_width() / 2, 4)
    far_selected_image = selected_image.copy()
    pygame.draw.circle(far_selected_image, (0, 0, 0), (far_selected_image.get_width() / 2, far_selected_image.get_height() / 2),
                       far_selected_image.get_width() / 2, 4)

    scale_width = sprite_image.get_width() * 1 / self.max_zoom
    scale_height = sprite_image.get_height() * 1 / self.max_zoom
    dim = pygame.Vector2(scale_width, scale_height)
    far_image = pygame.transform.scale(far_image, (int(dim[0]), int(dim[1])))
    far_selected_image = pygame.transform.scale(far_selected_image, (int(dim[0]), int(dim[1])))

    block = image.copy()  # image shown in inspect ui as square instead of circle
    # ^ End subunit base sprite

    # v health and stamina related
    health_image_list = [self.unit_ui_images["ui_health_circle_100.png"], self.unit_ui_images["ui_health_circle_75.png"],
                              self.unit_ui_images["ui_health_circle_50.png"], self.unit_ui_images["ui_health_circle_25.png"],
                              self.unit_ui_images["ui_health_circle_0.png"]]
    stamina_image_list = [self.unit_ui_images["ui_stamina_circle_100.png"], self.unit_ui_images["ui_stamina_circle_75.png"],
                               self.unit_ui_images["ui_stamina_circle_50.png"], self.unit_ui_images["ui_stamina_circle_25.png"],
                               self.unit_ui_images["ui_stamina_circle_0.png"]]

    health_image = self.unit_ui_images["ui_health_circle_100.png"]
    health_image_rect = health_image.get_rect(center=sprite_image.get_rect().center)  # for battle sprite
    health_block_rect = health_image.get_rect(center=block.get_rect().center)  # for ui sprite
    sprite_image.blit(health_image, health_image_rect)
    block.blit(health_image, health_block_rect)

    stamina_image = self.unit_ui_images["ui_stamina_circle_100.png"]
    stamina_image_rect = stamina_image.get_rect(center=sprite_image.get_rect().center)  # for battle sprite
    stamina_block_rect = stamina_image.get_rect(center=block.get_rect().center)  # for ui sprite
    sprite_image.blit(stamina_image, stamina_image_rect)
    block.blit(stamina_image, stamina_block_rect)
    # ^ End health and stamina

    # v weapon class icon in middle circle
    image1 = self.weapon_list.images[self.weapon_list.weapon_list[self.primary_main_weapon[0]]["ImageID"]]  # image on subunit sprite
    image1_rect = image1.get_rect(center=sprite_image.get_rect().center)
    sprite_image.blit(image1, image1_rect)

    image1_rect = image1.get_rect(center=block.get_rect().center)
    block.blit(image1, image1_rect)
    block_original = block.copy()

    corner_image_rect = self.unit_ui_images["ui_squad_combat.png"].get_rect(center=block.get_rect().center)  # red corner when take melee_dmg shown in image block
    # ^ End weapon icon

    image_original = sprite_image.copy()  # original for rotate
    image_original2 = sprite_image.copy()  # original2 for saving original not clicked
    image_original3 = sprite_image.copy()  # original3 for saving original zoom level

    return {"sprite": sprite_image, "original": image_original, "original2": image_original2, "original3": image_original3,
            "block": block, "block_original": block_original, "selected": selected_image, "selected_rect": selected_image_rect,
            "selected_original": selected_image_original, "selected_original2": selected_image_original2,
            "far": far_image, "far_selected": far_selected_image, "health_rect": health_image_rect, "health_block_rect": health_block_rect,
            "stamina_rect": stamina_image_rect, "stamina_block_rect": stamina_block_rect,
            "corner_rect": corner_image_rect, "health_list": health_image_list, "stamina_list": stamina_image_list}
