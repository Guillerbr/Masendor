Subunit action

There are 2 files for action system in arcade mode: 

- char for animation that use general weapon type

the file need to be in this structure:
action name, gear/equipment related to the action, animation name to play, list of propoerties 

equipment for list of action that each weapon can perform and based animation name. The animation 
the file need to be in this structure:
ID, Name (weapon), Action (animation name that needed to be in animation data, the system will search and match using race, mount, hand, and weapon type in the subunit object in game.), Properties


List of action properties:
"movable": animation can be performed when moving and moving can be initiate during animation
"uninterruptible": animation can not be interupt by anything else (normally can be interupted like when take damage)
"cancelable": can be cancel with other animation input beside forced animation
"invincible": can not be damaged during animation
"revert": run animation in revert frame
"hold": weapon action can hold at the frame with "hold" property 
"holdfront": weapon do damage during hold like spearwall and pikewall
"power": hold start power charging
"timing_": add release timing mechanic for hold (can work with power and block) that improve accuracy, require count time number and release time window (e.g., timing_1.5_2 for start perfect timing 1.5 second after hold and last for 2 seconds) 
"block": use full defence from the weapon and deal no damage when hold
"parry": animation count as blocking and attack with bonus during if got hit by attack
"aoe": effect deal further aoe damage outside of sprite effect in distance, need distance number after "aoe" (e.g.,aoe10)
"externaleffect": effect use its own external animation frame instead of the frame assigned in animation sprite, accept only the first frame for starting the effect animation 
"duration": effect remain in loop for duration, need duration number in second after "duration" (e.g.,duration60)
"nodmg": effect deal no dmg and will not check in code
"dmgsprite": whole sprite can cause damage instead of a single point
"skip_": skip specific frames from playing use same indexing as list (e.g.skip_0_4_8 for skiping first, fourth, and eight frame)
"p(number)_fix_main_weapon" or "p(number)_fix_sub_weapon": Use center point instead weapon joint positon and place them at the specified position instead of automatically at user's hand (main = right hand, sub = left hand)
"afterimage": play faded previous frame image along with the current frame 