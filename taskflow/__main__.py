"""Interfaz sencilla de consola: python -m taskflow."""
from .core import GestorTareas


def main():
    gestor = GestorTareas()
    opciones = "\n1 Agregar  2 Listar  3 Completar  4 Eliminar  5 Filtrar  6 Buscar  7 Resumen  0 Salir"
    while True:
        print(opciones)
        opcion = input("> ").strip()
        if opcion == "0":
            break
        try:
            if opcion == "1":
                t = gestor.agregar(input("Título: "), input("Prioridad [alta/media/baja]: ") or "media")
                print(f"Creada tarea #{t.id}")
            elif opcion == "2":
                mostrar(gestor.listar())
            elif opcion == "3":
                gestor.completar(int(input("ID: ")))
                print("Tarea completada")
            elif opcion == "4":
                gestor.eliminar(int(input("ID: ")))
                print("Tarea eliminada")
            elif opcion == "5":
                mostrar(gestor.filtrar_prioridad(input("Prioridad: ")))
            elif opcion == "6":
                mostrar(gestor.buscar(input("Texto: ")))
            elif opcion == "7":
                print(gestor.resumen())
            else:
                print("Opción no válida")
        except ValueError as exc:
            print(f"Error: {exc}")


def mostrar(tareas):
    if not tareas:
        print("No hay tareas")
    for t in tareas:
        print(f"#{t.id} [{'x' if t.completada else ' '}] {t.titulo} ({t.prioridad})")


if __name__ == "__main__":
    main()
