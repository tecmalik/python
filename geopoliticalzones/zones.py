from enum import Enum
class Zones (Enum):
    SOUTH_SOUTH = ("Akwa-Ibom", "Bayelsa", "Cross-River", "Delta", "Edo", "Rivers"),
    NORTH_EAST = ("Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe") ,
    NORTH_WEST = ("Kaduna", "Katsina", "Kano", "Kebbi", "Sokoto", "Jigawa", "Zamfara"),
    SOUTH_EAST = ("Abia", "Anambra", "Ebonyi", "Enugu", "Imo"),
    SOUTH_WEST = ("Ekiti", "Lagos", "Osun", "Ondo", "Ogun", "Oyo"),
    NORTH_CENTRAL = ("Benue", "FCT", "Kogi", "Kwara", "Nasarawa", "Niger", "Plateau")


    def get_state(users_choice:str , zones:object):
        for zone in Zones:
            for state in zone.value:
                if state == users_choice.title():
                    return zone
        return "zone not a zone in nigeria"
print(Zones.get_state("Kogi",Zones))

