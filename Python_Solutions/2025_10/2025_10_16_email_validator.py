import re

def validate(email):
    regex = "^([a-zA-Z0-9_\-]+\.)*[a-zA-Z0-9_-]+@([^@\s.]+\.)+[a-zA-Z]{2,}$"

    return bool(re.match(regex, email))

# print(validate("a@b.cd"))
# print(validate("hell.-w.rld@example.com"))
# print(validate(".b@sh.rc"))
# print(validate("example@test.c0"))
# print(validate("freecodecamp.org"))
# print(validate("develop.ment_user@c0D!NG.R.CKS"))
# print(validate("hello.@wo.rld"))
# print(validate("hello@world..com"))
# print(validate("git@commit@push.io"))