# -*- coding: utf-8 -*-
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def cleanRoom(self, robot):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/robot-room-cleaner/discuss/150132/Very-clear-Python-DFS-code-beat-99-+
        TP:
        Few things need to consider when we design the algorithm
        1. How we gonna check the spot being cleaned or not..?
            - Using Set() we can track visited nodes
        2. For each available nodes we need to clean all 4 directions
            -  each time we'll turn 90 degrees
        3. !!! How we decide we are done cleaning (When DFS ends..?)
            - We'll return to the our starting point (just like iRobot did)
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, 0, 1, set()) # Why init direction is 0, 1..? 因為題目說robot初始facing up

    def dfs(self, robot, x, y, x_direction, y_direction, visited):
        """
        a dfs algorithm to perform cleaning
        :param x: current x position
        :param y: current y position
        :param x_direction: current x direction
        :param y_direction: current y direction
        :param visted: a SET to record visited nodes
        :return:
        """
        robot.clean()
        visited.add((x, y))
        # once we done clean and add current cell into visited set, we need to move to next possible cells
        for i in range(4): # all 4 directions
            next_x = x + x_direction
            next_y = y + y_direction
            if (next_x, next_y) not in visited and robot.move():
                self.dfs(robot, next_x, next_y, x_direction, y_direction, visited)
                # We are gonna to return to previous position, but how..?
                # first we turn 180 degrees
                # then we move()
                # then we turn 180 degrees again to get back to original direction
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnLeft() # turn to next direction
            x_direction, y_direction = -y_direction, x_direction