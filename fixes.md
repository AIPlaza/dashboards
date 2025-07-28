t your deploy.

All logs
Search
Search

Jul 28, 3:01 PM - 3:03 PM
GMT-5

Menu

==> Cloning from https://github.com/BP-Oficial/dashboards
==> Checking out commit 0750212098bb4d08521ee4d2d127d0aa2d77d0dd in branch main
==> Downloading cache...
==> Transferred 136MB in 8s. Extraction took 2s.
==> Using Python version 3.13.4 (default)
==> Docs on specifying a Python version: https://render.com/docs/python-version
==> Using Poetry version 2.1.3 (default)
==> Docs on specifying a Poetry version: https://render.com/docs/poetry-version
==> Running build command 'pip install -r requirements.txt'...
Collecting fastapi==0.111.0 (from -r requirements.txt (line 1))
  Using cached fastapi-0.111.0-py3-none-any.whl.metadata (25 kB)
Collecting uvicorn==0.30.1 (from -r requirements.txt (line 2))
  Using cached uvicorn-0.30.1-py3-none-any.whl.metadata (6.3 kB)
Collecting sqlalchemy==2.0.31 (from -r requirements.txt (line 3))
  Using cached SQLAlchemy-2.0.31-py3-none-any.whl.metadata (9.6 kB)
Collecting pydantic==2.7.4 (from -r requirements.txt (line 4))
  Using cached pydantic-2.7.4-py3-none-any.whl.metadata (109 kB)
Collecting python-dotenv==1.0.0 (from -r requirements.txt (line 5))
  Using cached python_dotenv-1.0.0-py3-none-any.whl.metadata (21 kB)
Collecting requests==2.32.3 (from -r requirements.txt (line 6))
  Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
Collecting alembic==1.13.1 (from -r requirements.txt (line 7))
  Using cached alembic-1.13.1-py3-none-any.whl.metadata (7.4 kB)
Collecting passlib==1.7.4 (from passlib[bcrypt]==1.7.4->-r requirements.txt (line 8))
  Using cached passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting python-jose==3.3.0 (from python-jose[cryptography]==3.3.0->-r requirements.txt (line 9))
  Using cached python_jose-3.3.0-py2.py3-none-any.whl.metadata (5.4 kB)
