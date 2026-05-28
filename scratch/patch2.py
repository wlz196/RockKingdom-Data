import os

path = 'frontend-data/encyclopedia.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Snippets to move
btn_snippet = """                    ${d.skills['传说技能'] && d.skills['传说技能'].length > 0 ? `
                    <button class="tab-link" onclick="switchTab(event, 'skill-legendary')" style="color:#d4af37; font-weight:bold; text-shadow: 0 0 5px rgba(212, 175, 55, 0.5);">
                        <i class="fas fa-crown"></i> <span>传说技能</span>
                    </button>
                    ` : ''}"""

div_snippet = """                ${d.skills['传说技能'] && d.skills['传说技能'].length > 0 ? `
                <div id="skill-legendary" class="tab-content" style="display:none; border: 1px solid #d4af37; border-radius: 8px; box-shadow: inset 0 0 15px rgba(212,175,55,0.1);">${renderSkillsList(d.skills['传说技能'])}</div>
                ` : ''}"""

# Remove them from current locations
content = content.replace('\n' + btn_snippet, '')
content = content.replace('\n' + div_snippet, '')

# Insert after skill-self button
target_btn = """                    <button class="tab-link active" onclick="switchTab(event, 'skill-self')">
                        <i class="fas fa-book"></i> <span>自学</span>
                    </button>"""
content = content.replace(target_btn, target_btn + '\n' + btn_snippet)

# Insert after skill-self content
target_div = """                <div id="skill-self" class="tab-content">${renderSkillsList(d.skills['自学'])}</div>"""
content = content.replace(target_div, target_div + '\n' + div_snippet)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Moved successfully.')
