from ..services.teacher_service import TeacherService

class TeacherMenu:

    def __init__(self):
        self.service = TeacherService()

    def run(self):

        while True:

            print("\n===== PROFESORES =====")
            print("1. Agregar")
            print("2. Ver todos")
            print("3. Buscar")
            print("4. Eliminar")
            print("0. Salir")

            option = input("Opción: ")

            if option == "1":

                name = input("Nombre: ")
                specialty = input("Especialidad: ")
                email = input("Email: ")

                self.service.add_teacher(
                    name,
                    specialty,
                    email
                )

            elif option == "2":

                teachers = self.service.get_all_teachers()

                for teacher in teachers:
                    print(teacher)

            elif option == "3":

                teacher_id = int(input("ID: "))

                teacher = self.service.get_teacher_by_id(
                    teacher_id
                )

                print(teacher)

            elif option == "4":

                teacher_id = int(input("ID: "))

                self.service.delete_teacher(
                    teacher_id
                )

            elif option == "0":
                break