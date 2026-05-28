import os

def fix_file(path, old, new):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")
    else:
        print(f"Target string not found in {path}")

# DataController
dc_path = 'roco-data/src/main/java/com/roco/data/controller/DataController.java'
fix_file(dc_path, 'source == 0 ? "自学" : source == 1 ? "技能石" : source == 2 ? "血脉" : "特性"', 'source == 0 ? "自学" : source == 1 ? "技能石" : source == 2 ? "血脉" : source == 4 ? "传说技能" : "特性"')

# PetSkillMapping
pm_path = 'roco-data/src/main/java/com/roco/data/model/entity/PetSkillMapping.java'
fix_file(pm_path, 'case 2: return "血脉";', 'case 2: return "血脉";\n            case 4: return "传说技能";')

print('Backend Java files updated successfully.')
