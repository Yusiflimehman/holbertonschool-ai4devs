class Task:
    """A to-do task with an optional list of tags."""

    def __init__(self, title, tags=None):
        self.title = title
        self.tags = list(tags) if tags is not None else []

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __repr__(self):
        return f"Task({self.title!r}, tags={self.tags})"


if __name__ == "__main__":
    task_a = Task("Write report")
    task_b = Task("Buy groceries")

    task_a.add_tag("work")
    task_b.add_tag("personal")

    print(task_a)
    print(task_b)
