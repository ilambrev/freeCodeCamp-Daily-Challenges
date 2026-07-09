def triage_issue(title, labels):
    title_words = title.lower().split()

    if not labels:
        if "error" in title_words or "bug" in title_words:
            labels += ["bug", "needs triage"]

        if "feature" in title_words or "add" in title_words:
            labels += ["enhancement", "discussing"]
    else:
        is_help_wanted = False

        if "needs triage" in labels:
            if "simple" in title_words or "easy" in title_words:
                labels.remove("needs triage")
                labels.append("good first issue")
            else:
                labels.remove("needs triage")
                is_help_wanted = True

        if "discussing" in labels:
            if "planned" in title_words or "next" in title_words:
                labels.remove("discussing")
                labels.append("on the roadmap")
            else:
                labels.remove("discussing")
                is_help_wanted = True

        if is_help_wanted:
            labels.append("help wanted")

    if "security" in title_words:
        labels.append("critical")

    return labels

# print(triage_issue("app crashes with error", []))
# print(triage_issue("app crashes with error", ["bug", "needs triage"]))
# print(triage_issue("add dark mode", []))
# print(triage_issue("add dark mode", ["enhancement", "discussing"]))
# print(triage_issue("xss security bug", []))
# print(triage_issue("security vulnerability in auth", []))
# print(triage_issue("easy a11y fix", ["bug", "needs triage"]))
# print(triage_issue("planned api migration", ["enhancement", "discussing"]))
# print(triage_issue("improve security", ["enhancement", "discussing"]))