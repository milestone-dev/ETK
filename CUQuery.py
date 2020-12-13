#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from eudplib import *

"""

"""


def toEPD(ptr):
        return EPD(ptr)


def getUnitType(epd):
        return f_wread_epd(epd + 0x064 / 4,  0x064 % 4)


def setUnitType(epd, unitType):
        wwrite_epd(epd + 0x064 / 4,  0x064 % 4, unitType)


def isUnitType(epd, unitType):
        return getUnitType(epd) == unitType


def getButtonSet(epd):
        return f_wread_epd(epd + 0x094 / 4,  0x094 % 4)


def getPlayerID(epd):
        return f_bread_epd(epd + 0x04C / 4,  0x04C % 4)


def getEnergy(epd):
        return f_wread_epd(epd + 0x0A2 / 4,  0x0A2 % 4) / 256


def setEnergy(epd, energy):
        DoActions(SetMemoryEPD(epd + 0x0A2 / 4, Add, (energy * 256) * 65536))


def hasEnergy(epd, energy):
        return getEnergy(epd) >= energy


def getShields(epd):
        return df_wread_epd(epd + 0x060 / 4)


def setShields(epd, shields):
        DoActions(SetMemoryEPD(epd + 0x060 / 4, SetTo, shields * 256))


def getHitpoints(epd):
        return df_wread_epd(epd + 0x008 / 4) / 256


def setHitpoints(epd, hitpoints):
        DoActions(SetMemoryEPD(epd + 0x008 / 4, SetTo, hitpoints * 256))


def getMaxHitpoint(epd):
        unitType = getUnitType(epd)
        return dwread(0x65FD00 + 9808 + unitType * 4) / 256


def getTopSpeed(epd):
        return df_wread_epd(epd + 0x034 / 4)


def setTopSpeed(epd, speed):
        DoActions(SetMemoryEPD(epd + 0x034 / 4, SetTo, speed))
        DoActions(SetMemoryEPD(epd + 0x03C / 4, SetTo, speed))


def getOriginalTopSpeed(epd):
        unitType = getUnitType(epd)
        return dwread(0x6C9858 + 1696 + unitType * 4)


def getAcceleration(epd):
            return f_wread_epd(epd + 0x048 / 4,  0x048 % 4)


def f_setAcceleration(epd, acceleration):
            wwrite_epd(epd + 0x048 / 4,  0x048 % 4, acceleration)


def f_getOriginalAcceleration(epd):
        unitType = getUnitType(epd)
        return wread(0x6C9858 + 1056 + unitType * 2)


def f_getOrder(epd):
        return f_bread_epd(epd + 0x04D / 4,  0x04D % 4)


def f_setOrder(epd, order):
        f_bwrite_epd(epd + 0x04D / 4,  0x04D % 4, order)


def f_getSecondaryOrder(epd):
        return f_bread_epd(epd + 0x0A6 / 4,  0x0A6 % 4)


def f_setSecondaryOrder(epd, order):
        f_bwrite_epd(epd + 0x0A6 / 4,  0x0A6 % 4, order)


def f_getCommandCard(epd):
        return f_wread_epd(epd + 0x094 / 4,  0x094 % 4) 


def f_setCommandCard(epd, id):
        wwrite_epd(epd + 0x094 / 4,  0x094 % 4, id)


def f_get106Flag(epd):
        return f_bread_epd(epd + 0x106 / 4,  0x106 % 4)


def f_set106Flag(epd, state):
        f_bwrite_epd(epd + 0x106 / 4,  0x106 % 4, state)


def f_increment106Flag(epd):
        set106Flag(epd, get106Flag(epd) + 1)


def f_get8Flag(epd):
        return  f_wread_epd(epd + 0x08C / 4,  0x08C % 4)


def f_set8Flag(epd, state):
        wwrite_epd(epd + 0x08C / 4,  0x08C % 4, state)


def f_getParasiteFlag(epd):
        return  f_bread_epd(epd + 0x121 / 4,  0x121 % 4)


def f_setParasiteFlag(epd, flag):
        f_bwrite_epd(epd + 0x121 / 4,  0x121 % 4, flag)


def f_getRemainingBuildTime(epd):
        return f_wread_epd(epd + 0x0AC / 4,  0x0AC % 4)


def f_setRemainingBuildTime(epd, time):
        wwrite_epd(epd + 0x0AC / 4,  0x0AC % 4, time)


def f_getSprite(epd):
        return df_wread_epd(epd + 0x00C / 4)


def f_getGroundWeaponCooldown(epd):
        return f_bread_epd(epd + 0x055 / 4,  0x055 % 4)


def f_setGroundWeaponCooldown(epd, cooldown):
        f_bwrite_epd(epd + 0x055 / 4,  0x055 % 4, cooldown)


def f_setSprite(epd, spriteID):
        DoActions(SetMemoryEPD(epd + 0x00C / 4, SetTo, spriteID))


def f_getPositionX(epd):
        return f_wread_epd(epd + 0x028 / 4,  0x028 % 4)


def f_getPositionY(epd):
        return f_wread_epd(epd + 0x02A / 4,  0x02A % 4)


def f_setPositionX(epd, x):
        wwrite_epd(epd + 0x028 / 4,  0x028 % 4, x)


def f_setPositionY(epd, y):
        wwrite_epd(epd + 0x02A / 4,  0x02A % 4, y)


# TARGETING 

def f_getTargetX(epd):
        return f_wread_epd(epd + 0x058 / 4,  0x058 % 4)


def f_getTargetY(epd):
        return f_wread_epd(epd + 0x05A / 4,  0x05A % 4)


def f_getTargetUnitRaw(epd):
        return df_wread_epd(epd + 0x05C / 4)


def f_isOrderTargetUnitValid(epd):
        return getTargetUnitRaw(epd) > 0


def f_getTargetUnit(epd):
        return EPD(getTargetUnitRaw(epd))


def f_setTargetUnit(epd, targetUnitPtr):
        DoActions(SetMemoryEPD(epd + 0x05C / 4, SetTo, targetUnitPtr))


# TIMERS

def f_getLarvaTimer(epd):
        return f_bread_epd(epd + 0x0CA / 4,  0x0CA % 4) / 65536 


def f_setLarvaTimer(epd, timer):
        f_bwrite_epd(epd + 0x0CA / 4,  0x0CA % 4, timer * 65536)


def f_getStimTimer(epd):
        return f_bread_epd(epd + 0x115 / 4,  0x115 % 4) / 256


def f_setStimTimer(epd, timer):
        f_bwrite_epd(epd + 0x115 / 4,  0x115 % 4, timer * 256)
            

def f_getRemoveTimer(epd):
        return f_wread_epd(epd + 0x110 / 4,  0x110 % 4)


def f_setRemoveTimer(epd, timer):
        wwrite_epd(epd + 0x110 / 4,  0x110 % 4, timer)