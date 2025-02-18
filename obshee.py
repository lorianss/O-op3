#!/usr/bin/env python3
# -*- coding: utf-8 -*

from random import randint


class Warrior:
    def __init__(self, id="default", team="default"):
        self.__id = id
        self.__team = team

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = str(value)

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        self.__team = str(value)


class Hero(Warrior):
    def __init__(self, id="default", team="default", level=0, team_list=[]):
        super().__init__(id, team)
        self.__level = level
        self.__team_list = team_list

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = int(value)

    @property
    def team_list(self):
        return self.__team_list

    @team_list.setter
    def team_list(self, value):
        self.__team_list = value

    def level_up(self, n=1):
        self.level = self.level + n


class Soldier(Warrior):
    def __init__(self, id="default", team="default", hero=None):
        super().__init__(id, team)
        self.__hero = hero

    @property
    def hero(self):
        return self.__hero

    @hero.setter
    def hero(self, value):
        self.__hero = value

    def follow(self, hero):
        self.hero = hero
        self.team = hero.team


if __name__ == "__main__":
    first_hero = Hero("h001", "Red", 0)
    second_hero = Hero("h002", "Green", 0)
    red_soldiers = []
    green_soldiers = []
    for i in range(0, 16):
        temp_soldier = Soldier("00" + str(i))
        if randint(0, 1) == 0:
            red_soldiers.append(temp_soldier)

        else:
            green_soldiers.append(temp_soldier)

    first_hero.team_list = red_soldiers
    second_hero.team_list = green_soldiers
    if len(first_hero.team_list) < len(second_hero.team_list):
        second_hero.level += 1
        print(
            f"Команда второго героя больше.\nУровень второго героя: {second_hero.level}\nУровень первого героя: {first_hero.level}")
    elif len(first_hero.team_list) > len(second_hero.team_list):
        first_hero.level += 1
        print(
            f"Команда первого героя больше.\nУровень первого героя: {first_hero.level}\nУровень второго героя: {second_hero.level}")
    else:
        print("Размер команд одинаковый, уровни героев не изменились")

    red_soldiers[0].follow(first_hero)
    print(red_soldiers[0].hero.id)
    print(red_soldiers[0].id)
