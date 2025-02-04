import pygame


def player_input(self, cursor_pos, mouse_left_up=False, mouse_right_up=False, mouse_left_down=False,
                 mouse_right_down=False, double_mouse_right=False, target=None, key_state=None):
    """other_command is special type of command such as stop all action, raise flag, decimation, duel and so on"""
    if self.state not in (99, 100):
        self.rotate_only = False
        self.forced_melee = False
        self.attack_place = False

        new_pos = pygame.Vector2(self.leader_subunit.base_pos)
        if not self.leader_subunit.current_action:
            self.leader_subunit.new_angle = self.leader_subunit.set_rotate(cursor_pos)

        if key_state is not None:
            if self.input_delay == 0:  # for input that need to have time delay to work properly
                if key_state[pygame.K_DOWN]:
                    self.reposition_leader("down")
                elif key_state[pygame.K_UP]:
                    self.reposition_leader("up")
                elif key_state[pygame.K_LEFT]:
                    self.reposition_leader("left")
                elif key_state[pygame.K_RIGHT]:
                    self.reposition_leader("right")
                elif key_state[pygame.K_1]:  # Use troop weapon skill 1
                    self.issue_order(cursor_pos, other_command="Troop Weapon Skill 0")
                elif key_state[pygame.K_2]:  # Use troop weapon skill 2
                    self.issue_order(cursor_pos, other_command="Troop Weapon Skill 1")
                elif key_state[pygame.K_e]:  # Use leader weapon skill 1
                    self.leader_subunit.command_action = ("Leader Weapon Skill 0",)
                elif key_state[pygame.K_r]:  # Use leader weapon skill 2
                    self.leader_subunit.command_action = ("Leader Weapon Skill 1",)

            speed = self.walk_speed / 10
            if key_state[pygame.K_LSHIFT]:
                speed = self.run_speed / 10
            if key_state[pygame.K_SPACE]:
                self.rotate_only = True

            if key_state[pygame.K_s]:  # move down
                new_pos[1] += speed

            elif key_state[pygame.K_w]:  # move up
                new_pos[1] -= speed

            if key_state[pygame.K_a]:  # move left
                new_pos[0] -= speed

            elif key_state[pygame.K_d]:  # move right
                new_pos[0] += speed

        if mouse_left_up:
            self.leader_subunit.command_action = ("Action 0",)
            if "Main" in self.leader_subunit.current_action and "Charge" in self.leader_subunit.current_action:
                self.issue_order(new_pos, run_command=key_state[pygame.K_LSHIFT], revert_move=True,
                                 other_command="Action 0")

        elif mouse_right_up:
            self.leader_subunit.command_action = ("Action 1",)
            if "Sub" in self.leader_subunit.current_action and "Charge" in self.leader_subunit.current_action:
                self.issue_order(new_pos, run_command=key_state[pygame.K_LSHIFT], revert_move=True,
                                 other_command="Action 1")

        elif new_pos != self.leader_subunit.base_pos:
            self.leader_subunit.command_target = new_pos
            self.leader_subunit.new_angle = self.leader_subunit.set_rotate(new_pos)
            if mouse_left_down:
                if self.leader_subunit.equipped_weapon in self.leader_subunit.ammo_now and \
                        0 in self.leader_subunit.ammo_now[self.equipped_weapon] and \
                        self.leader_subunit.special_effect_check("Shoot While Moving"):  # range weapon
                    self.leader_subunit.command_action = ("Action 0",)
                    self.issue_order(new_pos, run_command=key_state[pygame.K_LSHIFT], revert_move=True)
                elif key_state[pygame.K_LSHIFT]:  # melee weapon charge
                    self.issue_order(new_pos, run_command=key_state[pygame.K_LSHIFT], revert_move=True,
                                     other_command="Charge Skill 0")
            elif mouse_right_down:
                if self.leader_subunit.equipped_weapon in self.leader_subunit.ammo_now and \
                        1 in self.leader_subunit.ammo_now[self.equipped_weapon] and \
                        self.leader_subunit.special_effect_check("Shoot While Moving"):  # range weapon
                    self.leader_subunit.command_action = ("Action 1",)
                    self.issue_order(new_pos, run_command=key_state[pygame.K_LSHIFT], revert_move=True)
                elif key_state[pygame.K_LSHIFT]:  # melee weapon charge
                    self.issue_order(new_pos, run_command=key_state[pygame.K_LSHIFT], revert_move=True,
                                     other_command="Charge Skill 1")
            else:
                self.issue_order(new_pos, run_command=key_state[pygame.K_LSHIFT], revert_move=True)

        elif self.rotate_only:
            self.issue_order(cursor_pos, run_command=key_state[pygame.K_LSHIFT])
        # else:  # no new movement register other command
