class ProfileFlyweight:
    _profiles = {}

    @classmethod
    def get_profile(cls, name):
        if name not in cls._profiles:
            cls._profiles[name] = {"brightness": 70, "temperature": 22}
        return cls._profiles[name]