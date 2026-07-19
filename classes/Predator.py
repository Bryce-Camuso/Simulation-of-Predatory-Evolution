from Animal import Animal


class Predator(Animal):

    def __init__(self, huntingStrategy, evolutionChance, speed, stealth, stamina, sense, position):
        self._huntingStrategy = huntingStrategy
        self._evolutionChance = evolutionChance
        super().__init__(speed, stealth, stamina, sense, position)

    

    # Getters
    def get_hunting_strategy(self):
        return self._huntingStrategy
    
    def get_evolution_chance(self):
        return self._evolutionChance
    

    # Setters
    def set_evolution_chance(self, newEvolutionChance):
        if newEvolutionChance < 0:
            raise ValueError("Evolution Chance can not be less then 0")
        self._evolutionChance = newEvolutionChance
    
    # Helper functions


    # Methods
