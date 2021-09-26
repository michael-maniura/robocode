#! /usr/bin/python
# -*- coding: utf-8 -*-
from AI.actions import Action
from AI.state import State

from Objects.robot import Robot  # Import a base Robot
import random

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
        self.action_by_enemy_sight_heuristic()
        self.action_by_shoot_enemy_heuristic()

        #self.action_by_proximity_heuristic()
        
        """
        random_value = random.randint(0,9)
        if random_value <= 1:
            self.turn_left()
        elif random_value <= 3:
            self.turn_right()
        """
        
        """
        if not self.shot_possible_at_enemy():
            self.gunTurn(10)
            self.forward()
            pos = self.getPosition()
            some = 0
        else:
            self.shoot()
        """

    def eval(self, state):
        """implement your evaluation function here"""
        utility = 0
        return self, utility


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

    minimal_distance_to_keep = 50.0

    def action_by_proximity_heuristic(self):
        if self.proximity_heuristic() > 0:
            self.turn_left()
            self.turn_left()
            self.turn_left()
        self.forward()

    def proximity_heuristic(self):
        cost = self.enemy_proximity_heuristic() + self.wall_proximity_heuristic()
        return cost

    def city_block_distance(self, first_position, second_position):  
        distance = sum([abs(first - second) for (first, second) in zip(first_position, second_position)])
        return distance

    def enemy_proximity_heuristic(self):
        own_position_q_point = self.getPosition()
        own_position = [own_position_q_point.x(), own_position_q_point.y()]
        
        enemy_position_q_point = self.getPosition_enemy()
        enemy_position = [enemy_position_q_point.x(), enemy_position_q_point.y()]
        if(self.city_block_distance(own_position, enemy_position) <= self.minimal_distance_to_keep):
            return 1
        else:
            return 0

    def wall_proximity_heuristic(self):
        map_x_end, map_y_end = self.getMapSize()
        map_x_start = 0
        map_y_start = 0
        own_pos_q_point  = self.getPosition()
        own_pos_x = own_pos_q_point.x()
        own_pos_y = own_pos_q_point.y()

        if self.city_block_distance([map_x_end],[own_pos_x]) <= self.minimal_distance_to_keep:
            return 1
        if self.city_block_distance([map_y_end],[own_pos_y]) <= self.minimal_distance_to_keep:
            return 1
        if self.city_block_distance([map_x_start],[own_pos_x]) <= self.minimal_distance_to_keep:
            return 1
        if self.city_block_distance([map_y_start],[own_pos_y]) <= self.minimal_distance_to_keep:
            return 1
        return 0

    def action_by_shoot_enemy_heuristic(self):
        if self.shoot_enemy_heuristic() == 0:
            self.shoot()
        else:
            self.gunTurn(5)

    def shoot_enemy_heuristic(self):
        if self.shot_possible_at_enemy():
            return 0
        else:
            return 1

    def action_by_enemy_sight_heuristic(self):
        if self.in_enemy_sight_heuristic() > 0:
            self.forward()
            self.forward()

    def in_enemy_sight_heuristic(self):
        if self.shot_possible_by_enemy():
            return 1
        else:
            return 0