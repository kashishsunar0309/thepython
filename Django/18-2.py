def __str__(self):
    if len(self.text)>50:
        return f"{self.text[:50]}...."
    else:
        return self.text