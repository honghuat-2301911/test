"""Module containing the User domain entity."""


class User:
    """Represents a user in the system.

    Attributes:
        user_id: Unique identifier for the user
        name: User's display name
        password: User's password (hashed)
        email: User's email address
        skill_lvl: User's skill level (optional)
        sports_exp: User's sports experience (optional)
        role: User's role (default: 'user')
    """

    def __init__(
        self,
        user_id,
        name,
        password,
        email,
        skill_lvl=None,
        sports_exp=None,
        role="user",
    ):
        self._user_id = user_id
        self._name = name
        self._password = password
        self._email = email
        self._skill_lvl = skill_lvl
        self._sports_exp = sports_exp
        self._role = role

    # Getters with docstrings
    def get_id(self):
        """Get the user's unique identifier."""
        return self._user_id

    def get_name(self):
        """Get the user's display name."""
        return self._name

    def get_password(self):
        """Get the user's password (hashed)."""
        return self._password

    def get_email(self):
        """Get the user's email address."""
        return self._email

    def get_skill_lvl(self):
        """Get the user's skill level."""
        return self._skill_lvl

    def get_sports_exp(self):
        """Get the user's sports experience."""
        return self._sports_exp

    def get_role(self):
        """Get the user's role."""
        return self._role

    # Setters with docstrings
    def set_name(self, name):
        """Set the user's display name.

        Args:
            name: New display name
        """
        self._name = name

    def set_password(self, password):
        """Set the user's password.

        Args:
            password: New password (should be hashed)
        """
        self._password = password

    def set_email(self, email):
        """Set the user's email address.

        Args:
            email: New email address
        """
        self._email = email

    def set_skill_lvl(self, skill_lvl):
        """Set the user's skill level.

        Args:
            skill_lvl: New skill level
        """
        self._skill_lvl = skill_lvl

    def set_sports_exp(self, sports_exp):
        """Set the user's sports experience.

        Args:
            sports_exp: New sports experience
        """
        self._sports_exp = sports_exp

    def set_role(self, role):
        """Set the user's role.

        Args:
            role: New role
        """
        self._role = role