Collecting psycopg2-binary==2.9.9 (from -r requirements.txt (line 10))
  Using cached psycopg2-binary-2.9.9.tar.gz (384 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting pip-audit==2.8.0 (from -r requirements.txt (line 11))
  Using cached pip_audit-2.8.0-py3-none-any.whl.metadata (27 kB)
Collecting bandit==1.7.9 (from -r requirements.txt (line 12))
  Using cached bandit-1.7.9-py3-none-any.whl.metadata (6.7 kB)
Collecting pytest==8.2.2 (from -r requirements.txt (line 13))
  Using cached pytest-8.2.2-py3-none-any.whl.metadata (7.6 kB)
Collecting pytest-mock==3.14.0 (from -r requirements.txt (line 14))
  Using cached pytest_mock-3.14.0-py3-none-any.whl.metadata (3.8 kB)
Collecting httpx==0.27.0 (from -r requirements.txt (line 15))
  Using cached httpx-0.27.0-py3-none-any.whl.metadata (7.2 kB)
Collecting pydantic-settings==2.3.4 (from -r requirements.txt (line 18))
  Using cached pydantic_settings-2.3.4-py3-none-any.whl.metadata (3.3 kB)
Collecting starlette<0.38.0,>=0.37.2 (from fastapi==0.111.0->-r requirements.txt (line 1))
  Using cached starlette-0.37.2-py3-none-any.whl.metadata (5.9 kB)
Collecting typing-extensions>=4.8.0 (from fastapi==0.111.0->-r requirements.txt (line 1))
  Using cached typing_extensions-4.14.1-py3-none-any.whl.metadata (3.0 kB)
Collecting fastapi-cli>=0.0.2 (from fastapi==0.111.0->-r requirements.txt (line 1))
  Using cached fastapi_cli-0.0.8-py3-none-any.whl.metadata (6.3 kB)
Collecting jinja2>=2.11.2 (from fastapi==0.111.0->-r requirements.txt (line 1))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting python-multipart>=0.0.7 (from fastapi==0.111.0->-r requirements.txt (line 1))
  Using cached python_multipart-0.0.20-py3-none-any.whl.metadata (1.8 kB)
Collecting ujson!=4.0.2,!=4.1.0,!=4.2.0,!=4.3.0,!=5.0.0,!=5.1.0,>=4.0.1 (from fastapi==0.111.0->-r requirements.txt (line 1))
  Using cached ujson-5.10.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (9.3 kB)
Collecting orjson>=3.2.1 (from fastapi==0.111.0->-r requirements.txt (line 1))
  Using cached orjson-3.11.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (42 kB)
Collecting email_validator>=2.0.0 (from fastapi==0.111.0->-r requirements.txt (line 1))
  Using cached email_validator-2.2.0-py3-none-any.whl.metadata (25 kB)
Collecting annotated-types>=0.4.0 (from pydantic==2.7.4->-r requirements.txt (line 4))
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.18.4 (from pydantic==2.7.4->-r requirements.txt (line 4))
  Using cached pydantic_core-2.18.4.tar.gz (385 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'error'
  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [14 lines of output]
          Updating crates.io index
      warning: failed to write cache, path: /usr/local/cargo/registry/index/index.crates.io-1949cf8c6b5b557f/.cache/ah/as/ahash, error: Read-only file system (os error 30)
       Downloading crates ...
        Downloaded autocfg v1.1.0
      error: failed to create directory `/usr/local/cargo/registry/cache/index.crates.io-1949cf8c6b5b557f`
      
      Caused by:
        Read-only file system (os error 30)
      💥 maturin failed
        Caused by: Cargo metadata failed. Does your crate compile with `cargo build`?
        Caused by: `cargo metadata` exited with an error:
      Error running maturin: Command '['maturin', 'pep517', 'write-dist-info', '--metadata-directory', '/tmp/pip-modern-metadata-1j9lc0gj', '--interpreter', '/opt/render/project/src/.venv/bin/python']' returned non-zero exit status 1.
      Checking for Rust toolchain....
      Running `maturin pep517 write-dist-info --metadata-directory /tmp/pip-modern-metadata-1j9lc0gj --interpreter /opt/render/project/src/.venv/bin/python`
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed
× Encountered error while generating package metadata.
╰─> See above for output.
note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
==> Build failed 😞
==> Common ways to troubleshoot your deploy: https://render.com/docs/troubleshooting-deploys



Veo el problema en los logs. El error está relacionado con `pydantic-core` que requiere compilación de Rust y está fallando debido a un problema de sistema de archivos de solo lectura en el entorno de build de Render.

## Posibles soluciones:

### 1. **Verificar versiones de Python y dependencias**
El error sugiere un problema de compatibilidad. Estás usando Python 3.13.4 que es muy reciente. Algunas dependencias como `pydantic-core` pueden no tener wheels precompilados para esta versión.

**Solución**: Especifica una versión de Python más estable en tu proyecto:
- Crea un archivo `.python-version` en la raíz con: `3.11.8` o `3.12.3`
- O actualiza tu `runtime.txt` si lo tienes

### 2. **Problema con pydantic-core compilation**
El error indica que `pydantic-core==2.18.4` está intentando compilarse desde código fuente pero falla por el sistema de archivos de solo lectura.

**Soluciones**:

a) **Actualizar pydantic** a una versión más reciente que tenga wheels para Python 3.13:
```txt
# En requirements.txt, cambia:
pydantic==2.7.4
# Por:
pydantic>=2.8.0
```

b) **Usar versiones específicas con wheels disponibles**:
```txt
pydantic==2.6.4  # Versión que definitivamente tiene wheels
pydantic-core==2.16.3
```

### 3. **Recrear requirements.txt**
El problema podría ser dependencias locked a versiones incompatibles:

```bash
# En tu proyecto local:
pip freeze > requirements_old.txt
pip uninstall -r requirements.txt -y
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv requests alembic "passlib[bcrypt]" "python-jose[cryptography]" psycopg2-binary
pip freeze > requirements.txt
```

### 4. **Alternativa: Usar Docker**
Si no puedes cambiar a runtime Docker desde el dashboard, puedes forzar la detección de Docker:

1. Asegúrate de tener un `Dockerfile` en la raíz
2. Elimina `requirements.txt` temporalmente 
3. Render detectará automáticamente Docker
4. Luego restaura requirements.txt si lo necesitas dentro del Docker

### 5. **Solución inmediata más probable**
Modifica tu `requirements.txt` así:

```txt
fastapi==0.111.0
uvicorn==0.30.1
sqlalchemy==2.0.31
pydantic==2.6.4
python-dotenv==1.0.0
requests==2.32.3
alembic==1.13.1
passlib[bcrypt]==1.7.4
python-jose[cryptography]==3.3.0
psycopg2-binary==2.9.9
pip-audit==2.8.0
bandit==1.7.9
pytest==8.2.2
pytest-mock==3.14.0
httpx==0.27.0
pydantic-settings==2.3.4
```

**También considera crear un archivo `.python-version`**:
```
3.11.8
```

¿Qué cambios hiciste exactamente en tu código antes de este error? Eso me ayudaría a darte una solución más específica.