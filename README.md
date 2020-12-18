# EUD Trigger Kit
ETK is a collection of EUD EPS functions designed for StarCraft: Brood War map creators. It aims to help you create powerful and felible maps with its accessible, well documented API.
ETK is possible thanks to [euddraft](https://github.com/phu54321/euddraft/) and is meant to be used with the powerful [EUD Editor 3](https://github.com/Buizz/EUD-Editor-3)

## Installation
Download the [Latest Version Zip File](https://github.com/milestone-games/ETK/archive/master.zip) and place all files in this folder:

`C:\Program Files\EUD.Editor.3.0\Data\TriggerEditor\` 

## Usage

```javascript
import TriggerEditor.ETKUnit as Unit;
import TriggerEditor.ETKUtils as Utils;
import TriggerEditor.ETKConstants as Const;

var heroUnit;

function onPluginStart() {
	heroUnit = Utils.createUnit($U("Terran Firebat"), $L("Anywhere"), $P1);
	Unit.setEnergy(heroUnit, 100);
}

function beforeTriggerExec() {

	// Hero gains HP while attacking
	if (Unit.getOrder(heroUnit) == Const.Order_AttackUnit_Normal && Unit.getHitpoints(heroUnit) < Unit.getMaxHitpoints(heroUnit)) {
		Unit.setHitpoints(heroUnit, Unit.getHitpoints(heroUnit) + 1);
	}

}

```

## API Reference

Coming soon...