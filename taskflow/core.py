"""Dominio de TaskFlow: gestor de tareas en memoria."""
from dataclasses import dataclass

PRIORIDADES = ("alta", "media", "baja")


@dataclass
class Tarea:
    id: int
    titulo: str
    prioridad: str = "media"
    completada: bool = False


class GestorTareas:
    def __init__(self):
        self._tareas: list[Tarea] = []
        self._siguiente_id = 1

    def agregar(self, titulo: str, prioridad: str = "media") -> Tarea:
        if not isinstance(titulo, str) or not titulo.strip():
            raise ValueError("El título no puede estar vacío")
        if not isinstance(prioridad, str) or prioridad.lower().strip() not in PRIORIDADES:
            raise ValueError("Prioridad inválida: alta, media o baja")
        normalizado = titulo.strip().casefold()
        if any(t.titulo.casefold() == normalizado for t in self._tareas):
            raise ValueError("Ya existe una tarea con ese título")
        tarea = Tarea(self._siguiente_id, titulo.strip(), prioridad.lower().strip())
        self._siguiente_id += 1
        self._tareas.append(tarea)
        return tarea

    def listar(self) -> list[Tarea]:
        return list(self._tareas)

    def _obtener(self, id_tarea: int) -> Tarea:
        for tarea in self._tareas:
            if tarea.id == id_tarea:
                return tarea
        raise ValueError(f"No existe la tarea {id_tarea}")

    def completar(self, id_tarea: int) -> Tarea:
        tarea = self._obtener(id_tarea)
        tarea.completada = True
        return tarea

    def eliminar(self, id_tarea: int) -> None:
        self._tareas.remove(self._obtener(id_tarea))

    def filtrar_prioridad(self, prioridad: str) -> list[Tarea]:
        if not isinstance(prioridad, str) or prioridad.lower().strip() not in PRIORIDADES:
            raise ValueError("Prioridad inválida")
        return [t for t in self._tareas if t.prioridad == prioridad.lower().strip()]

    def buscar(self, texto: str) -> list[Tarea]:
        if not isinstance(texto, str) or not texto.strip():
            raise ValueError("Escribe un texto para buscar")
        consulta = texto.strip().casefold()
        return [t for t in self._tareas if consulta in t.titulo.casefold()]

    def resumen(self) -> dict[str, int]:
        total = len(self._tareas)
        completadas = sum(t.completada for t in self._tareas)
        return {"total": total, "completadas": completadas,
                "pendientes": total - completadas,
                "avance": round(completadas * 100 / total) if total else 0}
