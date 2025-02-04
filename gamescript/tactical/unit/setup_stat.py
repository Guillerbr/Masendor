def setup_stat(self, battle_start=False):
    """Grab stat from all subunit in the unit"""
    self.troop_number = 0
    self.stamina = 0
    self.morale = 0
    all_speed = []  # list of subunit speed, use to get the slowest one
    self.ammo = 0
    how_many = 0
    all_shoot_range = []  # list of shoot range, use to get the shortest and longest one

    # v Grab subunit stat
    not_broken = False
    # if self.zoom == 1:  # closest zoom

    # for checking row order and adjusting layer to show subunit closest to bottom of the screen first
    pos_dict = {sprite: sprite.base_pos for sprite in self.subunit_list}
    pos_dict = dict(sorted(pos_dict.items(), key=lambda x: x[1][1]))

    for index, subunit in enumerate(pos_dict.keys()):
        if subunit.state != 100:  # only get stat from alive subunit
            if self.zoom == 1:
                self.battle_camera.change_layer(subunit, index + 4)
            self.troop_number += subunit.troop_number
            self.stamina += subunit.stamina
            self.morale += subunit.morale
            all_speed.append(subunit.speed)
            if subunit.magazine_count[0][0] > 0:
                self.ammo += subunit.magazine_count[0][0]
                all_shoot_range.append(subunit.shoot_range[0])
            subunit.skill_cond = self.skill_cond
            how_many += 1
            if subunit.state != 99:  # check if unit completely broken
                not_broken = True
    self.troop_number = int(self.troop_number)  # convert to int to prevent float decimal

    if not_broken is False:
        self.state = 99  # completely broken
        self.can_split_row = False  # can not split unit
        self.can_split_col = False

    self.cal_unit_stat(how_many, all_speed, all_shoot_range,
                       battle_start)  # calculate stat for unit related calculation
