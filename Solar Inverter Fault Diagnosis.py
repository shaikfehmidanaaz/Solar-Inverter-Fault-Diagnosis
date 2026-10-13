
# Solar Inverter Fault Diagnosis System
# Educational simulation for EEE students

def diagnose_inverter(dc_voltage, ac_voltage, temperature,
                      grid_voltage, status):

    faults = []

    # Check inverter status
    if status.lower() != "on":
        faults.append("Inverter is OFF or not operating")

    # Check DC input voltage
    if dc_voltage < 100:
        faults.append("Low DC input voltage")
    elif dc_voltage > 500:
        faults.append("High DC input voltage")

    # Check AC output voltage
    if ac_voltage < 200:
        faults.append("Low AC output voltage")
    elif ac_voltage > 250:
        faults.append("High AC output voltage")

    # Check grid voltage
    if grid_voltage < 200:
        faults.append("Grid under-voltage")
    elif grid_voltage > 250:
        faults.append("Grid over-voltage")

    # Check temperature
    if temperature >= 80:
        faults.append("Over-temperature fault")
    elif temperature >= 65:
        faults.append("Warning: Inverter temperature is high")

    # Display diagnosis
    print("\n===== SOLAR INVERTER DIAGNOSIS =====")

    if not faults:
        print("Status: Normal operation")
        print("No abnormal condition detected by these checks.")
    else:
        print("Status: Possible fault detected")
        for fault in faults:
            print("-", fault)

    print("\n===== SUGGESTED ACTIONS =====")

    if not faults:
        print("Continue monitoring inverter readings.")
    else:
        for fault in faults:
            if "DC input" in fault:
                print("- Check PV panels, DC cables, and connectors.")
            elif "AC output" in fault:
                print("- Check inverter output and AC protection.")
            elif "Grid" in fault:
                print("- Check grid supply and inverter grid settings.")
            elif "temperature" in fault.lower():
                print("- Check cooling, ventilation, and cooling fans.")
            elif "OFF" in fault:
                print("- Check alarms, supply, and inverter status.")

    print("\nNote: This is a simplified educational diagnosis.")


def main():
    print("SOLAR INVERTER FAULT DIAGNOSIS SYSTEM")
    print("-------------------------------------")

    try:
        dc_voltage = float(input("Enter DC input voltage (V): "))
        ac_voltage = float(input("Enter AC output voltage (V): "))
        temperature = float(input("Enter inverter temperature (°C): "))
        grid_voltage = float(input("Enter grid voltage (V): "))
        status = input("Enter inverter status (ON/OFF): ").strip()

        if min(dc_voltage, ac_voltage, temperature, grid_voltage) < 0:
            print("Error: Measurements cannot be negative.")
            return

        if status.lower() not in ("on", "off"):
            print("Error: Status must be ON or OFF.")
            return

        diagnose_inverter(
            dc_voltage,
            ac_voltage,
            temperature,
            grid_voltage,
            status
        )

    except ValueError:
        print("Error: Please enter valid numeric measurements.")


if __name__ == "__main__":
    main()
