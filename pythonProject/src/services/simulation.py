from src.domain.lfsr import LFSRGenerator


class MonteCarloSimulation:

    def __init__(self, a_percent: float, cost_b: float, cost_c: float, cost_d: float, n_trials: int = 10000):
        self.prob_defect = a_percent / 100.0
        self.cost_b = cost_b
        self.cost_c = cost_c
        self.cost_d = cost_d
        self.n_trials = n_trials

    def run_simulation(self) -> dict:
        """Запускает симуляцию контроля от 0% до 100% с шагом 5%"""
        lfsr = LFSRGenerator()
        results = {"percentages": [], "costs": []}

        min_cost = float('inf')
        optimal_p = 0

        for p_control_int in range(0, 105, 5):
            p_control = p_control_int / 100.0
            total_cost = 0.0

            for _ in range(self.n_trials):
                r1 = lfsr.step()
                r2 = lfsr.step()

                is_controlled = r1 < p_control
                is_defective = r2 < self.prob_defect

                if is_controlled:
                    total_cost += self.cost_b
                    if is_defective:
                        total_cost += self.cost_c
                else:
                    if is_defective:
                        total_cost += self.cost_d

            results["percentages"].append(p_control_int)
            results["costs"].append(total_cost)

            if total_cost < min_cost:
                min_cost = total_cost
                optimal_p = p_control_int

        results["optimal_percent"] = optimal_p
        results["min_cost"] = min_cost

        return results