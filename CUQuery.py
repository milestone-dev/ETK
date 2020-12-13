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

# AUTO GENEREATED FUNCTIONS

def f_getPrev(epd):
    return f_dwread_epd(epd + 0x000 // 4)

def f_setPrev(epd, value):
    f_dwwrite_epd(epd, 0x000, value)

def f_getNext(epd):
    return f_dwread_epd(epd + 0x004 // 4)

def f_setNext(epd, value):
    f_dwwrite_epd(epd, 0x004, value)

def f_getHitPoints(epd):
    return f_dwread_epd(epd + 0x008 // 4)

def f_setHitPoints(epd, value):
    f_dwwrite_epd(epd, 0x008, value)

def f_getSprite(epd):
    return f_dwread_epd(epd + 0x00C // 4)

def f_setSprite(epd, value):
    f_dwwrite_epd(epd, 0x00C, value)

def f_getMoveTargetX(epd):
    return f_wread_epd(epd + 0x010 // 4, 0x010 % 4)

def f_setMoveTargetX(epdepd, value):
    f_wread_epd(epd + 0x010 // 4, 0x010 % 4)

def f_getMoveTargetY(epd):
    return f_wread_epd(epd + 0x012 // 4, 0x012 % 4)

def f_setMoveTargetY(epdepd, value):
    f_wread_epd(epd + 0x012 // 4, 0x012 % 4)

def f_getMoveTargetUnit(epd):
    return f_dwread_epd(epd + 0x014 // 4)

def f_setMoveTargetUnit(epdepd, value):
    f_dwread_epd(epd + 0x014 // 4)

def f_getNextMovementWaypointX(epd):
    return f_wread_epd(epd + 0x018 // 4, 0x018 % 4)

def f_setNextMovementWaypointX(epd, value):
    f_wwrite_epd(epd + 0x018 // 4, 0x018 % 4, value)

def f_getNextMovementWaypointY(epd):
    return f_wread_epd(epd + 0x01A // 4, 0x01A % 4)

def f_setNextMovementWaypointY(epd, value):
    f_wwrite_epd(epd + 0x01A // 4, 0x01A % 4, value)

def f_getNextTargetWaypointX(epd):
    return f_wread_epd(epd + 0x01C // 4, 0x01C % 4)

def f_setNextTargetWaypointX(epdepd, value):
    f_wread_epd(epd + 0x01C // 4, 0x01C % 4)

def f_getNextTargetWaypointY(epd):
    return f_wread_epd(epd + 0x01E // 4, 0x01E % 4)

def f_setNextTargetWaypointY(epdepd, value):
    f_wread_epd(epd + 0x01E // 4, 0x01E % 4)

def f_getMovementFlags(epd):
    return f_bread_epd(epd + 0x020 // 4, 0x020 % 4)

def f_setMovementFlags(epd, value):
    f_bwrite_epd(epd + 0x020 // 4, 0x020 % 4, value)

def f_getCurrentDirection1(epd):
    return f_bread_epd(epd + 0x021 // 4, 0x021 % 4)

def f_setCurrentDirection1(epd, value):
    f_bwrite_epd(epd + 0x021 // 4, 0x021 % 4, value)

def f_getFlingyTurnRadius(epd):
    return f_bread_epd(epd + 0x022 // 4, 0x022 % 4)

def f_setFlingyTurnRadius(epd, value):
    f_bwrite_epd(epd + 0x022 // 4, 0x022 % 4, value)

def f_getVelocityDirection1(epd):
    return f_bread_epd(epd + 0x023 // 4, 0x023 % 4)

def f_setVelocityDirection1(epd, value):
    f_bwrite_epd(epd + 0x023 // 4, 0x023 % 4, value)

def f_getFlingyID(epd):
    return f_wread_epd(epd + 0x024 // 4, 0x024 % 4)

def f_setFlingyID(epd, value):
    f_wwrite_epd(epd + 0x024 // 4, 0x024 % 4, value)

def f_getUnknown_0x026(epd):
    return f_bread_epd(epd + 0x026 // 4, 0x026 % 4)

def f_set_unknown_0x026(epd, value):
    f_bwrite_epd(epd + 0x026 // 4, 0x026 % 4, value)

def f_getFlingyMovementType(epd):
    return f_bread_epd(epd + 0x027 // 4, 0x027 % 4)

def f_setFlingyMovementType(epd, value):
    f_bwrite_epd(epd + 0x027 // 4, 0x027 % 4, value)

def f_getPositionX(epd):
    return f_wread_epd(epd + 0x028 // 4, 0x028 % 4)

def f_setPositionX(epd, value):
    f_wwrite_epd(epd + 0x028 // 4, 0x028 % 4, value)

def f_getPositionY(epd):
    return f_wread_epd(epd + 0x02A // 4, 0x02A % 4)

def f_setPositionY(epd, value):
    f_wwrite_epd(epd + 0x02A // 4, 0x02A % 4, value)

def f_getHaltX(epd):
    return f_dwread_epd(epd + 0x02C // 4)

def f_setHaltX(epd, value):
    f_dwwrite_epd(epd, 0x02C, value)

def f_getHaltY(epd):
    return f_dwread_epd(epd + 0x030 // 4)

def f_setHaltY(epd, value):
    f_dwwrite_epd(epd, 0x030, value)

def f_getFlingyTopSpeed(epd):
    return f_dwread_epd(epd + 0x034 // 4)

def f_setFlingyTopSpeed(epd, value):
    f_dwwrite_epd(epd, 0x034, value)

def f_getCurrent_speed1(epd):
    return f_dwread_epd(epd + 0x038 // 4)

def f_setCurrent_speed1(epd, value):
    f_dwwrite_epd(epd, 0x038, value)

def f_getCurrent_speed2(epd):
    return f_dwread_epd(epd + 0x03C // 4)

def f_setCurrent_speed2(epd, value):
    f_dwwrite_epd(epd, 0x03C, value)

def f_getCurrent_speedX(epd):
    return f_dwread_epd(epd + 0x040 // 4)

def f_setCurrent_speedX(epd, value):
    f_dwwrite_epd(epd, 0x040, value)

def f_getCurrent_speedY(epd):
    return f_dwread_epd(epd + 0x044 // 4)

def f_setCurrent_speedY(epd, value):
    f_dwwrite_epd(epd, 0x044, value)

def f_getFlingyAcceleration(epd):
    return f_wread_epd(epd + 0x048 // 4, 0x048 % 4)

def f_setFlingyAcceleration(epd, value):
    f_wwrite_epd(epd + 0x048 // 4, 0x048 % 4, value)

def f_getCurrentDirection2(epd):
    return f_bread_epd(epd + 0x04A // 4, 0x04A % 4)

def f_setCurrentDirection2(epd, value):
    f_bwrite_epd(epd + 0x04A // 4, 0x04A % 4, value)

def f_getVelocityDirection2(epd):
    return f_bread_epd(epd + 0x04B // 4, 0x04B % 4)

def f_setVelocityDirection2(epd, value):
    f_bwrite_epd(epd + 0x04B // 4, 0x04B % 4, value)

def f_getPlayerID(epd):
    return f_bread_epd(epd + 0x04C // 4, 0x04C % 4)

def f_setPlayerID(epd, value):
    f_bwrite_epd(epd + 0x04C // 4, 0x04C % 4, value)

def f_getOrderID(epd):
    return f_bread_epd(epd + 0x04D // 4, 0x04D % 4)

def f_setOrderID(epd, value):
    f_bwrite_epd(epd + 0x04D // 4, 0x04D % 4, value)

def f_getOrderState(epd):
    return f_bread_epd(epd + 0x04E // 4, 0x04E % 4)

def f_setOrderState(epd, value):
    f_bwrite_epd(epd + 0x04E // 4, 0x04E % 4, value)

def f_getOrderSignal(epd):
    return f_bread_epd(epd + 0x04F // 4, 0x04F % 4)

def f_setOrderSignal(epd, value):
    f_bwrite_epd(epd + 0x04F // 4, 0x04F % 4, value)

def f_getOrderUnitType(epd):
    return f_wread_epd(epd + 0x050 // 4, 0x050 % 4)

def f_setOrderUnitType(epd, value):
    f_wwrite_epd(epd + 0x050 // 4, 0x050 % 4, value)

def f_get52Flag(epd):
    return f_wread_epd(epd + 0x052 // 4, 0x052 % 4)

def f_set52Flag(epd, value):
    f_wwrite_epd(epd + 0x052 // 4, 0x052 % 4, value)

def f_getMainOrderTimer(epd):
    return f_bread_epd(epd + 0x054 // 4, 0x054 % 4)

def f_setMainOrderTimer(epd, value):
    f_bwrite_epd(epd + 0x054 // 4, 0x054 % 4, value)

def f_getGroundWeaponCooldown(epd):
    return f_bread_epd(epd + 0x055 // 4, 0x055 % 4)

def f_setGroundWeaponCooldown(epd, value):
    f_bwrite_epd(epd + 0x055 // 4, 0x055 % 4, value)

def f_getAirWeaponCooldown(epd):
    return f_bread_epd(epd + 0x056 // 4, 0x056 % 4)

def f_setAirWeaponCooldown(epd, value):
    f_bwrite_epd(epd + 0x056 // 4, 0x056 % 4, value)

def f_getSpellCooldown(epd):
    return f_bread_epd(epd + 0x057 // 4, 0x057 % 4)

def f_setSpellCooldown(epd, value):
    f_bwrite_epd(epd + 0x057 // 4, 0x057 % 4, value)

def f_getOrderTargetX(epd):
    return f_wread_epd(epd + 0x058 // 4, 0x058 % 4)

def f_setOrderTargetX(epdepd, value):
    f_wread_epd(epd + 0x058 // 4, 0x058 % 4)

def f_getOrderTargetY(epd):
    return f_wread_epd(epd + 0x05A // 4, 0x05A % 4)

def f_setOrderTargetY(epdepd, value):
    f_wread_epd(epd + 0x05A // 4, 0x05A % 4)

def f_getOrderTargetUnit(epd):
    return f_dwread_epd(epd + 0x05C // 4)

def f_setOrderTargetUnit(epdepd, value):
    f_dwread_epd(epd + 0x05C // 4)

def f_getShieldPoints(epd):
    return f_dwread_epd(epd + 0x060 // 4)

def f_setShieldPoints(epd, value):
    f_dwwrite_epd(epd, 0x060, value)

def f_getUnitType(epd):
    return f_wread_epd(epd + 0x064 // 4, 0x064 % 4)

def f_setUnitType(epd, value):
    f_wwrite_epd(epd + 0x064 // 4, 0x064 % 4, value)

def f_get66Flag(epd):
    return f_wread_epd(epd + 0x066 // 4, 0x066 % 4)

def f_set66Flag(epd, value):
    f_wwrite_epd(epd + 0x066 // 4, 0x066 % 4, value)

def f_getPreviousPlayerUnit(epd):
    return f_dwread_epd(epd + 0x068 // 4)

def f_setPreviousPlayerUnit(epd, value):
    f_dwwrite_epd(epd, 0x068, value)

def f_getNextPlayerUnit(epd):
    return f_dwread_epd(epd + 0x06C // 4)

def f_setNextPlayerUnit(epd, value):
    f_dwwrite_epd(epd, 0x06C, value)

def f_getSubUnit(epd):
    return f_dwread_epd(epd + 0x070 // 4)

def f_setSubUnit(epd, value):
    f_dwwrite_epd(epd, 0x070, value)

def f_getOrderQueueHead(epd):
    return f_dwread_epd(epd + 0x074 // 4)

def f_setOrderQueueHead(epd, value):
    f_dwwrite_epd(epd, 0x074, value)

def f_getOrderQueueTail(epd):
    return f_dwread_epd(epd + 0x078 // 4)

def f_setOrderQueueTail(epd, value):
    f_dwwrite_epd(epd, 0x078, value)

def f_getAutoTargetUnit(epd):
    return f_dwread_epd(epd + 0x07C // 4)

def f_setAutoTargetUnit(epdepd, value):
    f_dwread_epd(epd + 0x07C // 4)

def f_getConnectedUnit(epd):
    return f_dwread_epd(epd + 0x080 // 4)

def f_setConnectedUnit(epd, value):
    f_dwwrite_epd(epd, 0x080, value)

def f_getOrderQueueCount(epd):
    return f_bread_epd(epd + 0x084 // 4, 0x084 % 4)

def f_setOrderQueueCount(epd, value):
    f_bwrite_epd(epd + 0x084 // 4, 0x084 % 4, value)

def f_getOrderQueueTimer(epd):
    return f_bread_epd(epd + 0x085 // 4, 0x085 % 4)

def f_setOrderQueueTimer(epd, value):
    f_bwrite_epd(epd + 0x085 // 4, 0x085 % 4, value)

def f_getUnknown_0x086(epd):
    return f_bread_epd(epd + 0x086 // 4, 0x086 % 4)

def f_set_unknown_0x086(epd, value):
    f_bwrite_epd(epd + 0x086 // 4, 0x086 % 4, value)

def f_getAttackNotifyTimer(epd):
    return f_bread_epd(epd + 0x087 // 4, 0x087 % 4)

def f_setAttackNotifyTimer(epd, value):
    f_bwrite_epd(epd + 0x087 // 4, 0x087 % 4, value)

def f_getPreviousUnitType(epd):
    return f_wread_epd(epd + 0x088 // 4, 0x088 % 4)

def f_setPreviousUnitType(epd, value):
    f_wwrite_epd(epd + 0x088 // 4, 0x088 % 4, value)

def f_getLastEventTimer(epd):
    return f_bread_epd(epd + 0x08A // 4, 0x08A % 4)

def f_setLastEventTimer(epd, value):
    f_bwrite_epd(epd + 0x08A // 4, 0x08A % 4, value)

def f_getLastEventColor(epd):
    return f_bread_epd(epd + 0x08B // 4, 0x08B % 4)

def f_setLastEventColor(epd, value):
    f_bwrite_epd(epd + 0x08B // 4, 0x08B % 4, value)

def f_getUnused_0x08C(epd):
    return f_wread_epd(epd + 0x08C // 4, 0x08C % 4)

def f_set_unused_0x08C(epd, value):
    f_wwrite_epd(epd + 0x08C // 4, 0x08C % 4, value)

def f_getRankIncrease(epd):
    return f_bread_epd(epd + 0x08E // 4, 0x08E % 4)

def f_setRankIncrease(epd, value):
    f_bwrite_epd(epd + 0x08E // 4, 0x08E % 4, value)

def f_getKillCount(epd):
    return f_bread_epd(epd + 0x08F // 4, 0x08F % 4)

def f_setKillCount(epd, value):
    f_bwrite_epd(epd + 0x08F // 4, 0x08F % 4, value)

def f_getLastAttackingPlayer(epd):
    return f_bread_epd(epd + 0x090 // 4, 0x090 % 4)

def f_setLastAttackingPlayer(epd, value):
    f_bwrite_epd(epd + 0x090 // 4, 0x090 % 4, value)

def f_getSecondaryOrderTimer(epd):
    return f_bread_epd(epd + 0x091 // 4, 0x091 % 4)

def f_setSecondaryOrderTimer(epd, value):
    f_bwrite_epd(epd + 0x091 // 4, 0x091 % 4, value)

def f_getAIActionFlag(epd):
    return f_bread_epd(epd + 0x092 // 4, 0x092 % 4)

def f_setAIActionFlag(epd, value):
    f_bwrite_epd(epd + 0x092 // 4, 0x092 % 4, value)

def f_getUserActionFlags(epd):
    return f_bread_epd(epd + 0x093 // 4, 0x093 % 4)

def f_setUserActionFlags(epd, value):
    f_bwrite_epd(epd + 0x093 // 4, 0x093 % 4, value)

def f_getCurrentButtonSet(epd):
    return f_wwrite_epd(epd + 0x094 // 4, 0x094 % 4, value)

def f_setCurrentButtonSet(epd, value):
    f_wwrite_epd(0x094 // 4, 0x094 % 4, value)

def f_getIsCloaked(epd):
    return f_boolread_epd(epd + 0x096 // 4, 0x096 % 4)

def f_setIsCloaked(epd, value):
    f_boolwrite_epd(epd + 0x096 // 4, 0x096 % 4, value)

def f_getMovementState(epd):
    return f_UnitMovementStateread_epd(epd + 0x097 // 4, 0x097 % 4)

def f_setMovementState(epd, value):
    f_UnitMovementStatewrite_epd(epd + 0x097 // 4, 0x097 % 4, value)

def f_getBuildQueue1(epd):
    return f_wread_epd(epd + 0x098 // 4, 0x098 % 4)

def f_setBuildQueue1(epd, value):
    f_wwrite_epd(epd + 0x098 // 4, 0x098 % 4, value)

def f_getBuildQueue2(epd):
    return f_wread_epd(epd + 0x09A // 4, 0x09A % 4)

def f_setBuildQueue2(epd, value):
    f_wwrite_epd(epd + 0x09A // 4, 0x09A % 4, value)

def f_getBuildQueue3(epd):
    return f_wread_epd(epd + 0x09C // 4, 0x09C % 4)

def f_setBuildQueue3(epd, value):
    f_wwrite_epd(epd + 0x09C // 4, 0x09C % 4, value)

def f_getBuildQueue4(epd):
    return f_wread_epd(epd + 0x09E // 4, 0x09E % 4)

def f_setBuildQueue4(epd, value):
    f_wwrite_epd(epd + 0x09E // 4, 0x09E % 4, value)

def f_getBuildQueue5(epd):
    return f_wread_epd(epd + 0x0A0 // 4, 0x0A0 % 4)

def f_setBuildQueue5(epd, value):
    f_wwrite_epd(epd + 0x0A0 // 4, 0x0A0 % 4, value)

def f_getEnergy(epd):
    return f_wread_epd(epd + 0x0A2 // 4, 0x0A2 % 4)

def f_setEnergy(epd, value):
    f_wwrite_epd(epd + 0x0A2 // 4, 0x0A2 % 4, value)

def f_getBuildQueueSlot(epd):
    return f_bread_epd(epd + 0x0A4 // 4, 0x0A4 % 4)

def f_setBuildQueueSlot(epd, value):
    f_bwrite_epd(epd + 0x0A4 // 4, 0x0A4 % 4, value)

def f_getUniquenessIdentifier(epd):
    return f_bread_epd(epd + 0x0A5 // 4, 0x0A5 % 4)

def f_setUniquenessIdentifier(epd, value):
    f_bwrite_epd(epd + 0x0A5 // 4, 0x0A5 % 4, value)

def f_getSecondaryOrderID(epd):
    return f_bread_epd(epd + 0x0A6 // 4, 0x0A6 % 4)

def f_setSecondaryOrderID(epd, value):
    f_bwrite_epd(epd + 0x0A6 // 4, 0x0A6 % 4, value)

def f_getBuildingOverlayState(epd):
    return f_bread_epd(epd + 0x0A7 // 4, 0x0A7 % 4)

def f_setBuildingOverlayState(epd, value):
    f_bwrite_epd(epd + 0x0A7 // 4, 0x0A7 % 4, value)

def f_getHpGain(epd):
    return f_wread_epd(epd + 0x0A8 // 4, 0x0A8 % 4)

def f_setHpGain(epd, value):
    f_wwrite_epd(epd + 0x0A8 // 4, 0x0A8 % 4, value)

def f_getShieldGain(epd):
    return f_wread_epd(epd + 0x0AA // 4, 0x0AA % 4)

def f_setShieldGain(epd, value):
    f_wwrite_epd(epd + 0x0AA // 4, 0x0AA % 4, value)

def f_getRemainingBuildTime(epd):
    return f_wread_epd(epd + 0x0AC // 4, 0x0AC % 4)

def f_setRemainingBuildTime(epd, value):
    f_wwrite_epd(epd + 0x0AC // 4, 0x0AC % 4, value)

def f_getPreviousHP(epd):
    return f_wread_epd(epd + 0x0AE // 4, 0x0AE % 4)

def f_setPreviousHP(epd, value):
    f_wwrite_epd(epd + 0x0AE // 4, 0x0AE % 4, value)

def f_getLoadedUnitIndex1(epd):
    return f_wread_epd(epd + 0x0B0 // 4, 0x0B0 % 4)

def f_setLoadedUnitIndex1(epd, value):
    f_wwrite_epd(epd + 0x0B0 // 4, 0x0B0 % 4, value)

def f_getLoadedUnitIndex2(epd):
    return f_wread_epd(epd + 0x0B2 // 4, 0x0B2 % 4)

def f_setLoadedUnitIndex2(epd, value):
    f_wwrite_epd(epd + 0x0B2 // 4, 0x0B2 % 4, value)

def f_getLoadedUnitIndex3(epd):
    return f_wread_epd(epd + 0x0B4 // 4, 0x0B4 % 4)

def f_setLoadedUnitIndex3(epd, value):
    f_wwrite_epd(epd + 0x0B4 // 4, 0x0B4 % 4, value)

def f_getLoadedUnitIndex4(epd):
    return f_wread_epd(epd + 0x0B6 // 4, 0x0B6 % 4)

def f_setLoadedUnitIndex4(epd, value):
    f_wwrite_epd(epd + 0x0B6 // 4, 0x0B6 % 4, value)

def f_getLoadedUnitIndex5(epd):
    return f_wread_epd(epd + 0x0B8 // 4, 0x0B8 % 4)

def f_setLoadedUnitIndex5(epd, value):
    f_wwrite_epd(epd + 0x0B8 // 4, 0x0B8 % 4, value)

def f_getLoadedUnitIndex6(epd):
    return f_wread_epd(epd + 0x0BA // 4, 0x0BA % 4)

def f_setLoadedUnitIndex6(epd, value):
    f_wwrite_epd(epd + 0x0BA // 4, 0x0BA % 4, value)

def f_getLoadedUnitIndex7(epd):
    return f_wread_epd(epd + 0x0BC // 4, 0x0BC % 4)

def f_setLoadedUnitIndex7(epd, value):
    f_wwrite_epd(epd + 0x0BC // 4, 0x0BC % 4, value)

def f_getLoadedUnitIndex8(epd):
    return f_wread_epd(epd + 0x0BE // 4, 0x0BE % 4)

def f_setLoadedUnitIndex8(epd, value):
    f_wwrite_epd(epd + 0x0BE // 4, 0x0BE % 4, value)

def f_getSpiderMineCount(epd):
    return f_bread_epd(epd + 0x0C0 // 4, 0x0C0 % 4)

def f_setSpiderMineCount(epd, value):
    f_bwrite_epd(epd + 0x0C0 // 4, 0x0C0 % 4, value)

def f_getPInHanger(epd):
    return f_dwread_epd(epd + 0x0C0 // 4)

def f_setPInHanger(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value)

def f_getPOutHanger(epd):
    return f_dwread_epd(epd + 0x0C4 // 4)

def f_setPOutHanger(epd, value):
    f_dwwrite_epd(epd, 0x0C4, value)

def f_getInHangerCount(epd):
    return f_bread_epd(epd + 0x0C8 // 4, 0x0C8 % 4)

def f_setInHangerCount(epd, value):
    f_bwrite_epd(epd + 0x0C8 // 4, 0x0C8 % 4, value)

def f_getOutHangerCount(epd):
    return f_bread_epd(epd + 0x0C9 // 4, 0x0C9 % 4)

def f_setOutHangerCount(epd, value):
    f_bwrite_epd(epd + 0x0C9 // 4, 0x0C9 % 4, value)

def f_getFighterParent(epd):
    return f_dwread_epd(epd + 0x0C0 // 4)

def f_setFighterParent(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value)

def f_getFighterPrev(epd):
    return f_dwread_epd(epd + 0x0C4 // 4)

def f_setFighterPrev(epd, value):
    f_dwwrite_epd(epd, 0x0C4, value)

def f_getFighterNext(epd):
    return f_dwread_epd(epd + 0x0C8 // 4)

def f_setFighterNext(epd, value):
    f_dwwrite_epd(epd, 0x0C8, value)

def f_getFighterInHanger(epd):
    return f_boolread_epd(epd + 0x0CC // 4, 0x0CC % 4)

def f_setFighterInHanger(epd, value):
    f_boolwrite_epd(epd + 0x0CC // 4, 0x0CC % 4, value)

def f_getUnknown00(epd):
    return f_dwread_epd(epd + 0x0C0 // 4)

def f_setUnknown00(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value)

def f_getUnknown04(epd):
    return f_dwread_epd(epd + 0x0C4 // 4)

def f_setUnknown04(epd, value):
    f_dwwrite_epd(epd, 0x0C4, value)

def f_getFlagSpawnFrame(epd):
    return f_dwread_epd(epd + 0x0C8 // 4)

def f_setFlagSpawnFrame(epd, value):
    f_dwwrite_epd(epd, 0x0C8, value)

def f_getAddon(epd):
    return f_dwread_epd(epd + 0x0C0 // 4)

def f_setAddon(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value)

def f_getAddonBuildType(epd):
    return f_wread_epd(epd + 0x0C4 // 4, 0x0C4 % 4)

def f_setAddonBuildType(epd, value):
    f_wwrite_epd(epd + 0x0C4 // 4, 0x0C4 % 4, value)

def f_getUpgradeResearchTime(epd):
    return f_wread_epd(epd + 0x0C6 // 4, 0x0C6 % 4)

def f_setUpgradeResearchTime(epd, value):
    f_wwrite_epd(epd + 0x0C6 // 4, 0x0C6 % 4, value)

def f_getTechType(epd):
    return f_bread_epd(epd + 0x0C8 // 4, 0x0C8 % 4)

def f_setTechType(epd, value):
    f_bwrite_epd(epd + 0x0C8 // 4, 0x0C8 % 4, value)

def f_getUpgradeType(epd):
    return f_bread_epd(epd + 0x0C9 // 4, 0x0C9 % 4)

def f_setUpgradeType(epd, value):
    f_bwrite_epd(epd + 0x0C9 // 4, 0x0C9 % 4, value)

def f_getLarvaTimer(epd):
    return f_bread_epd(epd + 0x0CA // 4, 0x0CA % 4) // 65536 

def f_setLarvaTimer(epd, value):
    f_bwrite_epd(epd + 0x0CA // 4, 0x0CA % 4, value * 65536)

def f_getLandingTimer(epd):
    return f_bread_epd(epd + 0x0CB // 4, 0x0CB % 4)

def f_setLandingTimer(epd, value):
    f_bwrite_epd(epd + 0x0CB // 4, 0x0CB % 4, value)

def f_getCreepTimer(epd):
    return f_bread_epd(epd + 0x0CC // 4, 0x0CC % 4)

def f_setCreepTimer(epd, value):
    f_bwrite_epd(epd + 0x0CC // 4, 0x0CC % 4, value)

def f_getUpgradeLevel(epd):
    return f_bread_epd(epd + 0x0CD // 4, 0x0CD % 4)

def f_setUpgradeLevel(epd, value):
    f_bwrite_epd(epd + 0x0CD // 4, 0x0CD % 4, value)

def f_getUnknownE(epd):
    return f_wread_epd(epd + 0x0CE // 4, 0x0CE % 4)

def f_setUnknownE(epd, value):
    f_wwrite_epd(epd + 0x0CE // 4, 0x0CE % 4, value)

def f_getPowerup(epd):
    return f_dwread_epd(epd + 0x0C0 // 4)

def f_setPowerup(epd, value):
    f_dwwrite_epd(epd, 0x0C0, value)

def f_getTargetResourceX(epd):
    return f_wread_epd(epd + 0x0C4 // 4, 0x0C4 % 4)

def f_setTargetResourceX(epdepd, value):
    f_wread_epd(epd + 0x0C4 // 4, 0x0C4 % 4)

def f_getTargetResourceY(epd):
    return f_wread_epd(epd + 0x0C6 // 4, 0x0C6 % 4)

def f_setTargetResourceY(epdepd, value):
    f_wread_epd(epd + 0x0C6 // 4, 0x0C6 % 4)

def f_getTargetResourceUnit(epd):
    return f_dwread_epd(epd + 0x0C8 // 4)

def f_setTargetResourceUnit(epdepd, value):
    f_dwread_epd(epd + 0x0C8 // 4)

def f_getRepairResourceLossTimer(epd):
    return f_wread_epd(epd + 0x0CC // 4, 0x0CC % 4)

def f_setRepairResourceLossTimer(epd, value):
    f_wwrite_epd(epd + 0x0CC // 4, 0x0CC % 4, value)

def f_getIsCarryingSomething(epd):
    return f_boolread_epd(epd + 0x0CE // 4, 0x0CE % 4)

def f_setIsCarryingSomething(epd, value):
    f_boolwrite_epd(epd + 0x0CE // 4, 0x0CE % 4, value)

def f_getResourceCarryCount(epd):
    return f_bread_epd(epd + 0x0CF // 4, 0x0CF % 4)

def f_setResourceCarryCount(epd, value):
    f_bwrite_epd(epd + 0x0CF // 4, 0x0CF % 4, value)

def f_getHarvestTarget(epd):
    return f_dwread_epd(epd + 0x0D0 // 4)

def f_setHarvestTarget(epdepd, value):
    f_dwread_epd(epd + 0x0D0 // 4)

def f_getPrevHarvestUnit(epd):
    return f_dwread_epd(epd + 0x0D4 // 4)

def f_setPrevHarvestUnit(epd, value):
    f_dwwrite_epd(epd, 0x0D4, value)

def f_getNextHarvestUnit(epd):
    return f_dwread_epd(epd + 0x0D8 // 4)

def f_setNextHarvestUnit(epd, value):
    f_dwwrite_epd(epd, 0x0D8, value)

def f_getResourceCount(epd):
    return f_wread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def f_setResourceCount(epd, value):
    f_wwrite_epd(epd + 0x0D0 // 4, 0x0D0 % 4, value)

def f_getResourceIscript(epd):
    return f_bread_epd(epd + 0x0D2 // 4, 0x0D2 % 4)

def f_setResourceIscript(epd, value):
    f_bwrite_epd(epd + 0x0D2 // 4, 0x0D2 % 4, value)

def f_getGatherQueueCount(epd):
    return f_bread_epd(epd + 0x0D3 // 4, 0x0D3 % 4)

def f_setGatherQueueCount(epd, value):
    f_bwrite_epd(epd + 0x0D3 // 4, 0x0D3 % 4, value)

def f_getNextGatherer(epd):
    return f_dwread_epd(epd + 0x0D4 // 4)

def f_setNextGatherer(epd, value):
    f_dwwrite_epd(epd, 0x0D4, value)

def f_getResourceGroup(epd):
    return f_bread_epd(epd + 0x0D8 // 4, 0x0D8 % 4)

def f_setResourceGroup(epd, value):
    f_bwrite_epd(epd + 0x0D8 // 4, 0x0D8 % 4, value)

def f_getResourceBelongsToAI(epd):
    return f_bread_epd(epd + 0x0D9 // 4, 0x0D9 % 4)

def f_setResourceBelongsToAI(epd, value):
    f_bwrite_epd(epd + 0x0D9 // 4, 0x0D9 % 4, value)

def f_getNydusExit(epd):
    return f_dwread_epd(epd + 0x0D0 // 4)

def f_setNydusExit(epd, value):
    f_dwwrite_epd(epd, 0x0D0, value)

def f_getGhostNukeDot(epd):
    return f_dwread_epd(epd + 0x0D0 // 4)

def f_setGhostNukeDot(epd, value):
    f_dwwrite_epd(epd, 0x0D0, value)

def f_getPylonpPowerTemplate(epd):
    return f_dwread_epd(epd + 0x0D0 // 4)

def f_setPylonpPowerTemplate(epd, value):
    f_dwwrite_epd(epd, 0x0D0, value)

def f_getSiloNuke(epd):
    return f_dwread_epd(epd + 0x0D0 // 4)

def f_setSiloNuke(epd, value):
    f_dwwrite_epd(epd, 0x0D0, value)

def f_getSiloReady(epd):
    return f_boolread_epd(epd + 0x0D4 // 4, 0x0D4 % 4)

def f_setSiloReady(epd, value):
    f_boolwrite_epd(epd + 0x0D4 // 4, 0x0D4 % 4, value)

def f_getHatcheryHarvestValueLeft(epd):
    return f_wread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def f_setHatcheryHarvestValueLeft(epd, value):
    f_wwrite_epd(epd + 0x0D0 // 4, 0x0D0 % 4, value)

def f_getHatcheryHarvestValueTop(epd):
    return f_wread_epd(epd + 0x0D2 // 4, 0x0D2 % 4)

def f_setHatcheryHarvestValueTop(epd, value):
    f_wwrite_epd(epd + 0x0D2 // 4, 0x0D2 % 4, value)

def f_getHatcheryHarvestValueRight(epd):
    return f_wread_epd(epd + 0x0D4 // 4, 0x0D4 % 4)

def f_setHatcheryHarvestValueRight(epd, value):
    f_wwrite_epd(epd + 0x0D4 // 4, 0x0D4 % 4, value)

def f_getHatcheryHarvestValueBottom(epd):
    return f_wread_epd(epd + 0x0D6 // 4, 0x0D6 % 4)

def f_setHatcheryHarvestValueBottom(epd, value):
    f_wwrite_epd(epd + 0x0D6 // 4, 0x0D6 % 4, value)

def f_getOriginX(epd):
    return f_wread_epd(epd + 0x0D0 // 4, 0x0D0 % 4)

def f_setOriginX(epd, value):
    f_wwrite_epd(epd + 0x0D0 // 4, 0x0D0 % 4, value)

def f_getOriginY(epd):
    return f_wread_epd(epd + 0x0D2 // 4, 0x0D2 % 4)

def f_setOriginY(epd, value):
    f_wwrite_epd(epd + 0x0D2 // 4, 0x0D2 % 4, value)

def f_getStatusFlags(epd):
    return f_statusFlagsread_epd(epd + 0x0DC // 4, 0x0DC % 4)

def f_setStatusFlags(epd, value):
    f_statusFlagswrite_epd(epd + 0x0DC // 4, 0x0DC % 4, value)

def f_getResourceType(epd):
    return f_bread_epd(epd + 0x0E0 // 4, 0x0E0 % 4)

def f_setResourceType(epd, value):
    f_bwrite_epd(epd + 0x0E0 // 4, 0x0E0 % 4, value)

def f_getWireframeRandomizer(epd):
    return f_bread_epd(epd + 0x0E1 // 4, 0x0E1 % 4)

def f_setWireframeRandomizer(epd, value):
    f_bwrite_epd(epd + 0x0E1 // 4, 0x0E1 % 4, value)

def f_getSecondaryOrderState(epd):
    return f_bread_epd(epd + 0x0E2 // 4, 0x0E2 % 4)

def f_setSecondaryOrderState(epd, value):
    f_bwrite_epd(epd + 0x0E2 // 4, 0x0E2 % 4, value)

def f_getRecentOrderTimer(epd):
    return f_bread_epd(epd + 0x0E3 // 4, 0x0E3 % 4)

def f_setRecentOrderTimer(epd, value):
    f_bwrite_epd(epd + 0x0E3 // 4, 0x0E3 % 4, value)

def f_getVisibilityStatus(epd):
    return f_dwread_epd(epd + 0x0E4 // 4)

def f_setVisibilityStatus(epd, value):
    f_dwwrite_epd(epd, 0x0E4, value)

def f_getSecondaryOrderPositionX(epd):
    return f_wread_epd(epd + 0x0E8 // 4, 0x0E8 % 4)

def f_setSecondaryOrderPositionX(epd, value):
    f_wwrite_epd(epd + 0x0E8 // 4, 0x0E8 % 4, value)

def f_getSecondaryOrderPositionY(epd):
    return f_wread_epd(epd + 0x0EA // 4, 0x0EA % 4)

def f_setSecondaryOrderPositionY(epd, value):
    f_wwrite_epd(epd + 0x0EA // 4, 0x0EA % 4, value)

def f_getCurrentBuildUnit(epd):
    return f_dwread_epd(epd + 0x0EC // 4)

def f_setCurrentBuildUnit(epd, value):
    f_dwwrite_epd(epd, 0x0EC, value)

def f_getPreviousBurrowedUnit(epd):
    return f_dwread_epd(epd + 0x0F0 // 4)

def f_setPreviousBurrowedUnit(epd, value):
    f_dwwrite_epd(epd, 0x0F0, value)

def f_getNextBurrowedUnit(epd):
    return f_dwread_epd(epd + 0x0F4 // 4)

def f_setNextBurrowedUnit(epd, value):
    f_dwwrite_epd(epd, 0x0F4, value)

def f_getRallyPositionX(epd):
    return f_wread_epd(epd + 0x0F8 // 4, 0x0F8 % 4)

def f_setRallyPositionX(epd, value):
    f_wwrite_epd(epd + 0x0F8 // 4, 0x0F8 % 4, value)

def f_getRallyPositionY(epd):
    return f_wread_epd(epd + 0x0FA // 4, 0x0FA % 4)

def f_setRallyPositionY(epd, value):
    f_wwrite_epd(epd + 0x0FA // 4, 0x0FA % 4, value)

def f_getRallyUnit(epd):
    return f_dwread_epd(epd + 0x0FC // 4)

def f_setRallyUnit(epd, value):
    f_dwwrite_epd(epd, 0x0FC, value)

def f_getPylonPrevPsiProvider(epd):
    return f_dwread_epd(epd + 0x0F8 // 4)

def f_setPylonPrevPsiProvider(epd, value):
    f_dwwrite_epd(epd, 0x0F8, value)

def f_getPylonNextPsiProvider(epd):
    return f_dwread_epd(epd + 0x0FC // 4)

def f_setPylonNextPsiProvider(epd, value):
    f_dwwrite_epd(epd, 0x0FC, value)

def f_getPath(epd):
    return f_dwread_epd(epd + 0x100 // 4)

def f_setPath(epd, value):
    f_dwwrite_epd(epd, 0x100, value)

def f_getPathingCollisionInterval(epd):
    return f_bread_epd(epd + 0x104 // 4, 0x104 % 4)

def f_setPathingCollisionInterval(epd, value):
    f_bwrite_epd(epd + 0x104 // 4, 0x104 % 4, value)

def f_getPathingFlags(epd):
    return f_bread_epd(epd + 0x105 // 4, 0x105 % 4)

def f_setPathingFlags(epd, value):
    f_bwrite_epd(epd + 0x105 // 4, 0x105 % 4, value)

def f_get106Flag(epd):
    return f_bread_epd(epd + 0x106 // 4, 0x106 % 4)

def f_set106(epd, value):
    f_bwrite_epd(epd + 0x106 // 4, 0x106 % 4, value)

def f_getIsBeingHealed(epd):
    return f_boolread_epd(epd + 0x107 // 4, 0x107 % 4)

def f_setIsBeingHealed(epd, value):
    f_boolwrite_epd(epd + 0x107 // 4, 0x107 % 4, value)

def f_getContourBoundsLeft(epd):
    return f_wread_epd(epd + 0x108 // 4, 0x108 % 4)

def f_setContourBoundsLeft(epd, value):
    f_wwrite_epd(epd + 0x108 // 4, 0x108 % 4, value)

def f_getContourBoundsTop(epd):
    return f_wread_epd(epd + 0x10A // 4, 0x10A % 4)

def f_setContourBoundsTop(epd, value):
    f_wwrite_epd(epd + 0x10A // 4, 0x10A % 4, value)

def f_getContourBoundsRight(epd):
    return f_wread_epd(epd + 0x10C // 4, 0x10C % 4)

def f_setContourBoundsRight(epd, value):
    f_wwrite_epd(epd + 0x10C // 4, 0x10C % 4, value)

def f_getContourBoundsBottom(epd):
    return f_wread_epd(epd + 0x10E // 4, 0x10E % 4)

def f_setContourBoundsBottom(epd, value):
    f_wwrite_epd(epd + 0x10E // 4, 0x10E % 4, value)

def f_getRemoveTimer(epd):
    return f_wread_epd(epd + 0x110 // 4, 0x110 % 4)

def f_setRemoveTimer(epd, value):
    f_wwrite_epd(epd + 0x110 // 4, 0x110 % 4, value)

def f_getDefenseMatrixDamage(epd):
    return f_wread_epd(epd + 0x112 // 4, 0x112 % 4)

def f_setDefenseMatrixDamage(epd, value):
    f_wwrite_epd(epd + 0x112 // 4, 0x112 % 4, value)

def f_getDefenseMatrixTimer(epd):
    return f_bread_epd(epd + 0x114 // 4, 0x114 % 4)

def f_setDefenseMatrixTimer(epd, value):
    f_bwrite_epd(epd + 0x114 // 4, 0x114 % 4, value)

def f_getStimTimer(epd):
    return f_bread_epd(epd + 0x115 // 4, 0x115 % 4) // 256

def f_setStimTimer(epd, value):
    f_bwrite_epd(epd + 0x115 // 4, 0x115 % 4, value * 256)

def f_getEnsnareTimer(epd):
    return f_bread_epd(epd + 0x116 // 4, 0x116 % 4)

def f_setEnsnareTimer(epd, value):
    f_bwrite_epd(epd + 0x116 // 4, 0x116 % 4, value)

def f_getLockdownTimer(epd):
    return f_bread_epd(epd + 0x117 // 4, 0x117 % 4)

def f_setLockdownTimer(epd, value):
    f_bwrite_epd(epd + 0x117 // 4, 0x117 % 4, value)

def f_getIrradiateTimer(epd):
    return f_bread_epd(epd + 0x118 // 4, 0x118 % 4)

def f_setIrradiateTimer(epd, value):
    f_bwrite_epd(epd + 0x118 // 4, 0x118 % 4, value)

def f_getStasisTimer(epd):
    return f_bread_epd(epd + 0x119 // 4, 0x119 % 4)

def f_setStasisTimer(epd, value):
    f_bwrite_epd(epd + 0x119 // 4, 0x119 % 4, value)

def f_getPlagueTimer(epd):
    return f_bread_epd(epd + 0x11A // 4, 0x11A % 4)

def f_setPlagueTimer(epd, value):
    f_bwrite_epd(epd + 0x11A // 4, 0x11A % 4, value)

def f_getStormTimer(epd):
    return f_bread_epd(epd + 0x11B // 4, 0x11B % 4)

def f_setStormTimer(epd, value):
    f_bwrite_epd(epd + 0x11B // 4, 0x11B % 4, value)

def f_getIrradiatedBy(epd):
    return f_dwread_epd(epd + 0x11C // 4)

def f_setIrradiatedBy(epd, value):
    f_dwwrite_epd(epd, 0x11C, value)

def f_getIrradiatePlayerID(epd):
    return f_bread_epd(epd + 0x120 // 4, 0x120 % 4)

def f_setIrradiatePlayerID(epd, value):
    f_bwrite_epd(epd + 0x120 // 4, 0x120 % 4, value)

def f_getParasiteFlags(epd):
    return f_bread_epd(epd + 0x121 // 4, 0x121 % 4)

def f_setParasiteFlags(epd, value):
    f_bwrite_epd(epd + 0x121 // 4, 0x121 % 4, value)

def f_getCycleCounter(epd):
    return f_bread_epd(epd + 0x122 // 4, 0x122 % 4)

def f_setCycleCounter(epd, value):
    f_bwrite_epd(epd + 0x122 // 4, 0x122 % 4, value)

def f_getIsBlind(epd):
    return f_boolread_epd(epd + 0x123 // 4, 0x123 % 4)

def f_setIsBlind(epd, value):
    f_boolwrite_epd(epd + 0x123 // 4, 0x123 % 4, value)

def f_getMaelstromTimer(epd):
    return f_bread_epd(epd + 0x124 // 4, 0x124 % 4)

def f_setMaelstromTimer(epd, value):
    f_bwrite_epd(epd + 0x124 // 4, 0x124 % 4, value)

def f_getUnused_0x125(epd):
    return f_bread_epd(epd + 0x125 // 4, 0x125 % 4)

def f_set_unused_0x125(epd, value):
    f_bwrite_epd(epd + 0x125 // 4, 0x125 % 4, value)

def f_getAcidSporeCount(epd):
    return f_bread_epd(epd + 0x126 // 4, 0x126 % 4)

def f_setAcidSporeCount(epd, value):
    f_bwrite_epd(epd + 0x126 // 4, 0x126 % 4, value)

def f_getAcidSporeTime_1(epd):
    return f_bread_epd(epd + 0x127 // 4, 0x127 % 4)

def f_setAcidSporeTime_1(epd, value):
    f_bwrite_epd(epd + 0x127 // 4, 0x127 % 4, value)

def f_getAcidSporeTime_2(epd):
    return f_bread_epd(epd + 0x128 // 4, 0x128 % 4)

def f_setAcidSporeTime_2(epd, value):
    f_bwrite_epd(epd + 0x128 // 4, 0x128 % 4, value)

def f_getAcidSporeTime_3(epd):
    return f_bread_epd(epd + 0x129 // 4, 0x129 % 4)

def f_setAcidSporeTime_3(epd, value):
    f_bwrite_epd(epd + 0x129 // 4, 0x129 % 4, value)

def f_getAcidSporeTime_4(epd):
    return f_bread_epd(epd + 0x12A // 4, 0x12A % 4)

def f_setAcidSporeTime_4(epd, value):
    f_bwrite_epd(epd + 0x12A // 4, 0x12A % 4, value)

def f_getAcidSporeTime_5(epd):
    return f_bread_epd(epd + 0x12B // 4, 0x12B % 4)

def f_setAcidSporeTime_5(epd, value):
    f_bwrite_epd(epd + 0x12B // 4, 0x12B % 4, value)

def f_getAcidSporeTime_6(epd):
    return f_bread_epd(epd + 0x12C // 4, 0x12C % 4)

def f_setAcidSporeTime_6(epd, value):
    f_bwrite_epd(epd + 0x12C // 4, 0x12C % 4, value)

def f_getAcidSporeTime_7(epd):
    return f_bread_epd(epd + 0x12D // 4, 0x12D % 4)

def f_setAcidSporeTime_7(epd, value):
    f_bwrite_epd(epd + 0x12D // 4, 0x12D % 4, value)

def f_getAcidSporeTime_8(epd):
    return f_bread_epd(epd + 0x12E // 4, 0x12E % 4)

def f_setAcidSporeTime_8(epd, value):
    f_bwrite_epd(epd + 0x12E // 4, 0x12E % 4, value)

def f_getAcidSporeTime_9(epd):
    return f_bread_epd(epd + 0x12F // 4, 0x12F % 4)

def f_setAcidSporeTime_9(epd, value):
    f_bwrite_epd(epd + 0x12F // 4, 0x12F % 4, value)

def f_getBulletBehaviour3by3AttackSequence(epd):
    return f_wread_epd(epd + 0x130 // 4, 0x130 % 4)

def f_setBulletBehaviour3by3AttackSequence(epd, value):
    f_wwrite_epd(epd + 0x130 // 4, 0x130 % 4, value)

def f_getPadding_0x132(epd):
    return f_wread_epd(epd + 0x132 // 4, 0x132 % 4)

def f_set_padding_0x132(epd, value):
    f_wwrite_epd(epd + 0x132 // 4, 0x132 % 4, value)

def f_getPAI(epd):
    return f_dwread_epd(epd + 0x134 // 4)

def f_setPAI(epd, value):
    f_dwwrite_epd(epd, 0x134, value)

def f_getAirStrength(epd):
    return f_wread_epd(epd + 0x138 // 4, 0x138 % 4)

def f_setAirStrength(epd, value):
    f_wwrite_epd(epd + 0x138 // 4, 0x138 % 4, value)

def f_getGroundStrength(epd):
    return f_wread_epd(epd + 0x13A // 4, 0x13A % 4)

def f_setGroundStrength(epd, value):
    f_wwrite_epd(epd + 0x13A // 4, 0x13A % 4, value)

def f_getFinderLeft(epd):
    return f_bread_epd(epd + 0x13C // 4, 0x13C % 4)

def f_setFinderLeft(epd, value):
    f_bwrite_epd(epd + 0x13C // 4, 0x13C % 4, value)

def f_getFinderRight(epd):
    return f_bread_epd(epd + 0x140 // 4, 0x140 % 4)

def f_setFinderRight(epd, value):
    f_bwrite_epd(epd + 0x140 // 4, 0x140 % 4, value)

def f_getFinderTop(epd):
    return f_bread_epd(epd + 0x144 // 4, 0x144 % 4)

def f_setFinderTop(epd, value):
    f_bwrite_epd(epd + 0x144 // 4, 0x144 % 4, value)

def f_getFinderBottom(epd):
    return f_bread_epd(epd + 0x148 // 4, 0x148 % 4)

def f_setFinderBottom(epd, value):
    f_bwrite_epd(epd + 0x148 // 4, 0x148 % 4, value)

def f_getRepulseUnknown(epd):
    return f_bread_epd(epd + 0x14C // 4, 0x14C % 4)

def f_setRepulseUnknown(epd, value):
    f_bwrite_epd(epd + 0x14C // 4, 0x14C % 4, value)

def f_getRepulseAngle(epd):
    return f_bread_epd(epd + 0x14D // 4, 0x14D % 4)

def f_setRepulseAngle(epd, value):
    f_bwrite_epd(epd + 0x14D // 4, 0x14D % 4, value)

def f_getBRepMtxX(epd):
    return f_bread_epd(epd + 0x14E // 4, 0x14E % 4)

def f_setBRepMtxX(epd, value):
    f_bwrite_epd(epd + 0x14E // 4, 0x14E % 4, value)

def f_getBRepMtxY(epd):
    return f_bread_epd(epd + 0x14F // 4, 0x14F % 4)

def f_setBRepMtxY(epd, value):
    f_bwrite_epd(epd + 0x14F // 4, 0x14F % 4, value)