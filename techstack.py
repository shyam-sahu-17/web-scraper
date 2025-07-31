# techstack.py
def detect_tech_stack(html):
    stack = []
    if "wp-content" in html:
        stack.append("WordPress")
    if "react" in html.lower():
        stack.append("React")
    if "vue" in html.lower():
        stack.append("Vue.js")
    if "django" in html.lower():
        stack.append("Django")
    return stack
