class PlayerState:
	FALL_STATE = 0
	IDLE_STATE = 1
	WALK_STATE = 2
	START_ROLL_STATE = 18
	ROLLWALL_STATE = 6
	ROLL_STATE = 3
	JUMP_STATE = 4
	LAND_STATE = 5
	START_GRAPLEDGE_STATE = 7
	GRAPLEDGE_STATE = 8
	CLIMBLEDGE_STATE = 9
	WAITBLOC_STATE = 10
	PUSHBLOCK_STATE = 11
	WAITLADDER_STATE = 12
	CLIMBUPLADDER_STATE = 13
	CLIMBDOWNLADDER_STATE = 14
	CLIMB_TO_GROUND_LADDER_STATE = 15
	WAIT_SWIM_STATE = 16
	FORWARD_SWIM_STATE = 17
	RUN_STATE = 18
	BEGIN_GRAPLEDGE_TO_GROUND_STATE = 19
	PATH_FOLLOW_STATE = 20
	LEVEL_GAP_STATE = 21
	LEVEL_GAP_UP_STATE = 22
	FIRST_LOOK_VIEW_STATE = 23
	PATH_FOLLOW_LEVEL_STATE = 24
	OPEN_DOOR_STATE = 25
	# starff
	IDLE_TARGET_STATE = 30
	STRAFE_STATE = 31
	LEFT_STRAFE_ROLL_STATE = 32
	RIGHT_STRAFE_ROLL_STATE = 33
	# Throw
	PICK_OBJECT_STATE = 40
	THROW_OBJECT_STATE = 41
	# interaction
	DIALOGUE_INTERACTION_STATE = 50
	# Sword Attack
	BASIC_SWORD_ATTACK_1 = 60
	BASIC_SWORD_ATTACK_2 = 61
	BASIC_SWORD_ATTACK_3 = 62
	# Etat secondaire
	GET_ARMED_STATE = 100