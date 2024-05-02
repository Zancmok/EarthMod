from enum import Enum
from typing import Any, Optional, Self


type pID = int  # Identification Key


class PlanetProperty(Enum):
    Starting: pID = 0  # The planet you start on
    Toxic: pID = 1  # You need a special suit to not die


class PlanetResource(Enum):
    Water: pID = 0
    Iron: pID = 1
    Copper: pID = 2
    Coal: pID = 3
    CrudeOil: pID = 4
    Ice: pID = 5
    Uranium: pID = 6
    Plutonium: pID = 7


class Planet:
    properties: list[PlanetProperty]  # planets properties
    resources: list[PlanetResource]  # the resources on ground
    prerequisite: Optional[Self]  # the planet that has to be visited beforehand


class Earth(Planet):
    properties = [PlanetProperty.Starting]
    resources = [PlanetResource.Water]
    prerequisite = None


class Mars(Planet):
    properties = []
    resources = [
        PlanetResource.Ice,
        PlanetResource.Iron,
        PlanetResource.Coal,
        PlanetResource.Copper,
        PlanetResource.CrudeOil
    ]
    prerequisite = Earth


class Venus(Planet):
    properties = [PlanetProperty.Toxic]
    resources = [
        PlanetResource.Uranium,
        PlanetResource.Plutonium
    ]
    prerequisite = Mars
