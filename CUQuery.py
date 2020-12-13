#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from eudplib import *

@EUDFunc

def f_dwwrite_epd(epd, addr, value):
    DoActions([SetMemoryEPD(epd + addr // 4, SetTo, value)])

def f_toEPD(ptr):
    return EPD(ptr)


def f_getUnitType(epd):
    return f_wread_epd(epd + 0x064 // 4,  0x064 % 4)


def f_setUnitType(epd, unitType):
    f_wwrite_epd(epd + 0x064 // 4,  0x064 % 4, unitType)


def f_isUnitType(epd, unitType):
    return getUnitType(epd) == unitType


def f_getButtonSet(epd):
    return f_wread_epd(epd + 0x094 // 4,  0x094 % 4)


def f_getPlayerID(epd):
    return f_bread_epd(epd + 0x04C // 4,  0x04C % 4)


def f_getEnergy(epd):
    return f_wread_epd(epd + 0x0A2 // 4,  0x0A2 % 4) // 256


def f_setEnergy(epd, energy):
    DoActions([SetMemoryEPD(epd + 0x0A2 // 4, Add, (energy * 256) * 65536)])


def f_hasEnergy(epd, energy):
    return getEnergy(epd) >= energy


def f_getShields(epd):
    return f_dwread_epd(epd + 0x060 // 4)


def f_setShields(epd, shields):
    DoActions([SetMemoryEPD(epd + 0x060 // 4, SetTo, shields * 256)])


def f_getHitpoints(epd):
    return f_dwread_epd(epd + 0x008 // 4) // 256


def f_setHitpoints(epd, hitpoints):
    DoActions([SetMemoryEPD(epd + 0x008 // 4, SetTo, hitpoints * 256)])


def f_getMaxHitpoint(epd):
    unitType = getUnitType(epd)
    return dwread(0x65FD00 + 9808 + unitType * 4) // 256


def f_setPreviousHitpoints(epd, value):
    f_wwrite_epd(epd + 0x0AE // 4,  0x0AE % 4, value)


def f_getPreviousHitpoints(epd):
    return f_wread_epd(epd + 0x0AE // 4,  0x0AE % 4)


def f_getTopSpeed(epd):
    return f_dwread_epd(epd + 0x034 // 4)


def f_setTopSpeed(epd, speed):
    DoActions([SetMemoryEPD(epd + 0x034 // 4, SetTo, speed)])
    DoActions([SetMemoryEPD(epd + 0x03C // 4, SetTo, speed)])


def f_getOriginalTopSpeed(epd):
    unitType = getUnitType(epd)
    return dwread(0x6C9858 + 1696 + unitType * 4)


def f_getAcceleration(epd):
    return f_wread_epd(epd + 0x048 // 4,  0x048 % 4)


def f_setAcceleration(epd, acceleration):
    f_wwrite_epd(epd + 0x048 // 4,  0x048 % 4, acceleration)


def f_getOriginalAcceleration(epd):
    unitType = getUnitType(epd)
    return wread(0x6C9858 + 1056 + unitType * 2)


def f_getOrder(epd):
    return f_bread_epd(epd + 0x04D // 4,  0x04D % 4)


def f_setOrder(epd, order):
    f_bwrite_epd(epd + 0x04D // 4,  0x04D % 4, order)


def f_getSecondaryOrder(epd):
    return f_bread_epd(epd + 0x0A6 // 4,  0x0A6 % 4)


def f_setSecondaryOrder(epd, order):
    f_bwrite_epd(epd + 0x0A6 // 4,  0x0A6 % 4, order)


def f_getCommandCard(epd):
    return f_wread_epd(epd + 0x094 // 4,  0x094 % 4) 


def f_setCommandCard(epd, id):
    f_wwrite_epd(epd + 0x094 // 4,  0x094 % 4, id)


def f_get106Flag(epd):
    return f_bread_epd(epd + 0x106 // 4,  0x106 % 4)


def f_set106Flag(epd, state):
    f_bwrite_epd(epd + 0x106 // 4,  0x106 % 4, state)


def f_increment106Flag(epd):
    set106Flag(epd, get106Flag(epd) + 1)


def f_get8Flag(epd):
    return  f_wread_epd(epd + 0x08C // 4,  0x08C % 4)


def f_set8Flag(epd, state):
    f_wwrite_epd(epd + 0x08C // 4,  0x08C % 4, state)


def f_getParasiteFlag(epd):
    return  f_bread_epd(epd + 0x121 // 4,  0x121 % 4)


def f_setParasiteFlag(epd, flag):
    f_bwrite_epd(epd + 0x121 // 4,  0x121 % 4, flag)


def f_getRemainingBuildTime(epd):
    return f_wread_epd(epd + 0x0AC // 4,  0x0AC % 4)


def f_setRemainingBuildTime(epd, time):
    f_wwrite_epd(epd + 0x0AC // 4,  0x0AC % 4, time)


def f_getSprite(epd):
    return f_dwread_epd(epd + 0x00C // 4)


def f_getGroundWeaponCooldown(epd):
    return f_bread_epd(epd + 0x055 // 4,  0x055 % 4)


def f_setGroundWeaponCooldown(epd, cooldown):
    f_bwrite_epd(epd + 0x055 // 4,  0x055 % 4, cooldown)


def f_setSprite(epd, spriteID):
    DoActions([SetMemoryEPD(epd + 0x00C // 4, SetTo, spriteID)])


def f_getPositionX(epd):
    return f_wread_epd(epd + 0x028 // 4,  0x028 % 4)


def f_getPositionY(epd):
    return f_wread_epd(epd + 0x02A // 4,  0x02A % 4)


def f_setPositionX(epd, x):
    f_wwrite_epd(epd + 0x028 // 4,  0x028 % 4, x)


def f_setPositionY(epd, y):
    f_wwrite_epd(epd + 0x02A // 4,  0x02A % 4, y)


def f_setPosition(epd, x, y):
    f_setPositionX(epd, x)
    f_setPositionY(epd, y + y*65536)


def f_getResourceCarryCount(epd) :
    return f_bread_epd(epd + 0x0CF // 4,  0x0CF % 4)


def f_setResourceCarryCount(epd, count) :
    f_bwrite_epd(epd + 0x0CF // 4,  0x0CF % 4, count)


def f_getIsCarryingSomething(epd):
    return f_bread_epd(epd + 0x0CE // 4,  0x0CE % 4)


def f_setIsCarryingSomething(epd, flag):
    f_bwrite_epd(epd + 0x0CE // 4,  0x0CE % 4, flag)


def f_setConnectedUnit(epd, value):
    DoActions([SetMemoryEPD(epd + 0x080 // 4, SetTo, value)])


def f_getConnectedUnit(epd):
    return f_dwread_epd(epd + 0x080 // 4)

# TARGETING 

def f_getTargetX(epd):
    return f_wread_epd(epd + 0x058 // 4,  0x058 % 4)


def f_getTargetY(epd):
    return f_wread_epd(epd + 0x05A // 4,  0x05A % 4)


def f_getTargetUnitRaw(epd):
    return f_dwread_epd(epd + 0x05C // 4)

def f_isOrderTargetUnitValid(epd):
    return f_getTargetUnitRaw(epd) > 0


def f_getTargetUnit(epd):
    return EPD(f_getTargetUnitRaw(epd))

def f_setTargetUnit(epd, targetUnitPtr):
    DoActions([SetMemoryEPD(epd + 0x05C // 4, SetTo, targetUnitPtr)])


def f_getTargetResourceRaw(epd):
    return f_dwread_epd(epd + 0x0C8 // 4)

# TIMERS

def f_getLarvaTimer(epd):
    return f_bread_epd(epd + 0x0CA // 4,  0x0CA % 4) // 65536 


def f_setLarvaTimer(epd, timer):
    f_bwrite_epd(epd + 0x0CA // 4,  0x0CA % 4, timer * 65536)


def f_getStimTimer(epd):
    return f_bread_epd(epd + 0x115 // 4,  0x115 % 4) // 256


def f_setStimTimer(epd, timer):
    f_bwrite_epd(epd + 0x115 // 4,  0x115 % 4, timer * 256)


def f_getRemoveTimer(epd):
    return f_wread_epd(epd + 0x110 // 4,  0x110 % 4)


def f_setRemoveTimer(epd, timer):
    f_wwrite_epd(epd + 0x110 // 4,  0x110 % 4, timer)


def f_getMaelstromTimer(epd):
    return f_bread_epd(epd + 0x124 // 4,  0x124 % 4)


def f_setMaelstromTimer(epd, timer):
    f_bwrite_epd(epd + 0x124 // 4,  0x124 % 4, timer)


def f_getEnsnareTimer(epd):
    return f_bread_epd(epd + 0x116 // 4,  0x116 % 4)


def f_setEnsnareTimer(epd, timer):
    f_bwrite_epd(epd + 0x116 // 4,  0x116 % 4, timer)


def f_getLockdownTimer(epd):
    return f_bread_epd(epd + 0x117 // 4,  0x117 % 4)


def f_setLockdownTimer(epd, timer):
    f_bwrite_epd(epd + 0x117 // 4,  0x117 % 4, timer)


def f_getStasisTimer(epd):
    return f_bread_epd(epd + 0x119 // 4,  0x119 % 4)


def f_setStasisTimer(epd, timer):
    f_bwrite_epd(epd + 0x119 // 4,  0x119 % 4, timer)


def f_getPlagueTimer(epd):
    return f_bread_epd(epd + 0x11A // 4,  0x11A % 4)


def f_setPlagueTimer(epd, timer):
    f_bwrite_epd(epd + 0x11A // 4,  0x11A % 4, timer)


def f_getStormTimer(epd):
    return f_bread_epd(epd + 0x11B // 4,  0x11B % 4)


def f_setStormTimer(epd, timer):
    f_bwrite_epd(epd + 0x11B // 4,  0x11B % 4, timer)


"""
def getPrev(epd):
    return f_dwread_epd(epd + 0x000 // 4, 0x000 % 4)

def setPrev(epd, value):
    f_dwwrite_epd(epd, 0x000, value, value)

def getNext(epd):
    return f_dwread_epd(epd + 0x004 // 4, 0x004 % 4)

def setNext(epd, value):
    f_dwwrite_epd(epd, 0x004, value, value)

def getHitPoints(epd):
    return f_dwread_epd(epd + 0x008 // 4, 0x008 % 4)

def setHitPoints(epd, value):
    f_dwwrite_epd(epd, 0x008, value, value)

def getSprite(epd):
    return f_dwread_epd(epd + 0x00C // 4, 0x00C % 4)

def setSprite(epd, value):
    f_dwwrite_epd(epd, 0x00C, value, value)

def getMoveTargetX(epd):
    return f_wread_epd(epd + 0x010 // 4, 0x010 % 4)

def setMoveTargetX(epdepd, value):
    f_wread_epd(epd + 0x010 // 4, 0x010 % 4)

def getMoveTargetY(epd):
    return f_wread_epd(epd + 0x012 // 4, 0x012 % 4)

def setMoveTargetY(epdepd, value):
    f_wread_epd(epd + 0x012 // 4, 0x012 % 4)

def getMoveTargetUnit(epd):
    return f_dwread_epd(epd + 0x014 // 4, 0x014 % 4)

def setMoveTargetUnit(epdepd, value):
    f_dwread_epd(epd + 0x014 // 4, 0x014 % 4)

def getNextMovementWaypointX(epd):
    return f_wread_epd(epd + 0x018 // 4, 0x018 % 4)

def setNextMovementWaypointX(epd, value):
    f_wwrite_epd(epd + 0x018 // 4, 0x018 % 4, value)

def getNextMovementWaypointY(epd):
    return f_wread_epd(epd + 0x01A // 4, 0x01A % 4)

def setNextMovementWaypointY(epd, value):
    f_wwrite_epd(epd + 0x01A // 4, 0x01A % 4, value)

def getNextTargetWaypointX(epd):
    return f_wread_epd(epd + 0x01C // 4, 0x01C % 4)

def setNextTargetWaypointX(epdepd, value):
    f_wread_epd(epd + 0x01C // 4, 0x01C % 4)

def getNextTargetWaypointY(epd):
    return f_wread_epd(epd + 0x01E // 4, 0x01E % 4)

def setNextTargetWaypointY(epdepd, value):
    f_wread_epd(epd + 0x01E // 4, 0x01E % 4)

def getMovementFlags(epd):
    return f_bread_epd(epd + 0x020 // 4, 0x020 % 4)

def setMovementFlags(epd, value):
    f_bwrite_epd(epd + 0x020 // 4, 0x020 % 4, value)

def getCurrentDirection1(epd):
    return f_bread_epd(epd + 0x021 // 4, 0x021 % 4)

def setCurrentDirection1(epd, value):
    f_bwrite_epd(epd + 0x021 // 4, 0x021 % 4, value)

def getFlingyTurnRadius(epd):
    return f_bread_epd(epd + 0x022 // 4, 0x022 % 4)

def setFlingyTurnRadius(epd, value):
    f_bwrite_epd(epd + 0x022 // 4, 0x022 % 4, value)

def getVelocityDirection1(epd):
    return f_bread_epd(epd + 0x023 // 4, 0x023 % 4)

def setVelocityDirection1(epd, value):
    f_bwrite_epd(epd + 0x023 // 4, 0x023 % 4, value)

def getFlingyID(epd):
    return f_wread_epd(epd + 0x024 // 4, 0x024 % 4)

def setFlingyID(epd, value):
    f_wwrite_epd(epd + 0x024 // 4, 0x024 % 4, value)

def get_unknown_0x026(epd):
    return f_bread_epd(epd + 0x026 // 4, 0x026 % 4)

def set_unknown_0x026(epd, value):
    f_bwrite_epd(epd + 0x026 // 4, 0x026 % 4, value)

def getFlingyMovementType(epd):
    return f_bread_epd(epd + 0x027 // 4, 0x027 % 4)

def setFlingyMovementType(epd, value):
    f_bwrite_epd(epd + 0x027 // 4, 0x027 % 4, value)

def getPositionX(epd):
    return f_wread_epd(epd + 0x028 // 4, 0x028 % 4)

def setPositionX(epd, value):
    f_wwrite_epd(epd + 0x028 // 4, 0x028 % 4, value)

def getPositionY(epd):
    return f_wread_epd(epd + 0x02A // 4, 0x02A % 4)

def setPositionY(epd, value):
    f_wwrite_epd(epd + 0x02A // 4, 0x02A % 4, value)

def getHaltX(epd):
    return f_dwread_epd(epd + 0x02C // 4, 0x02C % 4)

def setHaltX(epd, value):
    f_dwwrite_epd(epd, 0x02C, value, value)

def getHaltY(epd):
    return f_dwread_epd(epd + 0x030 // 4, 0x030 % 4)

def setHaltY(epd, value):
    f_dwwrite_epd(epd, 0x030, value, value)

def getFlingyTopSpeed(epd):
    return f_dwread_epd(epd + 0x034 // 4, 0x034 % 4)

def setFlingyTopSpeed(epd, value):
    f_dwwrite_epd(epd, 0x034, value, value)

def getCurrent_speed1(epd):
    return f_dwread_epd(epd + 0x038 // 4, 0x038 % 4)

def setCurrent_speed1(epd, value):
    f_dwwrite_epd(epd, 0x038, value, value)

def getCurrent_speed2(epd):
    return f_dwread_epd(epd + 0x03C // 4, 0x03C % 4)

def setCurrent_speed2(epd, value):
    f_dwwrite_epd(epd, 0x03C, value, value)

def getCurrent_speedX(epd):
    return f_dwread_epd(epd + 0x040 // 4, 0x040 % 4)

def setCurrent_speedX(epd, value):
    f_dwwrite_epd(epd, 0x040, value, value)

def getCurrent_speedY(epd):
    return f_dwread_epd(epd + 0x044 // 4, 0x044 % 4)

def setCurrent_speedY(epd, value):
    f_dwwrite_epd(epd, 0x044, value, value)

def getFlingyAcceleration(epd):
    return f_wread_epd(epd + 0x048 // 4, 0x048 % 4)

def setFlingyAcceleration(epd, value):
    f_wwrite_epd(epd + 0x048 // 4, 0x048 % 4, value)

def getCurrentDirection2(epd):
    return f_bread_epd(epd + 0x04A // 4, 0x04A % 4)

def setCurrentDirection2(epd, value):
    f_bwrite_epd(epd + 0x04A // 4, 0x04A % 4, value)

def getVelocityDirection2(epd):
    return f_bread_epd(epd + 0x04B // 4, 0x04B % 4)

def setVelocityDirection2(epd, value):
    f_bwrite_epd(epd + 0x04B // 4, 0x04B % 4, value)

def getPlayerID(epd):
    return f_bread_epd(epd + 0x04C // 4, 0x04C % 4)

def setPlayerID(epd, value):
    f_bwrite_epd(epd + 0x04C // 4, 0x04C % 4, value)

def getOrderID(epd):
    return f_bread_epd(epd + 0x04D // 4, 0x04D % 4)

def setOrderID(epd, value):
    f_bwrite_epd(epd + 0x04D // 4, 0x04D % 4, value)

def getOrderState(epd):
    return f_bread_epd(epd + 0x04E // 4, 0x04E % 4)

def setOrderState(epd, value):
    f_bwrite_epd(epd + 0x04E // 4, 0x04E % 4, value)

def getOrderSignal(epd):
    return f_bread_epd(epd + 0x04F // 4, 0x04F % 4)

def setOrderSignal(epd, value):
    f_bwrite_epd(epd + 0x04F // 4, 0x04F % 4, value)

def getOrderUnitType(epd):
    return f_wread_epd(epd + 0x050 // 4, 0x050 % 4)

def setOrderUnitType(epd, value):
    f_wwrite_epd(epd + 0x050 // 4, 0x050 % 4, value)

def get__0x52(epd):
    return f_wread_epd(epd + 0x052 // 4, 0x052 % 4)

def set__0x52(epd, value):
    f_wwrite_epd(epd + 0x052 // 4, 0x052 % 4, value)

def getMainOrderTimer(epd):
    return f_bread_epd(epd + 0x054 // 4, 0x054 % 4)

def setMainOrderTimer(epd, value):
    f_bwrite_epd(epd + 0x054 // 4, 0x054 % 4, value)

def getGroundWeaponCooldown(epd):
    return f_bread_epd(epd + 0x055 // 4, 0x055 % 4)

def setGroundWeaponCooldown(epd, value):
    f_bwrite_epd(epd + 0x055 // 4, 0x055 % 4, value)

def getAirWeaponCooldown(epd):
    return f_bread_epd(epd + 0x056 // 4, 0x056 % 4)

def setAirWeaponCooldown(epd, value):
    f_bwrite_epd(epd + 0x056 // 4, 0x056 % 4, value)

def getSpellCooldown(epd):
    return f_bread_epd(epd + 0x057 // 4, 0x057 % 4)

def setSpellCooldown(epd, value):
    f_bwrite_epd(epd + 0x057 // 4, 0x057 % 4, value)

def getOrderTargetX(epd):
    return f_wread_epd(epd + 0x058 // 4, 0x058 % 4)

def setOrderTargetX(epdepd, value):
    f_wread_epd(epd + 0x058 // 4, 0x058 % 4)

def getOrderTargetY(epd):
    return f_wread_epd(epd + 0x05A // 4, 0x05A % 4)

def setOrderTargetY(epdepd, value):
    f_wread_epd(epd + 0x05A // 4, 0x05A % 4)

def getOrderTargetUnit(epd):
    return f_dwread_epd(epd + 0x05C // 4, 0x05C % 4)

def setOrderTargetUnit(epdepd, value):
    f_dwread_epd(epd + 0x05C // 4, 0x05C % 4)

def getShieldPoints(epd):
    return f_dwread_epd(epd + 0x060 // 4, 0x060 % 4)

def setShieldPoints(epd, value):
    f_dwwrite_epd(epd, 0x060, value, value)

def getUnitType(epd):
    return f_wread_epd(epd + 0x064 // 4, 0x064 % 4)

def setUnitType(epd, value):
    f_wwrite_epd(epd + 0x064 // 4, 0x064 % 4, value)

def get__0x66(epd):
    return f_wread_epd(epd + 0x066 // 4, 0x066 % 4)

def set__0x66(epd, value):
    f_wwrite_epd(epd + 0x066 // 4, 0x066 % 4, value)

def getPreviousPlayerUnit(epd):
    return f_dwread_epd(epd + 0x068 // 4, 0x068 % 4)

def setPreviousPlayerUnit(epd, value):
    f_dwwrite_epd(epd, 0x068, value, value)

def getNextPlayerUnit(epd):
    return f_dwread_epd(epd + 0x06C // 4, 0x06C % 4)

def setNextPlayerUnit(epd, value):
    f_dwwrite_epd(epd, 0x06C, value, value)

def getSubUnit(epd):
    return f_dwread_epd(epd + 0x070 // 4, 0x070 % 4)

def setSubUnit(epd, value):
    f_dwwrite_epd(epd, 0x070, value, value)

def getOrderQueueHead(epd):
    return f_dwread_epd(epd + 0x074 // 4, 0x074 % 4)

def setOrderQueueHead(epd, value):
    f_dwwrite_epd(epd, 0x074, value, value)

def getOrderQueueTail(epd):
    return f_dwread_epd(epd + 0x078 // 4, 0x078 % 4)

def setOrderQueueTail(epd, value):
    f_dwwrite_epd(epd, 0x078, value, value)

def getAutoTargetUnit(epd):
    return f_dwread_epd(epd + 0x07C // 4, 0x07C % 4)

def setAutoTargetUnit(epdepd, value):
    f_dwread_epd(epd + 0x07C // 4, 0x07C % 4)

def getConnectedUnit(epd):
    return f_dwread_epd(epd + 0x080 // 4, 0x080 % 4)

def setConnectedUnit(epd, value):
    f_dwwrite_epd(epd, 0x080, value, value)

def getOrderQueueCount(epd):
    return f_bread_epd(epd + 0x084 // 4, 0x084 % 4)

def setOrderQueueCount(epd, value):
    f_bwrite_epd(epd + 0x084 // 4, 0x084 % 4, value)

def getOrderQueueTimer(epd):
    return f_bread_epd(epd + 0x085 // 4, 0x085 % 4)

def setOrderQueueTimer(epd, value):
    f_bwrite_epd(epd + 0x085 // 4, 0x085 % 4, value)

def get_unknown_0x086(epd):
    return f_bread_epd(epd + 0x086 // 4, 0x086 % 4)

def set_unknown_0x086(epd, value):
    f_bwrite_epd(epd + 0x086 // 4, 0x086 % 4, value)

def getAttackNotifyTimer(epd):
    return f_bread_epd(epd + 0x087 // 4, 0x087 % 4)

def setAttackNotifyTimer(epd, value):
    f_bwrite_epd(epd + 0x087 // 4, 0x087 % 4, value)

def getPreviousUnitType(epd):
    return f_wread_epd(epd + 0x088 // 4, 0x088 % 4)

def setPreviousUnitType(epd, value):
    f_wwrite_epd(epd + 0x088 // 4, 0x088 % 4, value)

def getLastEventTimer(epd):
    return f_bread_epd(epd + 0x08A // 4, 0x08A % 4)

def setLastEventTimer(epd, value):
    f_bwrite_epd(epd + 0x08A // 4, 0x08A % 4, value)

def getLastEventColor(epd):
    return f_bread_epd(epd + 0x08B // 4, 0x08B % 4)

def setLastEventColor(epd, value):
    f_bwrite_epd(epd + 0x08B // 4, 0x08B % 4, value)

def get_unused_0x08C(epd):
    return f_wread_epd(epd + 0x08C // 4, 0x08C % 4)

def set_unused_0x08C(epd, value):
    f_wwrite_epd(epd + 0x08C // 4, 0x08C % 4, value)

def getRankIncrease(epd):
    return f_bread_epd(epd + 0x08E // 4, 0x08E % 4)

def setRankIncrease(epd, value):
    f_bwrite_epd(epd + 0x08E // 4, 0x08E % 4, value)

def getKillCount(epd):
    return f_bread_epd(epd + 0x08F // 4, 0x08F % 4)

def setKillCount(epd, value):
    f_bwrite_epd(epd + 0x08F // 4, 0x08F % 4, value)

def getLastAttackingPlayer(epd):
    return f_bread_epd(epd + 0x090 // 4, 0x090 % 4)

def setLastAttackingPlayer(epd, value):
    f_bwrite_epd(epd + 0x090 // 4, 0x090 % 4, value)

def getSecondaryOrderTimer(epd):
    return f_bread_epd(epd + 0x091 // 4, 0x091 % 4)

def setSecondaryOrderTimer(epd, value):
    f_bwrite_epd(epd + 0x091 // 4, 0x091 % 4, value)

def getAIActionFlag(epd):
    return f_bread_epd(epd + 0x092 // 4, 0x092 % 4)

def setAIActionFlag(epd, value):
    f_bwrite_epd(epd + 0x092 // 4, 0x092 % 4, value)

def getUserActionFlags(epd):
    return f_bread_epd(epd + 0x093 // 4, 0x093 % 4)

def setUserActionFlags(epd, value):
    f_bwrite_epd(epd + 0x093 // 4, 0x093 % 4, value)

def getCurrentButtonSet(epd):
    return f_wwrite_epd(epd + 0x094 // 4, 0x094 % 4, value)

def setCurrentButtonSet(epd, value):
    f_wwrite_epd(0x094 // 4, 0x094 % 4, value)

def getIsCloaked(epd):
    return f_boolread_epd(epd + 0x096 // 4, 0x096 % 4)

def setIsCloaked(epd, value):
    f_boolwrite_epd(epd + 0x096 // 4, 0x096 % 4, value)

def getMovementState(epd):
    return f_UnitMovementStateread_epd(epd + 0x097 // 4, 0x097 % 4)

def setMovementState(epd, value):
    f_UnitMovementStatewrite_epd(epd + 0x097 // 4, 0x097 % 4, value)

def getBuildQueue_1(epd):
    return f_wread_epd(epd + 0x098 // 4, 0x098 % 4)

def setBuildQueue_1(epd, value):
    f_wwrite_epd(epd + 0x098 // 4, 0x098 % 4, value)

def getBuildQueue_2(epd):
    return f_wread_epd(epd + 0x09A // 4, 0x09A % 4)

def setBuildQueue_2(epd, value):
    f_wwrite_epd(epd + 0x09A // 4, 0x09A % 4, value)

def getBuildQueue_3(epd):
    return f_wread_epd(epd + 0x09C // 4, 0x09C % 4)

def setBuildQueue_3(epd, value):
    f_wwrite_epd(epd + 0x09C // 4, 0x09C % 4, value)

def getBuildQueue_4(epd):
    return f_wread_epd(epd + 0x09E // 4, 0x09E % 4)

def setBuildQueue_4(epd, value):
    f_wwrite_epd(epd + 0x09E // 4, 0x09E % 4, value)

def getBuildQueue_5(epd):
    return f_wread_epd(epd + 0x0A0 // 4, 0x0A0 % 4)

def setBuildQueue_5(epd, value):
    f_wwrite_epd(epd + 0x0A0 // 4, 0x0A0 % 4, value)

def getEnergy(epd):
    return f_wread_epd(epd + 0x0A2 // 4, 0x0A2 % 4)

def setEnergy(epd, value):
    f_wwrite_epd(epd + 0x0A2 // 4, 0x0A2 % 4, value)

def getBuildQueueSlot(epd):
    return f_bread_epd(epd + 0x0A4 // 4, 0x0A4 % 4)

def setBuildQueueSlot(epd, value):
    f_bwrite_epd(epd + 0x0A4 // 4, 0x0A4 % 4, value)

def getUniquenessIdentifier(epd):
    return f_bread_epd(epd + 0x0A5 // 4, 0x0A5 % 4)

def setUniquenessIdentifier(epd, value):
    f_bwrite_epd(epd + 0x0A5 // 4, 0x0A5 % 4, value)

def getSecondaryOrderID(epd):
    return f_bread_epd(epd + 0x0A6 // 4, 0x0A6 % 4)

def setSecondaryOrderID(epd, value):
    f_bwrite_epd(epd + 0x0A6 // 4, 0x0A6 % 4, value)

def getBuildingOverlayState(epd):
    return f_bread_epd(epd + 0x0A7 // 4, 0x0A7 % 4)

def setBuildingOverlayState(epd, value):
    f_bwrite_epd(epd + 0x0A7 // 4, 0x0A7 % 4, value)

def getHpGain(epd):
    return f_wread_epd(epd + 0x0A8 // 4, 0x0A8 % 4)

def setHpGain(epd, value):
    f_wwrite_epd(epd + 0x0A8 // 4, 0x0A8 % 4, value)

def getShieldGain(epd):
    return f_wread_epd(epd + 0x0AA // 4, 0x0AA % 4)

def setShieldGain(epd, value):
    f_wwrite_epd(epd + 0x0AA // 4, 0x0AA % 4, value)

def getRemainingBuildTime(epd):
    return f_wread_epd(epd + 0x0AC // 4, 0x0AC % 4)

def setRemainingBuildTime(epd, value):
    f_wwrite_epd(epd + 0x0AC // 4, 0x0AC % 4, value)

def getPreviousHP(epd):
    return f_wread_epd(epd + 0x0AE // 4, 0x0AE % 4)

def setPreviousHP(epd, value):
    f_wwrite_epd(epd + 0x0AE // 4, 0x0AE % 4, value)

def getLoadedUnitIndex_1(epd):
    return f_wread_epd(epd + 0x0B0 // 4, 0x0B0 % 4)

def setLoadedUnitIndex_1(epd, value):
    f_wwrite_epd(epd + 0x0B0 // 4, 0x0B0 % 4, value)

def getLoadedUnitIndex_2(epd):
    return f_wread_epd(epd + 0x0B2 // 4, 0x0B2 % 4)

def setLoadedUnitIndex_2(epd, value):
    f_wwrite_epd(epd + 0x0B2 // 4, 0x0B2 % 4, value)

def getLoadedUnitIndex_3(epd):
    return f_wread_epd(epd + 0x0B4 // 4, 0x0B4 % 4)

def setLoadedUnitIndex_3(epd, value):
    f_wwrite_epd(epd + 0x0B4 // 4, 0x0B4 % 4, value)

def getLoadedUnitIndex_4(epd):
    return f_wread_epd(epd + 0x0B6 // 4, 0x0B6 % 4)

def setLoadedUnitIndex_4(epd, value):
    f_wwrite_epd(epd + 0x0B6 // 4, 0x0B6 % 4, value)

def getLoadedUnitIndex_5(epd):
    return f_wread_epd(epd + 0x0B8 // 4, 0x0B8 % 4)

def setLoadedUnitIndex_5(epd, value):
    f_wwrite_epd(epd + 0x0B8 // 4, 0x0B8 % 4, value)

def getLoadedUnitIndex_6(epd):
    return f_wread_epd(epd + 0x0BA // 4, 0x0BA % 4)

def setLoadedUnitIndex_6(epd, value):
    f_wwrite_epd(epd + 0x0BA // 4, 0x0BA % 4, value)

def getLoadedUnitIndex_7(epd):
    return f_wread_epd(epd + 0x0BC // 4, 0x0BC % 4)

def setLoadedUnitIndex_7(epd, value):
    f_wwrite_epd(epd + 0x0BC // 4, 0x0BC % 4, value)

def getLoadedUnitIndex_8(epd):
    return f_wread_epd(epd + 0x0BE // 4, 0x0BE % 4)

def setLoadedUnitIndex_8(epd, value):
    f_wwrite_epd(epd + 0x0BE // 4, 0x0BE % 4, value)

def getVULTURE:spiderMineCount(epd):
    return f_bread_epd(epd + 0x0C0 // 4, 0x0C0 % 4)

def setVULTURE:spiderMineCount(epd, value):
    f_bwrite_epd(epd + 0x0C0 // 4, 0x0C0 % 4, value)

def getCARRIER_pInHanger(epd):
    return f_dwread_epd(epd + 0x0C0 // 4, 0x0C0 % 4)

def setCARRIER_pInHanger(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value, value)

def getCARRIER_pOutHanger(epd):
    return f_dwread_epd(epd + 0x0C4 // 4, 0x0C4 % 4)

def setCARRIER_pOutHanger(epd, value):
    f_dwwrite_epd(epd, 0x0C4, value, value)

def getCARRIER_inHangerCount(epd):
    return f_bread_epd(epd + 0x0C8 // 4, 0x0C8 % 4)

def setCARRIER_inHangerCount(epd, value):
    f_bwrite_epd(epd + 0x0C8 // 4, 0x0C8 % 4, value)

def getCARRIER_outHangerCount(epd):
    return f_bread_epd(epd + 0x0C9 // 4, 0x0C9 % 4)

def setCARRIER_outHangerCount(epd, value):
    f_bwrite_epd(epd + 0x0C9 // 4, 0x0C9 % 4, value)

def getFIGHTER_parent(epd):
    return f_dwread_epd(epd + 0x0C0 // 4, 0x0C0 % 4)

def setFIGHTER_parent(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value, value)

def getFIGHTER_prev(epd):
    return f_dwread_epd(epd + 0x0C4 // 4, 0x0C4 % 4)

def setFIGHTER_prev(epd, value):
    f_dwwrite_epd(epd, 0x0C4, value, value)

def getFIGHTER_next(epd):
    return f_dwread_epd(epd + 0x0C8 // 4, 0x0C8 % 4)

def setFIGHTER_next(epd, value):
    f_dwwrite_epd(epd, 0x0C8, value, value)

def getFIGHTER_inHanger(epd):
    return f_boolread_epd(epd + 0x0CC // 4, 0x0CC % 4)

def setFIGHTER_inHanger(epd, value):
    f_boolwrite_epd(epd + 0x0CC // 4, 0x0CC % 4, value)

def getBEACON__unknown_00(epd):
    return f_dwread_epd(epd + 0x0C0 // 4, 0x0C0 % 4)

def setBEACON__unknown_00(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value, value)

def getBEACON__unknown_04(epd):
    return f_dwread_epd(epd + 0x0C4 // 4, 0x0C4 % 4)

def setBEACON__unknown_04(epd, value):
    f_dwwrite_epd(epd, 0x0C4, value, value)

def getBEACON_flagSpawnFrame(epd):
    return f_dwread_epd(epd + 0x0C8 // 4, 0x0C8 % 4)

def setBEACON_flagSpawnFrame(epd, value):
    f_dwwrite_epd(epd, 0x0C8, value, value)

def getBUILDING_addon(epd):
    return f_dwread_epd(epd + 0x0C0 // 4, 0x0C0 % 4)

def setBUILDING_addon(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value, value)

def getBUILDING_addonBuildType(epd):
    return f_wread_epd(epd + 0x0C4 // 4, 0x0C4 % 4)

def setBUILDING_addonBuildType(epd, value):
    f_wwrite_epd(epd + 0x0C4 // 4, 0x0C4 % 4, value)

def getBUILDING_upgradeResearchTime(epd):
    return f_wread_epd(epd + 0x0C6 // 4, 0x0C6 % 4)

def setBUILDING_upgradeResearchTime(epd, value):
    f_wwrite_epd(epd + 0x0C6 // 4, 0x0C6 % 4, value)

def getBUILDING_techType(epd):
    return f_bread_epd(epd + 0x0C8 // 4, 0x0C8 % 4)

def setBUILDING_techType(epd, value):
    f_bwrite_epd(epd + 0x0C8 // 4, 0x0C8 % 4, value)

def getBUILDING_upgradeType(epd):
    return f_bread_epd(epd + 0x0C9 // 4, 0x0C9 % 4)

def setBUILDING_upgradeType(epd, value):
    f_bwrite_epd(epd + 0x0C9 // 4, 0x0C9 % 4, value)

def getBUILDING_larvaTimer(epd):
    return f_bread_epd(epd + 0x0CA // 4, 0x0CA % 4)

def setBUILDING_larvaTimer(epd, value):
    f_bwrite_epd(epd + 0x0CA // 4, 0x0CA % 4, value)

def getBUILDING_landingTimer(epd):
    return f_bread_epd(epd + 0x0CB // 4, 0x0CB % 4)

def setBUILDING_landingTimer(epd, value):
    f_bwrite_epd(epd + 0x0CB // 4, 0x0CB % 4, value)

def getBUILDING_creepTimer(epd):
    return f_bread_epd(epd + 0x0CC // 4, 0x0CC % 4)

def setBUILDING_creepTimer(epd, value):
    f_bwrite_epd(epd + 0x0CC // 4, 0x0CC % 4, value)

def getBUILDING_upgradeLevel(epd):
    return f_bread_epd(epd + 0x0CD // 4, 0x0CD % 4)

def setBUILDING_upgradeLevel(epd, value):
    f_bwrite_epd(epd + 0x0CD // 4, 0x0CD % 4, value)

def getBUILDING___E(epd):
    return f_wread_epd(epd + 0x0CE // 4, 0x0CE % 4)

def setBUILDING___E(epd, value):
    f_wwrite_epd(epd + 0x0CE // 4, 0x0CE % 4, value)

def getWORKER_pPowerup(epd):
    return f_dwread_epd(epd + 0x0C0 // 4, 0x0C0 % 4)

def setWORKER_pPowerup(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value, value)

def getWORKER_targetResourceX(epd):
    return f_wread_epd(epd + 0x0C4 // 4, 0x0C4 % 4)

def setWORKER_targetResourceX(epdepd, value):
    f_wread_epd(epd + 0x0C4 // 4, 0x0C4 % 4)

def getWORKER_targetResourceY(epd):
    return f_wread_epd(epd + 0x0C6 // 4, 0x0C6 % 4)

def setWORKER_targetResourceY(epdepd, value):
    f_wread_epd(epd + 0x0C6 // 4, 0x0C6 % 4)

def getWORKER_targetResourceUnit(epd):
    return f_dwread_epd(epd + 0x0C8 // 4, 0x0C8 % 4)

def setWORKER_targetResourceUnit(epdepd, value):
    f_dwread_epd(epd + 0x0C8 // 4, 0x0C8 % 4)

def getWORKER_repairResourceLossTimer(epd):
    return f_wread_epd(epd + 0x0CC // 4, 0x0CC % 4)

def setWORKER_repairResourceLossTimer(epd, value):
    f_wwrite_epd(epd + 0x0CC // 4, 0x0CC % 4, value)

def getWORKER_isCarryingSomething(epd):
    return f_boolread_epd(epd + 0x0CE // 4, 0x0CE % 4)

def setWORKER_isCarryingSomething(epd, value):
    f_boolwrite_epd(epd + 0x0CE // 4, 0x0CE % 4, value)

def getWORKER_resourceCarryCount(epd):
    return f_bread_epd(epd + 0x0CF // 4, 0x0CF % 4)

def setWORKER_resourceCarryCount(epd, value):
    f_bwrite_epd(epd + 0x0CF // 4, 0x0CF % 4, value)

def getWORKER_harvestTarget(epd):
    return f_dwread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def setWORKER_harvestTarget(epdepd, value):
    f_dwread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def getWORKER_prevHarvestUnit(epd):
    return f_dwread_epd(epd + 0x0D4 // 4, 0x0D4 % 4)

def setWORKER_prevHarvestUnit(epd, value):
    f_dwwrite_epd(epd, 0x0D4, value, value)

def getWORKER_nextHarvestUnit(epd):
    return f_dwread_epd(epd + 0x0D8 // 4, 0x0D8 % 4)

def setWORKER_nextHarvestUnit(epd, value):
    f_dwwrite_epd(epd, 0x0D8, value, value)

def getBUILDING_RESOURCE_resourceCount(epd):
    return f_wread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def setBUILDING_RESOURCE_resourceCount(epd, value):
    f_wwrite_epd(epd + 0x0D0 // 4, 0x0D0 % 4, value)

def getBUILDING_RESOURCE_resourceIscript(epd):
    return f_bread_epd(epd + 0x0D2 // 4, 0x0D2 % 4)

def setBUILDING_RESOURCE_resourceIscript(epd, value):
    f_bwrite_epd(epd + 0x0D2 // 4, 0x0D2 % 4, value)

def getBUILDING_RESOURCE_gatherQueueCount(epd):
    return f_bread_epd(epd + 0x0D3 // 4, 0x0D3 % 4)

def setBUILDING_RESOURCE_gatherQueueCount(epd, value):
    f_bwrite_epd(epd + 0x0D3 // 4, 0x0D3 % 4, value)

def getBUILDING_RESOURCE_nextGatherer(epd):
    return f_dwread_epd(epd + 0x0D4 // 4, 0x0D4 % 4)

def setBUILDING_RESOURCE_nextGatherer(epd, value):
    f_dwwrite_epd(epd, 0x0D4, value, value)

def getBUILDING_RESOURCE_resourceGroup(epd):
    return f_bread_epd(epd + 0x0D8 // 4, 0x0D8 % 4)

def setBUILDING_RESOURCE_resourceGroup(epd, value):
    f_bwrite_epd(epd + 0x0D8 // 4, 0x0D8 % 4, value)

def getBUILDING_RESOURCE_resourceBelongsToAI(epd):
    return f_bread_epd(epd + 0x0D9 // 4, 0x0D9 % 4)

def setBUILDING_RESOURCE_resourceBelongsToAI(epd, value):
    f_bwrite_epd(epd + 0x0D9 // 4, 0x0D9 % 4, value)

def getBUILDING_NYDUS_exit(epd):
    return f_dwread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def setBUILDING_NYDUS_exit(epd, value):
    f_dwwrite_epd(epd, 0x0D0, value, value)

def getBUILDING_GHOST_nukeDot(epd):
    return f_dwread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def setBUILDING_GHOST_nukeDot(epd, value):
    f_dwwrite_epd(epd, 0x0D0, value, value)

def getBUILDING_PYLON_pPowerTemplate(epd):
    return f_dwread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def setBUILDING_PYLON_pPowerTemplate(epd, value):
    f_dwwrite_epd(epd, 0x0D0, value, value)

def getBUILDING_SILO_pNuke(epd):
    return f_dwread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def setBUILDING_SILO_pNuke(epd, value):
    f_dwwrite_epd(epd, 0x0D0, value, value)

def getBUILDING_SILO_bReady(epd):
    return f_boolread_epd(epd + 0x0D4 // 4, 0x0D4 % 4)

def setBUILDING_SILO_bReady(epd, value):
    f_boolwrite_epd(epd + 0x0D4 // 4, 0x0D4 % 4, value)

def getBUILDING_HATCHERY_harvestValueLeft(epd):
    return f_wread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def setBUILDING_HATCHERY_harvestValueLeft(epd, value):
    f_wwrite_epd(epd + 0x0D0 // 4, 0x0D0 % 4, value)

def getBUILDING_HATCHERY_harvestValueTop(epd):
    return f_wread_epd(epd + 0x0D2 // 4, 0x0D2 % 4)

def setBUILDING_HATCHERY_harvestValueTop(epd, value):
    f_wwrite_epd(epd + 0x0D2 // 4, 0x0D2 % 4, value)

def getBUILDING_HATCHERY_harvestValueRight(epd):
    return f_wread_epd(epd + 0x0D4 // 4, 0x0D4 % 4)

def setBUILDING_HATCHERY_harvestValueRight(epd, value):
    f_wwrite_epd(epd + 0x0D4 // 4, 0x0D4 % 4, value)

def getBUILDING_HATCHERY_harvestValueBottom(epd):
    return f_wread_epd(epd + 0x0D6 // 4, 0x0D6 % 4)

def setBUILDING_HATCHERY_harvestValueBottom(epd, value):
    f_wwrite_epd(epd + 0x0D6 // 4, 0x0D6 % 4, value)

def getBUILDING_POWERUP_originX(epd):
    return f_wread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def setBUILDING_POWERUP_originX(epd, value):
    f_wwrite_epd(epd + 0x0D0 // 4, 0x0D0 % 4, value)

def getBUILDING_POWERUP_originY(epd):
    return f_wread_epd(epd + 0x0D2 // 4, 0x0D2 % 4)

def setBUILDING_POWERUP_originY(epd, value):
    f_wwrite_epd(epd + 0x0D2 // 4, 0x0D2 % 4, value)

def getStatusFlags(epd):
    return f_statusFlagsread_epd(epd + 0x0DC // 4, 0x0DC % 4)

def setStatusFlags(epd, value):
    f_statusFlagswrite_epd(epd + 0x0DC // 4, 0x0DC % 4, value)

def getResourceType(epd):
    return f_bread_epd(epd + 0x0E0 // 4, 0x0E0 % 4)

def setResourceType(epd, value):
    f_bwrite_epd(epd + 0x0E0 // 4, 0x0E0 % 4, value)

def getWireframeRandomizer(epd):
    return f_bread_epd(epd + 0x0E1 // 4, 0x0E1 % 4)

def setWireframeRandomizer(epd, value):
    f_bwrite_epd(epd + 0x0E1 // 4, 0x0E1 % 4, value)

def getSecondaryOrderState(epd):
    return f_bread_epd(epd + 0x0E2 // 4, 0x0E2 % 4)

def setSecondaryOrderState(epd, value):
    f_bwrite_epd(epd + 0x0E2 // 4, 0x0E2 % 4, value)

def getRecentOrderTimer(epd):
    return f_bread_epd(epd + 0x0E3 // 4, 0x0E3 % 4)

def setRecentOrderTimer(epd, value):
    f_bwrite_epd(epd + 0x0E3 // 4, 0x0E3 % 4, value)

def getVisibilityStatus(epd):
    return f_dwread_epd(epd + 0x0E4 // 4, 0x0E4 % 4)

def setVisibilityStatus(epd, value):
    f_dwwrite_epd(epd, 0x0E4, value, value)

def getSecondaryOrderPositionX(epd):
    return f_wread_epd(epd + 0x0E8 // 4, 0x0E8 % 4)

def setSecondaryOrderPositionX(epd, value):
    f_wwrite_epd(epd + 0x0E8 // 4, 0x0E8 % 4, value)

def getSecondaryOrderPositionY(epd):
    return f_wread_epd(epd + 0x0EA // 4, 0x0EA % 4)

def setSecondaryOrderPositionY(epd, value):
    f_wwrite_epd(epd + 0x0EA // 4, 0x0EA % 4, value)

def getCurrentBuildUnit(epd):
    return f_dwread_epd(epd + 0x0EC // 4, 0x0EC % 4)

def setCurrentBuildUnit(epd, value):
    f_dwwrite_epd(epd, 0x0EC, value, value)

def getPreviousBurrowedUnit(epd):
    return f_dwread_epd(epd + 0x0F0 // 4, 0x0F0 % 4)

def setPreviousBurrowedUnit(epd, value):
    f_dwwrite_epd(epd, 0x0F0, value, value)

def getNextBurrowedUnit(epd):
    return f_dwread_epd(epd + 0x0F4 // 4, 0x0F4 % 4)

def setNextBurrowedUnit(epd, value):
    f_dwwrite_epd(epd, 0x0F4, value, value)

def getRALLY_positionX(epd):
    return f_wread_epd(epd + 0x0F8 // 4, 0x0F8 % 4)

def setRALLY_positionX(epd, value):
    f_wwrite_epd(epd + 0x0F8 // 4, 0x0F8 % 4, value)

def getRALLY_positionY(epd):
    return f_wread_epd(epd + 0x0FA // 4, 0x0FA % 4)

def setRALLY_positionY(epd, value):
    f_wwrite_epd(epd + 0x0FA // 4, 0x0FA % 4, value)

def getRALLY_unit(epd):
    return f_dwread_epd(epd + 0x0FC // 4, 0x0FC % 4)

def setRALLY_unit(epd, value):
    f_dwwrite_epd(epd, 0x0FC, value, value)

def getPYLON_prevPsiProvider(epd):
    return f_dwread_epd(epd + 0x0F8 // 4, 0x0F8 % 4)

def setPYLON_prevPsiProvider(epd, value):
    f_dwwrite_epd(epd, 0x0F8, value, value)

def getPYLON_nextPsiProvider(epd):
    return f_dwread_epd(epd + 0x0FC // 4, 0x0FC % 4)

def setPYLON_nextPsiProvider(epd, value):
    f_dwwrite_epd(epd, 0x0FC, value, value)

def getPath(epd):
    return f_dwread_epd(epd + 0x100 // 4, 0x100 % 4)

def setPath(epd, value):
    f_dwwrite_epd(epd, 0x100, value, value)

def getPathingCollisionInterval(epd):
    return f_bread_epd(epd + 0x104 // 4, 0x104 % 4)

def setPathingCollisionInterval(epd, value):
    f_bwrite_epd(epd + 0x104 // 4, 0x104 % 4, value)

def getPathingFlags(epd):
    return f_bread_epd(epd + 0x105 // 4, 0x105 % 4)

def setPathingFlags(epd, value):
    f_bwrite_epd(epd + 0x105 // 4, 0x105 % 4, value)

def get_unused_0x106(epd):
    return f_bread_epd(epd + 0x106 // 4, 0x106 % 4)

def set_unused_0x106(epd, value):
    f_bwrite_epd(epd + 0x106 // 4, 0x106 % 4, value)

def getIsBeingHealed(epd):
    return f_boolread_epd(epd + 0x107 // 4, 0x107 % 4)

def setIsBeingHealed(epd, value):
    f_boolwrite_epd(epd + 0x107 // 4, 0x107 % 4, value)

def getContourBoundsLeft(epd):
    return f_wread_epd(epd + 0x108 // 4, 0x108 % 4)

def setContourBoundsLeft(epd, value):
    f_wwrite_epd(epd + 0x108 // 4, 0x108 % 4, value)

def getContourBoundsTop(epd):
    return f_wread_epd(epd + 0x10A // 4, 0x10A % 4)

def setContourBoundsTop(epd, value):
    f_wwrite_epd(epd + 0x10A // 4, 0x10A % 4, value)

def getContourBoundsRight(epd):
    return f_wread_epd(epd + 0x10C // 4, 0x10C % 4)

def setContourBoundsRight(epd, value):
    f_wwrite_epd(epd + 0x10C // 4, 0x10C % 4, value)

def getContourBoundsBottom(epd):
    return f_wread_epd(epd + 0x10E // 4, 0x10E % 4)

def setContourBoundsBottom(epd, value):
    f_wwrite_epd(epd + 0x10E // 4, 0x10E % 4, value)

def getSTATUS_removeTimer(epd):
    return f_wread_epd(epd + 0x110 // 4, 0x110 % 4)

def setSTATUS_removeTimer(epd, value):
    f_wwrite_epd(epd + 0x110 // 4, 0x110 % 4, value)

def getSTATUS_defenseMatrixDamage(epd):
    return f_wread_epd(epd + 0x112 // 4, 0x112 % 4)

def setSTATUS_defenseMatrixDamage(epd, value):
    f_wwrite_epd(epd + 0x112 // 4, 0x112 % 4, value)

def getSTATUS_defenseMatrixTimer(epd):
    return f_bread_epd(epd + 0x114 // 4, 0x114 % 4)

def setSTATUS_defenseMatrixTimer(epd, value):
    f_bwrite_epd(epd + 0x114 // 4, 0x114 % 4, value)

def getSTATUS_stimTimer(epd):
    return f_bread_epd(epd + 0x115 // 4, 0x115 % 4)

def setSTATUS_stimTimer(epd, value):
    f_bwrite_epd(epd + 0x115 // 4, 0x115 % 4, value)

def getSTATUS_ensnareTimer(epd):
    return f_bread_epd(epd + 0x116 // 4, 0x116 % 4)

def setSTATUS_ensnareTimer(epd, value):
    f_bwrite_epd(epd + 0x116 // 4, 0x116 % 4, value)

def getSTATUS_lockdownTimer(epd):
    return f_bread_epd(epd + 0x117 // 4, 0x117 % 4)

def setSTATUS_lockdownTimer(epd, value):
    f_bwrite_epd(epd + 0x117 // 4, 0x117 % 4, value)

def getSTATUS_irradiateTimer(epd):
    return f_bread_epd(epd + 0x118 // 4, 0x118 % 4)

def setSTATUS_irradiateTimer(epd, value):
    f_bwrite_epd(epd + 0x118 // 4, 0x118 % 4, value)

def getSTATUS_stasisTimer(epd):
    return f_bread_epd(epd + 0x119 // 4, 0x119 % 4)

def setSTATUS_stasisTimer(epd, value):
    f_bwrite_epd(epd + 0x119 // 4, 0x119 % 4, value)

def getSTATUS_plagueTimer(epd):
    return f_bread_epd(epd + 0x11A // 4, 0x11A % 4)

def setSTATUS_plagueTimer(epd, value):
    f_bwrite_epd(epd + 0x11A // 4, 0x11A % 4, value)

def getSTATUS_stormTimer(epd):
    return f_bread_epd(epd + 0x11B // 4, 0x11B % 4)

def setSTATUS_stormTimer(epd, value):
    f_bwrite_epd(epd + 0x11B // 4, 0x11B % 4, value)

def getSTATUS_irradiatedBy(epd):
    return f_dwread_epd(epd + 0x11C // 4, 0x11C % 4)

def setSTATUS_irradiatedBy(epd, value):
    f_dwwrite_epd(epd, 0x11C, value, value)

def getSTATUS_irradiatePlayerID(epd):
    return f_bread_epd(epd + 0x120 // 4, 0x120 % 4)

def setSTATUS_irradiatePlayerID(epd, value):
    f_bwrite_epd(epd + 0x120 // 4, 0x120 % 4, value)

def getSTATUS_parasiteFlags(epd):
    return f_bread_epd(epd + 0x121 // 4, 0x121 % 4)

def setSTATUS_parasiteFlags(epd, value):
    f_bwrite_epd(epd + 0x121 // 4, 0x121 % 4, value)

def getSTATUS_cycleCounter(epd):
    return f_bread_epd(epd + 0x122 // 4, 0x122 % 4)

def setSTATUS_cycleCounter(epd, value):
    f_bwrite_epd(epd + 0x122 // 4, 0x122 % 4, value)

def getSTATUS_isBlind(epd):
    return f_boolread_epd(epd + 0x123 // 4, 0x123 % 4)

def setSTATUS_isBlind(epd, value):
    f_boolwrite_epd(epd + 0x123 // 4, 0x123 % 4, value)

def getSTATUS_maelstromTimer(epd):
    return f_bread_epd(epd + 0x124 // 4, 0x124 % 4)

def setSTATUS_maelstromTimer(epd, value):
    f_bwrite_epd(epd + 0x124 // 4, 0x124 % 4, value)

def getSTATUS__unused_0x125(epd):
    return f_bread_epd(epd + 0x125 // 4, 0x125 % 4)

def setSTATUS__unused_0x125(epd, value):
    f_bwrite_epd(epd + 0x125 // 4, 0x125 % 4, value)

def getSTATUS_acidSporeCount(epd):
    return f_bread_epd(epd + 0x126 // 4, 0x126 % 4)

def setSTATUS_acidSporeCount(epd, value):
    f_bwrite_epd(epd + 0x126 // 4, 0x126 % 4, value)

def getSTATUS_acidSporeTime_1(epd):
    return f_bread_epd(epd + 0x127 // 4, 0x127 % 4)

def setSTATUS_acidSporeTime_1(epd, value):
    f_bwrite_epd(epd + 0x127 // 4, 0x127 % 4, value)

def getSTATUS_acidSporeTime_2(epd):
    return f_bread_epd(epd + 0x128 // 4, 0x128 % 4)

def setSTATUS_acidSporeTime_2(epd, value):
    f_bwrite_epd(epd + 0x128 // 4, 0x128 % 4, value)

def getSTATUS_acidSporeTime_3(epd):
    return f_bread_epd(epd + 0x129 // 4, 0x129 % 4)

def setSTATUS_acidSporeTime_3(epd, value):
    f_bwrite_epd(epd + 0x129 // 4, 0x129 % 4, value)

def getSTATUS_acidSporeTime_4(epd):
    return f_bread_epd(epd + 0x12A // 4, 0x12A % 4)

def setSTATUS_acidSporeTime_4(epd, value):
    f_bwrite_epd(epd + 0x12A // 4, 0x12A % 4, value)

def getSTATUS_acidSporeTime_5(epd):
    return f_bread_epd(epd + 0x12B // 4, 0x12B % 4)

def setSTATUS_acidSporeTime_5(epd, value):
    f_bwrite_epd(epd + 0x12B // 4, 0x12B % 4, value)

def getSTATUS_acidSporeTime_6(epd):
    return f_bread_epd(epd + 0x12C // 4, 0x12C % 4)

def setSTATUS_acidSporeTime_6(epd, value):
    f_bwrite_epd(epd + 0x12C // 4, 0x12C % 4, value)

def getSTATUS_acidSporeTime_7(epd):
    return f_bread_epd(epd + 0x12D // 4, 0x12D % 4)

def setSTATUS_acidSporeTime_7(epd, value):
    f_bwrite_epd(epd + 0x12D // 4, 0x12D % 4, value)

def getSTATUS_acidSporeTime_8(epd):
    return f_bread_epd(epd + 0x12E // 4, 0x12E % 4)

def setSTATUS_acidSporeTime_8(epd, value):
    f_bwrite_epd(epd + 0x12E // 4, 0x12E % 4, value)

def getSTATUS_acidSporeTime_9(epd):
    return f_bread_epd(epd + 0x12F // 4, 0x12F % 4)

def setSTATUS_acidSporeTime_9(epd, value):
    f_bwrite_epd(epd + 0x12F // 4, 0x12F % 4, value)

def getSTATUS_bulletBehaviour3by3AttackSequence(epd):
    return f_wread_epd(epd + 0x130 // 4, 0x130 % 4)

def setSTATUS_bulletBehaviour3by3AttackSequence(epd, value):
    f_wwrite_epd(epd + 0x130 // 4, 0x130 % 4, value)

def get_padding_0x132(epd):
    return f_wread_epd(epd + 0x132 // 4, 0x132 % 4)

def set_padding_0x132(epd, value):
    f_wwrite_epd(epd + 0x132 // 4, 0x132 % 4, value)

def getPAI(epd):
    return f_dwread_epd(epd + 0x134 // 4, 0x134 % 4)

def setPAI(epd, value):
    f_dwwrite_epd(epd, 0x134, value, value)

def getAirStrength(epd):
    return f_wread_epd(epd + 0x138 // 4, 0x138 % 4)

def setAirStrength(epd, value):
    f_wwrite_epd(epd + 0x138 // 4, 0x138 % 4, value)

def getGroundStrength(epd):
    return f_wread_epd(epd + 0x13A // 4, 0x13A % 4)

def setGroundStrength(epd, value):
    f_wwrite_epd(epd + 0x13A // 4, 0x13A % 4, value)

def getFINDER_Left(epd):
    return f_bread_epd(epd + 0x13C // 4, 0x13C % 4)

def setFINDER_Left(epd, value):
    f_bwrite_epd(epd + 0x13C // 4, 0x13C % 4, value)

def getFINDER_Right(epd):
    return f_bread_epd(epd + 0x140 // 4, 0x140 % 4)

def setFINDER_Right(epd, value):
    f_bwrite_epd(epd + 0x140 // 4, 0x140 % 4, value)

def getFINDER_Top(epd):
    return f_bread_epd(epd + 0x144 // 4, 0x144 % 4)

def setFINDER_Top(epd, value):
    f_bwrite_epd(epd + 0x144 // 4, 0x144 % 4, value)

def getFINDER_Bottom(epd):
    return f_bread_epd(epd + 0x148 // 4, 0x148 % 4)

def setFINDER_Bottom(epd, value):
    f_bwrite_epd(epd + 0x148 // 4, 0x148 % 4, value)

def getRepulseUnknown(epd):
    return f_bread_epd(epd + 0x14C // 4, 0x14C % 4)

def setRepulseUnknown(epd, value):
    f_bwrite_epd(epd + 0x14C // 4, 0x14C % 4, value)

def getRepulseAngle(epd):
    return f_bread_epd(epd + 0x14D // 4, 0x14D % 4)

def setRepulseAngle(epd, value):
    f_bwrite_epd(epd + 0x14D // 4, 0x14D % 4, value)

def getBRepMtxX(epd):
    return f_bread_epd(epd + 0x14E // 4, 0x14E % 4)

def setBRepMtxX(epd, value):
    f_bwrite_epd(epd + 0x14E // 4, 0x14E % 4, value)

def getBRepMtxY(epd):
    return f_bread_epd(epd + 0x14F // 4, 0x14F % 4)

def setBRepMtxY(epd, value):
    f_bwrite_epd(epd + 0x14F // 4, 0x14F % 4, value)
"""