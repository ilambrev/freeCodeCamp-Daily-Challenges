def sort(emails):
    email_parts = [email.split("@") for email in emails]
    sorted_email_parts = sorted(email_parts, key = lambda x: (x[1].lower(), x[0].lower()))
    
    return ["@".join(mail_parts) for mail_parts in sorted_email_parts]

# print(sort(["jill@mail.com", "john@example.com", "jane@example.com"]))
# print(sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"]))
# print(sort(["user@z.com", "user@y.com", "user@x.com"]))
# print(sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]))
# print(sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"]))