from ..models.subject import Subject


class SubjectService:

    def __init__(self):
        self.subjects = []

    def get_next_id(self):

        if not self.subjects:
            return 1

        return max(subject.id for subject in self.subjects) + 1

    # CREATE
    def add_subject(
            self,
            name,
            teacher_id,
            credits,
            description=""
    ):

        new_subject = Subject(
            self.get_next_id(),
            name,
            teacher_id,
            credits,
            description
        )

        self.subjects.append(new_subject)

        return new_subject

    # READ
    def get_all_subjects(self):
        return self.subjects

    def get_subject_by_id(self, subject_id):

        for subject in self.subjects:

            if subject.id == subject_id:
                return subject

        return None

    # DELETE
    def delete_subject(self, subject_id):

        subject = self.get_subject_by_id(subject_id)

        if subject:

            self.subjects.remove(subject)

            return True

        return False