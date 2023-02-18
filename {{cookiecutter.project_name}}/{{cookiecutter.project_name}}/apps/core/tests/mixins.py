class ExtraAssertionsMixin:
    def assertContainsAll(self, response, dict):
        for value in dict:
            self.assertContains(response, value)
