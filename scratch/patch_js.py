import os

path = 'frontend-data/encyclopedia.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Insert the button
btn_target = """                    <button class="tab-link" onclick="switchTab(event, 'skill-common')">
                        <i class="fas fa-star"></i> <span>常用</span>
                    </button>"""

btn_new = btn_target + """
                    ${d.skills['传说技能'] && d.skills['传说技能'].length > 0 ? `
                    <button class="tab-link" onclick="switchTab(event, 'skill-legendary')" style="color:#d4af37; font-weight:bold; text-shadow: 0 0 5px rgba(212, 175, 55, 0.5);">
                        <i class="fas fa-crown"></i> <span>传说技能</span>
                    </button>
                    ` : ''}"""

content = content.replace(btn_target, btn_new)

# Insert the tab content
div_target = """                <div id="skill-common" class="tab-content" style="display:none">${renderSkillsList(d.skills['常用'] || [])}</div>"""
div_new = div_target + """
                ${d.skills['传说技能'] && d.skills['传说技能'].length > 0 ? `
                <div id="skill-legendary" class="tab-content" style="display:none; border: 1px solid #d4af37; border-radius: 8px; box-shadow: inset 0 0 15px rgba(212,175,55,0.1);">${renderSkillsList(d.skills['传说技能'])}</div>
                ` : ''}"""

content = content.replace(div_target, div_new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated encyclopedia.js")
