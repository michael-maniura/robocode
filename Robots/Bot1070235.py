#! /usr/bin/python
# -*- coding: utf-8 -*-
from AI.actions import Action
from AI.state import State

from Objects.robot import Robot  # Import a base Robot
import random
import math

class Bot1070235(Robot):  # Create a Robot

    def init(self):  # To initialize your robot

        # Feel free to customize: Set the bot color in RGB
        self.setColor(39, 93, 115)
        self.setGunColor(86, 191, 232)
        self.setRadarColor(46, 112, 28)
        self.setBulletsColor(166, 31, 204)
        self.maxDepth = 5

        #Don't Change
        self.setRadarField("thin")
        self.radarVisible(True)  # if True the radar field is visible
        self.gun_to_side()
        self.lockRadar("gun")
        size = self.getMapSize()


    def run(self):  # main loop to command the bot
        """
        to create your own bot, create an new python-file in python package "Robots" and give it a name
        copy the code of simplebot and rename the class
        starting the main.py starts the game

        use this method to control the bot
        1. information from your sensors:
            - get your position: self.getPosition()
            - get enemies position: self.getPosition_enemy()
            - get left energy (max 100): self.energy_left_self()
            - get left energy of enemy: self.energy_left_enemy()
            - return true if a shot would hit the enemy: self.shot_possible_by_enemy()
            - return true if a shot by the enemy would hit you: self.shot_possible_at_enemy()
            - return the angle of your gun (looking down (0,1) equals an angle of 0: self.getGunHeading()
            - return the angle of your enemies gun (looking down (0,1) equals an angle of 0: self.getGunHeading_enemy()+
            - returns the map size (left upper corner is (0,0):  self.getMapSize
        2. possible actions
            - turns 45° to the right: self.turn_right()
            - turns 45° to the left: self.turn_left()
            - move 50 points forward: self.forward()
            - move 50 points backward: self.backwards()
            - shoots cost 3 points of energy (when the enemy is hit he gets 9 points damage and you receive 6 points cure): self.shoot()
        """

        alpha = -math.inf
        beta = math.inf

        state = self.get_current_state()
        action, evaluation = self.minimax(state, self.maxDepth, alpha, beta, True)

        # not quite following the minmax algorithm,
        # but a successfull little hack for the agent's behaviour
        if self.shot_possible_at_enemy():
            action = "shoot"

        print(action)
        if action == "turn_right":
           self.turn_right()
        elif action == "turn_left":
            self.turn_left()
        elif action == "forward":
            self.forward()
        elif action == "backward":
            self.backwards()
        elif action == "shoot":
            self.shoot()
            self.shoot()

    def eval(self, state):
        utility = 0
        if state.energy_self <= 0:
            return -math.inf+1
        elif state.energy_enemy <= 0:
            return math.inf-1

        utility = utility + self.shoot_enemy_heuristic(state)*1000
        utility = utility + self.in_enemy_sight_heuristic(state)*400
        #utility = utility + self.enemy_proximity_heuristic(state)*200
        utility = utility + self.wall_proximity_heuristic(state)*50
        
        return utility

    def onHitWall(self):
        self.reset()  # To reset the run fonction to the begining (automatically called on hitWall, and robotHit event)
        self.rPrint('ouch! a wall !')

    def sensors(self):  # NECESARY FOR THE GAME
        pass

    def onRobotHit(self, robotId, robotName):  # when My bot hit another
        self.rPrint('collision with:' + str(robotId))

    def onHitByRobot(self, robotId, robotName):
        self.rPrint("damn a bot collided me!")

    def onHitByBullet(self, bulletBotId, bulletBotName, bulletPower):  # NECESARY FOR THE GAME
        """ When i'm hit by a bullet"""
        self.rPrint("hit by " + str(bulletBotId) + "with power:" + str(bulletPower))

    def onBulletHit(self, botId, bulletId):  # NECESARY FOR THE GAME
        """when my bullet hit a bot"""
        self.rPrint("fire done on " + str(botId))

    def onBulletMiss(self, bulletId):  # NECESARY FOR THE GAME
        """when my bullet hit a wall"""
        self.rPrint("the bullet " + str(bulletId) + " fail")

    def onRobotDeath(self):  # NECESARY FOR THE GAME
        """When my bot die"""
        self.rPrint("damn I'm Dead")

    def onTargetSpotted(self, botId, botName, botPos):  # NECESARY FOR THE GAME
        "when the bot see another one"
        self.rPrint("I see the bot:" + str(botId) + "on position: x:" + str(botPos.x()) + " , y:" + str(botPos.y()))

    def onEnemyDeath(self):
        pass

    def get_positions(self):
        """
        Get the own as well as the enemy's position as arrays in the form of [x.y]
        Returns a tuple with the own position as the first and the enemy's position as the second element 
        """
        own_position_q_point = self.getPosition()
        own_position = [own_position_q_point.x(), own_position_q_point.y()]
        
        enemy_position_q_point = self.getPosition_enemy()
        enemy_position = [enemy_position_q_point.x(), enemy_position_q_point.y()]
        return (own_position, enemy_position)

    def get_current_state(self):
        """
        Get the current state of the game as described the 'State' class from the AI module
        Returns an instance of 'state'
        """
        own_position, enemy_position = self.get_positions()

        state = State(
            self.energy_left_self(),
            self.energy_left_enemy(),
            self.shot_possible_by_enemy(), 
            self.shot_possible_at_enemy(),
            own_position,
            enemy_position,
            self.getGunHeading(),
            self.getGunHeading_enemy(),
            self.getMapSize()
            )

        return state

    def minimax(self, state, depth, alpha, beta, is_max):
        """
        Implements the minimax algorithm to find the best action depending on a given state.
        Returns the best action to perfom.
        """
        if depth == 0 or state.is_terminal():
            return None, self.eval(state)

        possible_actions = state.get_possible_actions(not is_max)
        random_int = random.randint(0, len(possible_actions)-1)
        for count, action in enumerate(possible_actions):
            if count == random_int:
                best_action = action
                break
        
        if is_max:
            max_evaluation = -math.inf
            for action in possible_actions:
                new_state = state.apply_action(False, action)
                new_evaluation = self.minimax(new_state, depth-1, alpha, beta, False)[1]
                if new_evaluation > max_evaluation:
                    max_evaluation = new_evaluation
                    best_action = action
                
                alpha = max(alpha, new_evaluation)
                if beta <= alpha:
                    break
            return best_action, max_evaluation
        else:
            min_evaluation = math.inf
            for action in possible_actions:
                new_state = state.apply_action(True, action)
                new_evaluation = self.minimax(new_state, depth-1, alpha, beta, True)[1]
                if new_evaluation < min_evaluation:
                    min_evaluation = new_evaluation
                    best_action = action
                
                beta = min(beta, new_evaluation)
                if beta <= alpha:
                    break
            return best_action, min_evaluation

    minimal_distance_to_keep = 50.0

    def proximity_heuristic(self):
        cost = self.enemy_proximity_heuristic() + self.wall_proximity_heuristic()
        return cost

    def city_block_distance(self, first_position, second_position):  
        distance = sum([abs(first - second) for (first, second) in zip(first_position, second_position)])
        return distance

    def enemy_proximity_heuristic(self, state):
        own_position = [state.pos_self[0], state.pos_self[1]]
        
        enemy_position = [state.pos_enemy[0], state.pos_enemy[1]]
        return -self.city_block_distance(own_position, enemy_position)*300
        #if(self.city_block_distance(own_position, enemy_position) <= self.minimal_distance_to_keep):
        #    return 0
        #else:
        #    return 1

    def wall_proximity_heuristic(self, state):
        map_x_end, map_y_end = self.getMapSize()
        map_x_start = 0
        map_y_start = 0
        own_pos_x = state.pos_enemy[0]
        own_pos_y = state.pos_enemy[1]

        if self.city_block_distance([map_x_end],[own_pos_x]) <= self.minimal_distance_to_keep:
            return -5000
        if self.city_block_distance([map_y_end],[own_pos_y]) <= self.minimal_distance_to_keep:
            return -5000
        if self.city_block_distance([map_x_start],[own_pos_x]) <= self.minimal_distance_to_keep:
            return -5000
        if self.city_block_distance([map_y_start],[own_pos_y]) <= self.minimal_distance_to_keep:
            return -5000
        return 5000

    def shoot_enemy_heuristic(self, state):
        if state.shot_possibly_at_enemy:
            return 1
        else:
            return 0

    def in_enemy_sight_heuristic(self, state):
        if state.shot_possibly_by_enemy:
            return 0
        else:
            return 1