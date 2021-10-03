#! /usr/bin/python
# -*- coding: utf-8 -*-
from AI.actions import Action
from Objects.robot import Robot  # Import a base Robot
from AI.state import State
import random
import math


class PieresBot(Robot):  # Create a Robot


    def init(self):  # To initialyse your robot

        # Feel free to customize: Set the bot color in RGB
        self.setColor(108, 124, 89)
        self.setGunColor(0, 0, 0)
        self.setRadarColor(0, 60, 0)
        self.setBulletsColor(255, 150, 150)
        self.maxDepth = 5
        self.anzMax = 0     #Anzahl Berechnungen pro Ebene -> 15-10-20: Passen noch nicht zusammen
        self.anzMin = 0
        self.counter = 0    #Anzahl Berechnungen bis Aktion

        #Don't Change
        self.setRadarField("thin")
        self.radarVisible(True)  # if True the radar field is visible
        self.gun_to_side()
        self.lockRadar("gun")
        self.size = self.getMapSize()

    def run(self):  # main loop to command the bot
        """
        to create your own bot, create an new python-file in python package "Robots" and giv it a name
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
        
        selfPos = self.getPosition()
        enemyPos = self.getPosition_enemy()
        if enemyPos == None:
            return
        selfPosList = [selfPos.x(), selfPos.y()]
        enemyPosList = [enemyPos.x(), enemyPos.y()]
        currentState = State(self.energy_left_self(), self.energy_left_enemy(), 
                             self.shot_possible_by_enemy(), 
                             self.shot_possible_at_enemy(), selfPosList, 
                             enemyPosList, self.getGunHeading(), 
                             self.getGunHeading_enemy(), self.getMapSize())
        alpha = CustomUtility(-1000, 0, 0)
        beta = CustomUtility(1000,0,0)
        maxEval, actions = self.miniMax(currentState, 4, alpha, beta, True)        
        #maxEval, actions = self.miniMax(currentState, 5, -100, 100, True)
        print("Rechenschritte bis Aktion:", self.counter)
        self.counter = 0
        print(actions)
        
        if currentState.shot_possibly_at_enemy:
            print("Schussmöglichkeit")
        if len(actions) > 1:
            if "shoot" in actions:
                action = "shoot"
            else:
                action = random.choice(actions)
        else:
            action = actions[0]    
        if action == "turn_right":
            self.turn_right()
        elif action == "shoot":
            #if currentState.shot_possibly_at_enemy:
                self.shoot()
        elif action == "turn_left":
            self.turn_left()
        elif action == "forward":
            self.forward()
        else:
            self.backwards()
    
    def miniMax(self, state, depth, alpha, beta, maxPlayer):
        actions = []
        #not maxPlayer, da get_possible_actions False für den eigenen Spieler erwartet
        possible_actions = [a for a in state.get_possible_actions(not maxPlayer)]
        if depth == 0:
            #bessere Pruning-Ergebnisse durch zufällige Reihenfolge
            #der untersten Ebene
            random.shuffle(possible_actions)
        if maxPlayer:
            maxEval = CustomUtility(-1000,0,0)
            for action in possible_actions:
                self.anzMax += 1
                currentState = state.apply_action(False, action)
                if depth == 0:
                    robot, val = self.eval(currentState)
                else:
                    #Rekursion zum zweigweisen Durchlauf des
                    #Entscheidungsbaums
                    val, nextAction = self.miniMax(currentState, 
                                                   depth - 1, alpha, 
                                                   beta, False)
                if val > alpha:
                    alpha = val
                #Alpha-Beta-Pruning
                if beta <= alpha:
                    #print("Berechnungen Max-Zweige:", self.anzMax)
                    #self.anzMax = 0
                    return alpha, []
                if val > maxEval:
                    maxEval = val
                    #Zurücksetzen der Aktionsliste, sollten mehrere
                    #Aktionen die gleiche, beste Bewertung erhalten
                    actions = [action]
                elif val == maxEval:
                    actions += [action]
            #print("Berechnungen Max-Zweige:", self.anzMax)
            #self.anzMax = 0
            return maxEval, actions
        else:
            minEval = CustomUtility(1000,0,0)
            for action in possible_actions:
                self.anzMin += 1
                currentState = state.apply_action(True, action)
                if depth == 0:
                    robot, val = self.eval(currentState)
                else:
                    val, nextAction = self.miniMax(currentState, 
                                                   depth - 1, alpha, 
                                                   beta, True)
                if val < beta:
                    beta = val
                if beta <= alpha:
                    #print("Berechnungen Min-Zweige:" ,self.anzMin)
                    #self.anzMin = 0
                    return beta, []
                if val < minEval:
                    minEval = val
                    actions = [action]
                elif val == minEval:
                    actions += [action]
            #print("Berechnungen Min-Zweige:" ,self.anzMin)
            #self.anzMin = 0
            return minEval, actions
    
    def schussWinkel(self, self_angle, xSelf, ySelf, xEn, yEn):
        #Verhinderung einer Nulldivision
        if xEn == xSelf:
            if yEn > ySelf:
                angleTan = 0
            else:
                angleTan = 180
        else:
            angleTan = math.degrees(math.atan((yEn-ySelf)/(xEn-xSelf)))
        '''
        Der Nullpunkt liegt oben links in der Ecke der GUI.
        So werden die Koordinaten des Enemy größer, wenn er sich
        rechts unter dem Spieler befindet.
        
        Zur grafischen Erläuterung der Winkelberechnung siehe OneNote
        '''
        if xEn > xSelf:
            angle = 270 + angleTan
        else:
            angle = 90 + angleTan
        angle = abs(angle - self_angle)
        #Korrektur des angle, sodass immer die richtige Richtung
        #berechnet wird
        if angle > 180:
            angle = 360 - angle
        return angle
    
    def evalNum(self, state, action):
        
        self.counter += 1
        #Versuch einer numerischen Bewertungsmethodik, die die
        #State-Merkamle numerisch ausdrückt und normiert berücksichtigt
        if state.energy_self == 0:
            utility = -1000
        elif state.energy_enemy == 0:
            utility = 1000
        else:
            utility = 100
        shotSelf = state.shot_possibly_at_enemy
        shotEn = state.shot_possibly_by_enemy
        if shotEn:
            utility -= 10
        elif shotSelf:
            utility += 10
            
        xSelf = state.pos_self[0]
        ySelf = state.pos_self[1]
        xEn = state.pos_enemy[0]
        yEn = state.pos_enemy[1]
        
        #Normierung um gleichgewichtete numerische Bewertung (ggf. faktorisiert) durchzuführen
        angle = self.schussWinkel(state.angle_self, xSelf, ySelf, xEn, yEn)/180
        distance = math.sqrt((xSelf-xEn)**2+(ySelf-yEn)**2)
        #Kehrwert, da die minimalste Position höchstmögliche belohnt werden soll
        #56 ergibt sich aus 38 (Roboterbreite) * Wurzel 2 -> so sollen Kollisionsbewegungen durch Bestrafung vermieden werden
        if distance <=56:
            distance = -1/distance
        else:
            distance = 1/distance
        if angle == 0:
            angle += 0.001
        angle = 1/angle
        
        #Normierung nicht zwangsläufig notwendig -> nur zur vereinfachten Faktorisierung
        utility = utility + 1/(state.energy_self/100) - 1/(state.energy_enemy/100) + angle + distance*10
        #print(action, ": ", round(utility, 2), sep="")
        return self, utility
    
    ''' Krax-Eval
    def evalKrax(self, state):
        """implement your evaluation function here"""
        self.counter += 1
        health = self.CalcHealthUtility(state)
        distance = self.CalcDistanceSquare(state)
        angle = self.CalcAngleDifference(state)
        return self, CustomUtility(health, distance,angle)
    
    def CalcHealthUtility(self, state):
        if state.energy_self == 0:
            return -1000
        elif state.energy_enemy == 0:
            return 1000
        
        utility = state.energy_self - state.energy_enemy
        if state.shot_possibly_at_enemy:
            utility += 10
        if state.shot_possibly_by_enemy:
            utility -= 10
        return utility


    def CalcDistanceSquare(self, state):
        return math.sqrt((state.pos_self[0] - state.pos_enemy[0])**2 + (state.pos_self[1] - state.pos_enemy[1])**2)

    def CalcAngleDifference(self, state):
        gunAngle = state.angle_self
        posAngle = self.CalcPositionAngle(state)
        angle = abs(gunAngle - posAngle)
        if angle > 180:
            angle = 360 - angle
        return angle

    def CalcPositionAngle(self, state):
        xEn = state.pos_enemy[0]
        yEn = state.pos_enemy[1]
        xSelf = state.pos_self[0]
        ySelf = state.pos_self[1]

        if xSelf == xEn:
            if yEn > ySelf:
                return 0
            else:
                return 180
        
        angleTan = math.atan((yEn-ySelf)/(xEn-xSelf))
        angleTan = math.degrees(angleTan)

        if xEn > xSelf:
            return 270 + angleTan
        return 90 + angleTan
    '''
    
    def eval(self, state):
        """implement your evaluation function here"""
        self.counter += 1
        if state.energy_self == 0:
            utility = -1000
        elif state.energy_enemy == 0:
            utility = 1000
            
        #Ggf. sinnvoll, die Lebenspunkte, Distanz und Winkeldifferenz
        #direkt numerisch zu bewerten
        utility = state.energy_self - state.energy_enemy
        if state.shot_possibly_by_enemy:
            utility -= 10
        elif state.shot_possibly_at_enemy:
            utility += 10
        xSelf = state.pos_self[0]
        ySelf = state.pos_self[1]
        xEn = state.pos_enemy[0]
        yEn = state.pos_enemy[1]
        
        angle = self.schussWinkel(state.angle_self, xSelf, ySelf, xEn, yEn)
        distance = math.sqrt((xSelf-xEn)**2+(yEn-ySelf)**2)
        
        return self, CustomUtility(utility, distance, angle)


    def onHitWall(self):
        self.reset()  # To reset the run fonction to the begining (auomatically called on hitWall, and robotHit event)
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

class CustomUtility:

    def __init__(self, health, angle, distance):
        self.health = health
        self.distance = distance
        self.angle = angle
        self.value = angle/2 + distance
        if distance <= 56:
            self.value *= 100

    
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value
    
    
    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        self.__angle = value

    #Funktionen zum Überladen der Vergleichsoperatoren zur Verwendung
    #bei zwei CustomUtility-Instanzen
    def __eq__(self, other):
        return self.health == other.health and self.value == other.value
    
    def __gt__(self, other):
        #Priorisierung der Lebensenergie
        if self.health > other.health:
            return True
        if self.health < other.health:
            return False
        if self.value < other.value:
            return True
        return False
    
    def __lt__(self, other):
        return other > self
    def __le__(self, other):
        return not self > other
    def __ge__(self, other):
        return self == other or self > other
    def __ne__(self, other):
        return not self == other
