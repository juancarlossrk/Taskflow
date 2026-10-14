import pytest
from taskflow import GestorTareas


@pytest.fixture
def gestor():
    return GestorTareas()


def test_lista_vacia(gestor):
    assert gestor.listar() == []


def test_agrega_tarea(gestor):
    assert gestor.agregar("Demo").titulo == "Demo"


def test_id_incremental(gestor):
    assert (gestor.agregar("A").id, gestor.agregar("B").id) == (1, 2)


def test_prioridad_predeterminada(gestor):
    assert gestor.agregar("A").prioridad == "media"


def test_prioridad_alta(gestor):
    assert gestor.agregar("A", "alta").prioridad == "alta"


def test_rechaza_prioridad_invalida(gestor):
    with pytest.raises(ValueError):
        gestor.agregar("A", "urgente")


def test_rechaza_titulo_vacio(gestor):
    with pytest.raises(ValueError):
        gestor.agregar(" ")


def test_completar(gestor):
    tarea = gestor.agregar("A")
    gestor.completar(tarea.id)
    assert gestor.listar()[0].completada


def test_completar_id_inexistente(gestor):
    with pytest.raises(ValueError):
        gestor.completar(99)


def test_eliminar(gestor):
    tarea = gestor.agregar("A")
    gestor.eliminar(tarea.id)
    assert not gestor.listar()


def test_eliminar_id_inexistente(gestor):
    with pytest.raises(ValueError):
        gestor.eliminar(100)


def test_filtro_prioridad(gestor):
    gestor.agregar("A", "alta")
    gestor.agregar("B", "baja")
    assert [t.titulo for t in gestor.filtrar_prioridad("alta")] == ["A"]


def test_filtro_prioridad_insensible_a_mayusculas(gestor):
    gestor.agregar("A", "alta")
    assert len(gestor.filtrar_prioridad(" ALTA ")) == 1


def test_filtro_prioridad_invalida(gestor):
    with pytest.raises(ValueError):
        gestor.filtrar_prioridad("urgente")


def test_buscar_parcial_insensible_a_mayusculas(gestor):
    gestor.agregar("Escribir README")
    gestor.agregar("Preparar demo")
    assert [t.titulo for t in gestor.buscar("readme")] == ["Escribir README"]


def test_buscar_sin_resultados(gestor):
    gestor.agregar("Escribir README")
    assert gestor.buscar("xyz") == []


def test_buscar_texto_vacio(gestor):
    with pytest.raises(ValueError):
        gestor.buscar("  ")


def test_resumen_vacio(gestor):
    assert gestor.resumen() == {"total": 0, "completadas": 0, "pendientes": 0, "avance": 0}


def test_resumen_mitad_completadas(gestor):
    a = gestor.agregar("A")
    gestor.agregar("B")
    gestor.completar(a.id)
    assert gestor.resumen() == {"total": 2, "completadas": 1, "pendientes": 1, "avance": 50}


def test_resumen_totalmente_completado(gestor):
    a = gestor.agregar("A")
    gestor.completar(a.id)
    assert gestor.resumen()["avance"] == 100


def test_duplicado_mismo_titulo(gestor):
    gestor.agregar("Preparar demo")
    with pytest.raises(ValueError):
        gestor.agregar("Preparar demo")


def test_duplicado_ignora_mayusculas_y_espacios(gestor):
    gestor.agregar("Preparar demo")
    with pytest.raises(ValueError):
        gestor.agregar("  preparar DEMO  ")


def test_titulo_recorta_espacios(gestor):
    assert gestor.agregar("  Demo  ").titulo == "Demo"


def test_no_reutiliza_id_tras_eliminar(gestor):
    a = gestor.agregar("A")
    gestor.eliminar(a.id)
    assert gestor.agregar("B").id == 2
