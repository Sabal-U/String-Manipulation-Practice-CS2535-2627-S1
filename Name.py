# String 1 — Clean a Name

name = "   aLeX mOrGaN   "

name = name.strip()
name = name.title()

print(name)


# String 2 — Clean a Status Message

status = "WARNING::ENGINE_OVERHEAT::SECTOR_7"

status = status.lower()
status = status.replace("::", " | ")
status = status.replace("_", " ")

print(status)


# String 3 — Organize Module Names

modules = "navigation|life_support|cargo_bay|engine_control"

modules = modules.split("|")

for i in range(len(modules)):
    modules[i] = modules[i].replace("_", " ").title()

modules = ",".join(modules)

print(modules)


# String 4 — Process Sensor Readings

readings = "  18,27,35,20  "

readings = readings.strip()
readings = readings.split(",")

readings = [int(value) for value in readings]

total = sum(readings)
average = total / len(readings)

print("Total:", total)
print("Average:", average)