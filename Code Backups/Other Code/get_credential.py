import keyring

email    = keyring.get_password("StudentEvaluationReport_app", "sender_email")
password = keyring.get_password("StudentEvaluationReport_app", "sender_password")

print(f"Email    : {email}")
print(f"Password : {password}")  # check it matches your app password