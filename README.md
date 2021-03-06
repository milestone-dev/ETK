# EUD Trigger Kit
ETK is a collection of EUD EPS functions designed for StarCraft: Brood War map creators. It aims to help you create powerful and flexible maps by providing an accessible and well documented API. 

ETK is possible thanks to [euddraft](https://github.com/phu54321/euddraft/) and is meant to be used with the powerful [EUD Editor 3](https://github.com/Buizz/EUD-Editor-3)

## Installation
Download the [Latest Version Zip File](https://github.com/milestone-games/ETK/archive/master.zip) and place all files in this folder:

`C:\Program Files\EUD.Editor.3.0\Data\TriggerEditor\` 

## Usage

```javascript
import TriggerEditor.ETKUnit as Unit;
import TriggerEditor.ETKUtils as Utils;
import TriggerEditor.ETKTimer as Timer;
import TriggerEditor.ETKConstants as Const;

var heroUnit;

function onPluginStart() {
	heroUnit = Utils.createUnit($U("Terran Firebat"), $L("Anywhere"), $P1);
	Unit.setEnergy(heroUnit, 100);
}

function beforeTriggerExec() {

	// Passive Ability: Hero gains HP while attacking
	if (Unit.getOrder(heroUnit) == Const.Order_AttackUnit_Normal) {
		// Heal the hero for 15 HP every 3 seconds, with a Restoration overlay effect 
		if (!Timer.isTimerRunningForUnit(heroUnit)) {
			Timer.add(24 * 3, heroUnit, EUDFuncPtr (1, 0) (function(callbackUnit) {
				Utils.createImageSpriteAtUnitPosition(callbackUnit, Const.Image_Restoration_Hit_Small);
				Unit.heal(callbackUnit, 50);
			}));
		}
	}
}

```

## API Reference

Coming soon...