#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from eudplib import *

"""

"""

@EUDFunc

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
000,BW::CUnit*,prev
004,BW::CUnit*,next
008,s32,hitPoints
00C,BW::CSprite*,sprite
010,u16,moveTargetX
012,u16,moveTargetY
014,BW::CUnit*,moveTargetUnit
018,u16,nextMovementWaypointX
01A,u16,nextMovementWaypointY
01C,u16,nextTargetWaypointX
01E,u16,nextTargetWaypointY
020,u8,movementFlags
021,u8,currentDirection1
022,u8,flingyTurnRadius
023,u8,velocityDirection1
024,u16,flingyID
026,u8,_unknown_0x026
027,u8,flingyMovementType
028,u16,positionX
02A,u16,positionY
02C,u32,haltX
030,u32,haltY
034,u32,flingyTopSpeed
038,s32,current_speed1
03C,s32,current_speed2
040,u32,current_speedX
044,u32,current_speedY
048,u16,flingyAcceleration
04A,u8,currentDirection2
04B,u8,velocityDirection2
04C,u8,playerID
04D,u8,orderID
04E,u8,orderState
04F,u8,orderSignal
050,u16,orderUnitType
052,u16,__0x52
054,u8,mainOrderTimer
055,u8,groundWeaponCooldown
056,u8,airWeaponCooldown
057,u8,spellCooldown
058,u16,orderTargetX
05A,u16,orderTargetY
05C,BW::CUnit*,orderTargetUnit
060,u32,shieldPoints
064,u16,unitType
066,u16,__0x66
068,BW::CUnit*,previousPlayerUnit
06C,BW::CUnit*,nextPlayerUnit
070,BW::CUnit*,subUnit
074,BW::COrder*,orderQueueHead
078,BW::COrder*,orderQueueTail
07C,BW::CUnit*,autoTargetUnit
080,BW::CUnit*,connectedUnit
084,u8,orderQueueCount
085,u8,orderQueueTimer
086,u8,_unknown_0x086
087,u8,attackNotifyTimer
088,u16,previousUnitType
08A,u8,lastEventTimer
08B,u8,lastEventColor
08C,u16,_unused_0x08C
08E,u8,rankIncrease
08F,u8,killCount
090,u8,lastAttackingPlayer
091,u8,secondaryOrderTimer
092,u8,AIActionFlag
093,u8,userActionFlags
094,u16,currentButtonSet
096,bool,isCloaked
097,UnitMovementState,movementState
098,u16,buildQueue[1]
09A,u16,buildQueue[2]
09C,u16,buildQueue[3]
09E,u16,buildQueue[4]
0A0,u16,buildQueue[5]
0A2,u16,energy
0A4,u8,buildQueueSlot
0A5,u8,uniquenessIdentifier
0A6,u8,secondaryOrderID
0A7,u8,buildingOverlayState
0A8,u16,hpGain
0AA,u16,shieldGain
0AC,u16,remainingBuildTime
0AE,u16,previousHP
0B0,u16,loadedUnitIndex[1]
0B2,u16,loadedUnitIndex[2]
0B4,u16,loadedUnitIndex[3]
0B6,u16,loadedUnitIndex[4]
0B8,u16,loadedUnitIndex[5]
0BA,u16,loadedUnitIndex[6]
0BC,u16,loadedUnitIndex[7]
0BE,u16,loadedUnitIndex[8]
0C0,u8,VULTURE:spiderMineCount
0C0,BW::CUnit*,CARRIER:pInHanger
0C4,BW::CUnit*,CARRIER:pOutHanger
0C8,u8,CARRIER:inHangerCount
0C9,u8,CARRIER:outHangerCount
0C0,BW::CUnit*,FIGHTER:parent
0C4,BW::CUnit*,FIGHTER:prev
0C8,BW::CUnit*,FIGHTER:next
0CC,bool,FIGHTER:inHanger
0C0,u32,BEACON:_unknown_00
0C4,u32,BEACON:_unknown_04
0C8,u32,BEACON:flagSpawnFrame
0C0,BW::CUnit*,BUILDING:addon
0C4,u16,BUILDING:addonBuildType
0C6,u16,BUILDING:upgradeResearchTime
0C8,u8,BUILDING:techType
0C9,u8,BUILDING:upgradeType
0CA,u8,BUILDING:larvaTimer
0CB,u8,BUILDING:landingTimer
0CC,u8,BUILDING:creepTimer
0CD,u8,BUILDING:upgradeLevel
0CE,u16,BUILDING:__E
0C0,BW::CUnit*,WORKER:pPowerup
0C4,u16,WORKER:targetResourceX
0C6,u16,WORKER:targetResourceY
0C8,BW::CUnit*,WORKER:targetResourceUnit
0CC,u16,WORKER:repairResourceLossTimer
0CE,bool,WORKER:isCarryingSomething
0CF,u8,WORKER:resourceCarryCount
0D0,BW::CUnit*,WORKER:harvestTarget
0D4,BW::CUnit*,WORKER:prevHarvestUnit
0D8,BW::CUnit*,WORKER:nextHarvestUnit
0D0,u16,BUILDING:RESOURCE:resourceCount
0D2,u8,BUILDING:RESOURCE:resourceIscript
0D3,u8,BUILDING:RESOURCE:gatherQueueCount
0D4,BW::CUnit*,BUILDING:RESOURCE:nextGatherer
0D8,u8,BUILDING:RESOURCE:resourceGroup
0D9,u8,BUILDING:RESOURCE:resourceBelongsToAI
0D0,BW::CUnit*,BUILDING:NYDUS:exit
0D0,BW::CSprite*,BUILDING:GHOST:nukeDot
0D0,BW::CSprite*,BUILDING:PYLON:pPowerTemplate
0D0,BW::CUnit*,BUILDING:SILO:pNuke
0D4,bool,BUILDING:SILO:bReady
0D0,u16,BUILDING:HATCHERY:harvestValueLeft
0D2,u16,BUILDING:HATCHERY:harvestValueTop
0D4,u16,BUILDING:HATCHERY:harvestValueRight
0D6,u16,BUILDING:HATCHERY:harvestValueBottom
0D0,u16,BUILDING:POWERUP:originX
0D2,u16,BUILDING:POWERUP:originY
0DC,statusFlags,statusFlags
0E0,u8,resourceType
0E1,u8,wireframeRandomizer
0E2,u8,secondaryOrderState
0E3,u8,recentOrderTimer
0E4,s32,visibilityStatus
0E8,u16,secondaryOrderPositionX
0EA,u16,secondaryOrderPositionY
0EC,BW::CUnit*,currentBuildUnit
0F0,BW::CUnit*,previousBurrowedUnit
0F4,BW::CUnit*,nextBurrowedUnit
0F8,u16,RALLY:positionX
0FA,u16,RALLY:positionY
0FC,BW::CUnit*,RALLY:unit
0F8,BW::CUnit*,PYLON:prevPsiProvider
0FC,BW::CUnit*,PYLON:nextPsiProvider
100,BW::Path*,path
104,u8,pathingCollisionInterval
105,u8,pathingFlags
106,u8,_unused_0x106
107,bool,isBeingHealed
108,u16,contourBoundsLeft
10A,u16,contourBoundsTop
10C,u16,contourBoundsRight
10E,u16,contourBoundsBottom
110,u16,STATUS:removeTimer
112,u16,STATUS:defenseMatrixDamage
114,u8,STATUS:defenseMatrixTimer
115,u8,STATUS:stimTimer
116,u8,STATUS:ensnareTimer
117,u8,STATUS:lockdownTimer
118,u8,STATUS:irradiateTimer
119,u8,STATUS:stasisTimer
11A,u8,STATUS:plagueTimer
11B,u8,STATUS:stormTimer
11C,BW::CUnit*,STATUS:irradiatedBy
120,u8,STATUS:irradiatePlayerID
121,u8,STATUS:parasiteFlags
122,u8,STATUS:cycleCounter
123,bool,STATUS:isBlind
124,u8,STATUS:maelstromTimer
125,u8,STATUS:_unused_0x125
126,u8,STATUS:acidSporeCount
127,u8,STATUS:acidSporeTime[1]
128,u8,STATUS:acidSporeTime[2]
129,u8,STATUS:acidSporeTime[3]
12A,u8,STATUS:acidSporeTime[4]
12B,u8,STATUS:acidSporeTime[5]
12C,u8,STATUS:acidSporeTime[6]
12D,u8,STATUS:acidSporeTime[7]
12E,u8,STATUS:acidSporeTime[8]
12F,u8,STATUS:acidSporeTime[9]
130,u16,STATUS:bulletBehaviour3by3AttackSequence
132,u16,_padding_0x132
134,void*,pAI
138,u16,airStrength
13A,u16,groundStrength
13C,u8,FINDER:Left
140,u8,FINDER:Right
144,u8,FINDER:Top
148,u8,FINDER:Bottom
14C,u8,_repulseUnknown
14D,u8,repulseAngle
14E,u8,bRepMtxX
14F,u8,bRepMtxY
"""