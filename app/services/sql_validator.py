class SQLValidator:
    FORBIDDEN = {"DROP", "DELETE", "UPDATE", "ALTER", "TRUNCATE", "INSERT"}

    def validate(self, query: str) -> tuple[bool, str]:
        q = query.strip().upper()

        if not q.startswith("SELECT"):
            return False, "Only SELECT queries are allowed"

        if any(word in q for word in self.FORBIDDEN):
            return False, "Forbidden SQL keyword detected"

        if ";" in q[:-1]:
            return False, "Multiple statements not allowed"

        return True, "Valid"
