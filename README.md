# TaskFlow

Gestor de tareas en Python · Proyecto integrador DevOps & Project Management.

**Repositorio:** https://github.com/TU_USUARIO/taskflow  
**Sitio:** https://TU_USUARIO.github.io/taskflow/  
**Jira:** (agregar enlace del proyecto real)

> Sustituir `TU_USUARIO` por tu identificador de GitHub. Las URLs y métricas de Jira son pendientes hasta configurarlas.

## Funcionalidades
- TF-4: agregar, listar y completar tareas con prioridad.
- TF-5: eliminar por ID.
- TF-8: filtrar por prioridad.
- TF-9: buscar por texto sin distinguir mayúsculas.
- TF-10: resumen de avance (total, completadas, pendientes y porcentaje).
- TF-11: rechazar títulos duplicados ignorando mayúsculas y espacios extremos.

## Cómo ejecutarlo y probarlo
```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python -m taskflow
```

Los datos residen en memoria; al cerrar la terminal se pierden. Persistencia JSON (TF-14) está fuera del alcance básico.

## GitHub Flow
- Rama por ticket: `feature/TF-8-filtro`, `fix/TF-11-duplicados`.
- Conventional Commits con clave Jira: `feat: TF-8 filtrar tareas por prioridad`.
- Abrir Pull Request y usar la plantilla; revisión y squash merge en `main`.
- Configurar ruleset de protección de `main` en GitHub después de ver los checks.

## CI/CD
- `.github/workflows/ci.yml` ejecuta Pytest en Python 3.11, 3.12 y 3.13 por cada PR y push a main.
- `.github/workflows/deploy.yml` ejecuta las pruebas y solo después publica `docs/` en GitHub Pages.
- En Settings → Pages, elegir **GitHub Actions** como origen de publicación.

## Gestión ágil
- 3 épicas: Gestión de tareas, Calidad y automatización, Visibilidad del proyecto.
- Sprint 0: TF-4 a TF-7. Sprint 1: TF-8 a TF-11.
- Sprint Goal sugerido: «Encontrar tareas rápido y conocer el avance».
- Los identificadores TF-n dependen de cómo se creen los tickets reales en Jira.
- Adjuntar aquí enlaces reales a backlog, burndown, sprint report, revisiones y velocity.

## Equipo
- (Completar nombre(s) y perfiles GitHub)

## Evidencias
- (Añadir URLs de Pull Requests reales, idealmente al menos 6)
- Capturas: `docs/evidencias/`

## Retrospectiva del Sprint 1
| Mantener | Mejorar | Acción (clave Jira) |
|---|---|---|
| (por completar) | (por completar) | (por completar) |

## Lecciones aprendidas
(Completar con experiencias reales del sprint, las revisiones y los pipelines.)
