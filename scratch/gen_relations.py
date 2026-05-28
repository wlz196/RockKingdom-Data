import sqlite3
import json

def generate_relations():
    conn = sqlite3.connect('/Users/wanglianzuo/project/RockKingdomWorldAssistant/roco_encyclopedia.db')
    conn.row_factory = sqlite3.Row
    
    # Get all types
    types = {r['id']: r['name'].replace('系', '') for r in conn.execute('SELECT id, name FROM types').fetchall()}
    
    # Get all relations
    relations_raw = conn.execute('SELECT * FROM type_relations').fetchall()
    
    # Format relations
    result = []
    for r in relations_raw:
        m = 2.0 if r['multiplier'] == 1 else (0.5 if r['multiplier'] == -1 else 0.0)
        result.append({
            'attacker': types.get(r['attacker_id'], '未知'),
            'defender': types.get(r['defender_id'], '未知'),
            'multiplier': m
        })
    
    # Organize into a more structured format: attacker -> { defender: multiplier }
    structured = {}
    for r in result:
        atk = r['attacker']
        dfd = r['defender']
        mult = r['multiplier']
        if atk not in structured:
            structured[atk] = {}
        structured[atk][dfd] = mult
        
    final_output = {
        "description": "洛克王国属性克制关系表 (1.0: 常规, 2.0: 克制, 0.5: 抵抗, 0.0: 免疫)",
        "types": list(types.values()),
        "matrix": structured
    }
    
    with open('/Users/wanglianzuo/project/RockKingdomWorldAssistant/type_relations.json', 'w', encoding='utf-8') as f:
        json.dump(final_output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate_relations()
