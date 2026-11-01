from dataclasses import dataclass
from typing import List, Optional, Literal

@dataclass
class MiniRackUPSCandidate:
    """
    Models a 1U Mini Rack UPS as described in the Issue Body.
    Focuses on AC outlets, Li-Ion integration, and power headroom.
    """
    name: str
    max_input_watts: float
    battery_ah: float
    nominal_voltage: float = 20.5  # Typical for 20V-24V DC inputs in this form factor
    ac_outlets: int = 1
    depth_inches: float = 10.0     # The "10"" depth mentioned in title
    efficiency: float = 0.90

    def get_total_energy_wh(self) -> float:
        return self.battery_ah * self.nominal_voltage

    def get_run_time_hours(self, load_watts: float) -> float:
        return self.get_total_energy_wh() * self.efficiency / load_watts


@dataclass
class RackLoadProfile:
    """
    Models the PoE Pi Rack setup described in the Issue Body.
    Handles idle vs peak consumption for accurate runtime.
    """
    device_name: str
    idle_watts: float
    peak_watts: float
    spike_factor: float = 1.15     # Buffer for PoE negotiation spikes

    def get_effective_load(self) -> float:
        # Estimate a "typical" load between idle and peak
        return self.idle_watts + ((self.peak_watts - self.idle_watts) * 0.6)

    def get_peak_load(self) -> float:
        return self.peak_watts * self.spike_factor


def analyze_mini_rack_ups(candidates: List[MiniRackUPSCandidate], load: RackLoadProfile) -> Optional[MiniRackUPSCandidate]:
    """
    Evaluates a list of UPS candidates against the specific Rack Load.
    Returns the candidate that balances power headroom with capacity.
    """
    if not candidates:
        return None

    # Find candidate with the best wattage-to-capacity ratio relative to the load
    best_fit = max(candidates, key=lambda x: x.get_total_energy_wh() / x.max_input_watts)
    return best_fit


if __name__ == "__main__":
    # Instantiate the specific ZeroKor from the Issue Body
    # Specs: ZeroKor Portable Power Bank with AC Outlet - 65W / 24 Ah
    zero_kor = MiniRackUPSCandidate(
        name="ZeroKor",
        max_input_watts=65.0,
        battery_ah=24.0,
        nominal_voltage=20.5,
        ac_outlets=1,
        depth_inches=10.0,
        efficiency=0.90
    )

    # Instantiate the PoE Pi Rack Load
    # Specs: 17W at idle, 40-50W max
    pi_rack = RackLoadProfile(
        device_name="PoE Pi Rack",
        idle_watts=17.0,
        peak_watts=50.0,
        spike_factor=1.2
    )

    print("--- Mini Rack UPS Analysis Report ---")
    print(f"Candidate: {zero_kor.name}")
    print(f"Form Factor: {zero_kor.depth_inches}\" Depth / 1U Height")
    print(f"Input Power Limit: {zero_kor.max_input_watts}W")
    print(f"Total Battery Energy: {zero_kor.get_total_energy_wh():.1f}Wh")
    print()

    # Simulate Runtime at Peak Load
    effective_load = pi_rack.get_peak_load()
    run_time = zero_kor.get_run_time_hours(effective_load)

    print(f"Target Load (Peak + Spikes): {effective_load:.1f}W")
    print(f"Estimated Run Time: {run_time:.2f} Hours")
    print()

    # Check Power Headroom (Critical for AC vs PoE conversion)
    headroom = zero_kor.max_input_watts - effective_load
    print(f"Power Headroom: {headroom:.1f}W")

    # Determine Status
    if headroom > 15.0:
        status = "OPTIMAL"
    elif headroom > 5.0:
        status = "ADEQUATE"
    else:
        status = "TIGHT"

    print(f"Compatibility Status: {status}")
    print("---")