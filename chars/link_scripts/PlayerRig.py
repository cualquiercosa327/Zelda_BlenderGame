from bge import logic, types
from link_scripts.PlayerConstants import ArmAnimation, FlipX

PLAY = logic.KX_ACTION_MODE_PLAY
LOOP = logic.KX_ACTION_MODE_LOOP

class PlayerRig(types.BL_ArmatureObject):

	def __init__(self, own):
		self.armAnimation = 0
		self.pickAnimation = -1

	def getSpeedFromJoyAxis(self, player):
		if ( player.gamepad.joystickConnected() ):
			speed = player.gamepad.getJoyAxis1Value()
		else:
			speed = 1.0
		return speed

	def setArmAnimation(self, value):
		self.armAnimation = value
	# -------------------------------------------------------------------------------#
	# * LAYER ANIMATION MANAGEMENT (KEEP)
	# -------------------------------------------------------------------------------#
	def keepLayer0(self):
		self.stopAction(1)
		self.stopAction(2)
		self.stopAction(3)
		self.stopAction(4)
		self.stopAction(5)

	def keepLayer1(self):
		self.stopAction(0)
		self.stopAction(2)
		self.stopAction(3)
		self.stopAction(4)
		self.stopAction(5)

	def keepLayer2(self):
		self.stopAction(0)
		self.stopAction(1)
		self.stopAction(3)
		self.stopAction(4)
		self.stopAction(5)

	def keepLayer3(self):
		self.stopAction(0)
		self.stopAction(1)
		self.stopAction(2)
		self.stopAction(4)
		self.stopAction(5)

	def keepLayer4(self):
		self.stopAction(0)
		self.stopAction(1)
		self.stopAction(2)
		self.stopAction(3)
		self.stopAction(5)

	def keepLayer5(self):
		self.stopAction(0)
		self.stopAction(1)
		self.stopAction(2)
		self.stopAction(3)
		self.stopAction(4)

	def stopArmLayer(self):
		self.stopAction(7)
	# -------------------------------------------------------------------------------#
	# * LAYER ZERO (ZERO)
	# -------------------------------------------------------------------------------#
	def playFallDown(self):
		""" Play fall down animation of link
		"""
		self.keepLayer0()

		self.playAction(
		'link_jump', 40, 40,
		0, 1,
		5, LOOP)

	def playJump(self):
		""" Play jump animation of link
		"""
		self.keepLayer0()

		self.playAction(
		'link_jump', 1, 12,
		0, 0,
		2, PLAY)

	def playJumpSalto(self):
		""" Play jump animation of link
		"""
		self.keepLayer0()

		self.playAction(
		'link_jump', 1, 22,
		0, 0,
		2, PLAY)

	# -------------------------------------------------------------------------------#
	# * LAYER ONE (1)
	# -------------------------------------------------------------------------------#
	def playBasePose(self):
		""" Play wait animation of link
		"""
		self.keepLayer1()

		self.playAction(
		'link_idle1', 1, 1,
		1, 0,
		0, PLAY)

	def playWait(self):
		""" Play wait animation of link
		"""
		self.keepLayer1()

		self.playAction(
		'link_idle1', 1, 59,
		1, 1,
		5, LOOP)

	def playHeavyWait(self):
		""" Play wait animation of link
		"""
		self.keepLayer1()

		self.playAction(
		'link_idle1', 70, 119,
		1, 1,
		5, LOOP)

	def playWalk(self, speed=1.0):
		""" Play walk animation of link
		"""
		self.keepLayer1()

		self.playAction(
		'link_walk', 1, 20,
		1, 1,
		5, LOOP, 0.0, 0, speed)

	def playRun(self):
		""" Play run animation of link
		"""
		self.keepLayer1()
		# Play down animation
		self.playAction(
		'link_run', 1, 14,
		1, 1,
		4, LOOP)
		# Play arm animation
		arm = self.armAnimation
		if (arm == ArmAnimation.ARMED):
			self.playAction(
			'link_run_arm', 21, 34,
			7, 0,
			4, LOOP)
		elif (self.pickAnimation == 0):
			# play ge tstick aniumation
			self.playPickStick()
		else:
			self.playAction(
			'link_run_arm', 1, 14,
			7, 0,
			4, LOOP)

	def playRoll(self):
		""" Play roll animation of link
		"""
		self.keepLayer1()

		self.playAction(
		'link_roll', 1, 11,
		1, 1,
		0, PLAY)

	def playRollWall(self):
		""" Play roll wall animation of link, is the collision to wall when lin roll
		"""
		self.keepLayer1()

		self.playAction(
		'link_roll', 15, 30,
		1, 1,
		1, PLAY)

	def playLowLand(self):
		""" Play low land animation, after little jump or fall
		"""
		self.keepLayer1()

		self.playAction(
		'link_falling_down', 44, 48,
		1, 1,
		3, PLAY)

	# -------------------------------------------------------------------------------#
	# * LAYER TWO (2) - Ladder (Echelle) animation
	# -------------------------------------------------------------------------------#
	def playLadderWait(self):
		""" Play ladder wait animation of link
		"""
		self.keepLayer2()

		self.playAction(
		'link_climb_ladder', 1, 1,
		2, 0,
		1, LOOP)

	def playSetLadderFromTop(self):
		""" Play ladder set from top
		"""
		self.keepLayer2()

		self.playAction(
		'link_climb_ladder', 39, 58,
		2, 0,
		0, PLAY)

	def playLadderClimbUp(self):
		""" Play climb to down ladder animation of link
		"""
		self.keepLayer2()

		self.playAction(
		'link_climb_ladder', 1, 17,
		2, 0,
		1, PLAY)

	def playLadderClimbDown(self):
		""" Play climb to up ladder animation of link
		"""
		self.keepLayer2()

		self.playAction(
		'link_climb_ladder', 17, 1,
		2, 0,
		1, PLAY)

	def playLadderClimbToGround(self):
		""" Play climb to ground from ladder animation of link
		"""
		self.keepLayer2()

		self.playAction(
		'link_climb_ladder', 17, 39,
		2, 0,
		1, PLAY)

	# -------------------------------------------------------------------------------#
	# * LAYER THREE (3) - LEDGE ANIMATION
	# -------------------------------------------------------------------------------#
	def playStartGrapLedge(self):
		""" Play grap ledge animation of link
		"""
		self.keepLayer3()

		self.playAction(
		'link_climb_wall', 1, 20,
		3, 0,
		2, PLAY)

	def playGrapLedge(self):
		""" Play grap ledge animation of link
		"""
		self.keepLayer3()

		self.playAction(
		'link_climb_wall', 20, 20,
		3, 0,
		0, LOOP)

	def playGoToWaitLedge(self):
		""" Play grap ledge animation of link
		"""
		self.keepLayer3()

		self.playAction(
		'link_climb_wall', 21, 33,
		3, 0,
		1, PLAY)

	def playEdgeWait(self):
		""" Play push bloc animation of link
		"""
		self.keepLayer3()

		self.playAction(
		'link_climb_wall', 33, 33,
		3, 0,
		0, LOOP)

	def playClimbLedge(self):
		""" Play climb to ground from ledge animation of link
		"""
		self.keepLayer3()

		self.playAction(
		'link_climb_wall', 34, 74,
		3, 0,
		0, PLAY)

	# -------------------------------------------------------------------------------#
	# * LAYER THREE (4) - Bloc ANIMATION
	# -------------------------------------------------------------------------------#
	def playWaitPush(self):
		""" Play push bloc animation of link
		"""
		self.keepLayer4()

		self.playAction(
		'link_push', 1, 2,
		4, 0,
		0, PLAY)

	def playWalkPush(self):
		""" Play push bloc animation of link
		"""
		self.keepLayer4()

		self.playAction(
		'link_push', 1, 41,
		4, 0,
		0, PLAY)

	# -------------------------------------------------------------------------------#
	# * LAYER THREE (5) - Swim ANIMATION
	# -------------------------------------------------------------------------------#
	def playOpenSmallChest(self):
		""" Play push bloc animation of link
		"""
		self.keepLayer5()

		self.playAction(
		'link_open_small_chest', 1, 40,
		5, 1,
		0, PLAY)

	def playOpenBigChest(self):
		""" Play push bloc animation of link
		"""
		self.keepLayer5()

		self.playAction(
		'link_find_treasure', 1, 170,
		5, 1,
		0, PLAY)

	def playSwimIdle(self):
		""" Play push bloc animation of link
		"""
		self.keepLayer5()

		self.playAction(
		'link_swimming', 1, 48,
		5, 1,
		2, LOOP)

	def playSwimForward(self):
		""" Play push bloc animation of link
		"""
		self.keepLayer5()

		self.playAction(
		'link_swimming', 50, 60,
		5, 1,
		2, LOOP)

	def playOpenDoor(self):
		""" Play push bloc animation of link
		"""
		self.keepLayer5()

		self.playAction(
		'link_door', 1, 48,
		5, 1,
		2, PLAY)

	# * Target Mode
	def playTargetIdle(self):
		""" Play target idle animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_target_idle', 0, 19,
		5, 1,
		2, LOOP)

	def playObjectTargetIdle(self):
		""" Play target idle animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_target_object', 0, 0,
		5, 1,
		0, LOOP)

	def playTargetFallBackJump(self):
		""" Play target idle animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_target_jump', 1, 11,
		5, 1,
		2, PLAY)

	def playTargetBounceBackJump(self):
		""" Play target idle animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_target_jump', 12, 16,
		5, 1,
		1, PLAY)

	def playStrafeWard(self, flip=FlipX.RIGHT):
		""" Play strafe movement
		"""
		self.keepLayer5()

		# Set frames by flip
		frame = [115, 125]
		if (flip == FlipX.LEFT):
			frame = [100, 110]

		self.playAction(
		'link_target_move', frame[0], frame[1],
		5, 1,
		2, LOOP)

	def playStrafeRoll(self, flip=FlipX.RIGHT):
		""" Play strafe movement
		"""
		self.keepLayer5()

		# Set frames by flip
		frame = [45, 66]
		if (flip == FlipX.LEFT):
			frame = [70, 91]

		self.playAction(
		'link_target_move', frame[0], frame[1],
		5, 1,
		2, PLAY)

	def playStrafeJump(self):
		""" Play strafe movement
		"""
		self.keepLayer5()

		self.playAction(
		'link_straff', 2, 12,
		5, 1,
		2, PLAY)

	# Attack
	def playBasicSwordAttack1(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_attack', 0, 13,
		5, 1,
		2, PLAY)

	def playBasicSwordAttack2(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_attack', 14, 35,
		5, 1,
		2, PLAY)

	def playBasicSwordAttack3(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_attack', 36, 58,
		5, 1,
		1, PLAY)

	def playBeginJumpAttack(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_attack', 61, 74,
		5, 1,
		2, PLAY)

	def playBounceJumpAttack(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_attack', 79, 89,
		5, 1,
		0, PLAY)

	def playClangSword(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_attack', 97, 110,
		5, 1,
		2, PLAY)

	# Specials Attacks
	def playSpecialAttack1(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_dodge_attack', 0, 17,
		5, 1,
		2, PLAY)

	def playWaitSpinSwordAttack(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_attack', 115, 115,
		5, 1,
		5, LOOP)

	def playSpinSwordAttack(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_attack', 115, 130,
		5, 1,
		0, PLAY)

	# -------------------------------------------------------------------------------#
	# * HIT ANIMATIOS
	# -------------------------------------------------------------------------------#
	def playGroundDeath(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_death', 0, 59,
		5, 0,
		0, PLAY)

	def playHitUpercut(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_hit', 0, 7,
		5, 1,
		0, PLAY)

	def playHitBounce(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_hit', 7, 32,
		5,1,
		0, PLAY)

	def playBounceStandUp(self):
		""" Play basic sword Attack animation
		"""
		self.keepLayer5()

		self.playAction(
		'link_hit', 32, 46,
		5, 1,
		0, PLAY)

	# -------------------------------------------------------------------------------#
	# * LAYER TEN (10) * FOR ARMED ANIMATION
	# -------------------------------------------------------------------------------#
	def playPick(self):
		""" Play wait animation when link is armed
		"""

		self.playAction(
		'link_pickthrow', 1, 1,
		7, 0,
		1, LOOP)

	def playPickStick(self):
		""" Play wait animation when link is armed
		"""

		self.playAction(
		'link_pick_arm', 0, 0,
		7, 0,
		0, LOOP)

	def playThrow(self):
		""" Play wait animation when link is armed
		"""

		self.playAction(
		'link_pickthrow', 1, 6,
		7, 0,
		1, PLAY)

	def playWaitArmed(self):
		""" Play wait animation when link is armed
		"""

		self.playAction(
		'link_armed', 1, 274,
		7, 0,
		1, LOOP)

	def playGetArmed(self):
		""" Play get armed animation of link
		"""

		self.playAction(
		'link_armed', 281, 286,
		7, 0,
		1, PLAY)

	# * Bow animtion
	def playWaitBow(self):
		""" Play bow animation of link
		"""
		self.playAction(
		'link_bow', 1, 10,
		7, 0,
		1, LOOP)
