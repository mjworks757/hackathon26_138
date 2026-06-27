import keyring

keyring.set_password("StudentEvaluationReport_app", "sender_email",    "<Paste Here>")
keyring.set_password("StudentEvaluationReport_app", "sender_password", "<Paste Here>")

print("Credentials saved to Windows Credential Manager!")