# shipEnergyVampireRangeBonusFixedAF2
#
# Used by:
# Ship: Malice
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Vampire",
                                  "powerTransferRange", ship.getModifiedItemAttr("shipBonus2AF") * level)
