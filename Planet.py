class Planet:
    def __init__(
        self,
        planetName: str,
        hostStar: str = None,
        planetDistanceParsecs: float = None,
        planetDistanceBanana: float = None,
        planetOrbitalPeriodDays: float = None
    ):
        self.PlanetName = planetName
        self.HostStar = hostStar
        self.PlanetDistanceParsecs = planetDistanceParsecs
        self.PlanetDistanceBanana = planetDistanceBanana
        self.PlanetOrbitalPeriodDays = planetOrbitalPeriodDays