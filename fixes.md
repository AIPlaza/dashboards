(.venv) PS C:\Users\DELL\P2P-Dashboard> uvicorn p2p_api.main:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Users\\DELL\\P2P-Dashboard']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12004] using WatchFiles
INFO:     Started server process [16512]
INFO:     Waiting for application startup.
2025-07-11 01:30:52,442 - p2p_api.main - INFO - Starting P2P Dashboard API...
INFO:     Application startup complete.
INFO:     127.0.0.1:58045 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:58065 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:58065 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:58150 - "POST /admin/users/ HTTP/1.1" 500 Internal Server Error
ERROR:    Exception in ASGI application
Traceback (most recent call last):
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: no such table: users

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\uvicorn\protocols\http\httptools_impl.py", line 409, in run_asgi 
    result = await app(  # type: ignore[func-returns-value]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        self.scope, self.receive, self.send
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\uvicorn\middleware\proxy_headers.py", line 60, in __call__       
    return await self.app(scope, receive, send)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\fastapi\applications.py", line 1054, in __call__
    await super().__call__(scope, receive, send)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\applications.py", line 112, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\middleware\errors.py", line 187, in __call__
    raise exc
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\middleware\errors.py", line 165, in __call__
    await self.app(scope, receive, _send)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\middleware\exceptions.py", line 62, in __call__        
    await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app        
    raise exc
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app        
    await app(scope, receive, sender)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\routing.py", line 714, in __call__
    await self.middleware_stack(scope, receive, send)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\routing.py", line 734, in app
    await route.handle(scope, receive, send)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\routing.py", line 288, in handle
    await self.app(scope, receive, send)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\routing.py", line 76, in app
    await wrap_app_handling_exceptions(app, request)(scope, receive, send)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\_exception_handler.py", line 53, in wrapped_app        
    raise exc
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\_exception_handler.py", line 42, in wrapped_app        
    await app(scope, receive, sender)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\starlette\routing.py", line 73, in app
    response = await f(request)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\fastapi\routing.py", line 301, in app
    raw_response = await run_endpoint_function(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\fastapi\routing.py", line 212, in run_endpoint_function
    return await dependant.call(**values)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\P2P-Dashboard\p2p_api\routers\admin.py", line 48, in create_admin_user
    db_user = crud.get_user_by_username(db, username=user.username)
  File "C:\Users\DELL\P2P-Dashboard\p2p_api\crud.py", line 66, in get_user_by_username
    return db.query(models.User).filter(models.User.username == username).first()
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\orm\query.py", line 2759, in first
    return self.limit(1)._iter().first()  # type: ignore
           ~~~~~~~~~~~~~~~~~~~^^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\orm\query.py", line 2857, in _iter
    result: Union[ScalarResult[_T], Result[_T]] = self.session.execute(
                                                  ~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
        params,
        ^^^^^^^
        execution_options={"_sa_orm_load_options": self.load_options},
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 2365, in execute
    return self._execute_internal(
           ~~~~~~~~~~~~~~~~~~~~~~^
        statement,
        ^^^^^^^^^^
    ...<4 lines>...
        _add_event=_add_event,
        ^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\orm\session.py", line 2251, in _execute_internal      
    result: Result[Any] = compile_state_cls.orm_execute_statement(
                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self,
        ^^^^^
    ...<4 lines>...
        conn,
        ^^^^^
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\orm\context.py", line 306, in orm_execute_statement   
    result = conn.execute(
        statement, params or {}, execution_options=execution_options
    )
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1415, in execute
    return meth(
        self,
        distilled_parameters,
        execution_options or NO_OPTIONS,
    )
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\sql\elements.py", line 523, in _execute_on_connection 
    return connection._execute_clauseelement(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        self, distilled_params, execution_options
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1637, in _execute_clauseelement 
    ret = self._execute_context(
        dialect,
    ...<8 lines>...
        cache_hit=cache_hit,
    )
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1842, in _execute_context       
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1982, in _exec_single_context   
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 2351, in _handle_dbapi_exception    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1963, in _exec_single_context   
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 943, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: users
[SQL: SELECT users.id AS users_id, users.username AS users_username, users.hashed_password AS users_hashed_password, users.is_active AS users_is_active
FROM users
WHERE users.username = ?
 LIMIT ? OFFSET ?]
[parameters: ('admin', 1, 0)]
(Background on this error at: https://sqlalche.me/e/20/e3q8)
INFO:     Shutting down
INFO:     Waiting for application shutdown.
2025-07-11 01:32:59,715 - p2p_api.main - INFO - Shutting down P2P Dashboard API...
INFO:     Application shutdown complete.
INFO:     Finished server process [16512]
INFO:     Stopping reloader process [12004]
(.venv) PS C:\Users\DELL\P2P-Dashboard> 




pydantic, playwright, cryptography, anyio, watchfiles, starlette, pydantic-settings, httpx, fastapi

Successfully installed SQLAlchemy-2.0.41 annotated-types-0.7.0 anyio-4.9.0 bcrypt-4.3.0 beautifulsoup4-4.13.4 certifi-2025.7.9 cffi-1.17.1 charset_normalizer-3.4.2 click-8.2.1 cryptography-45.0.5 dnspython-2.7.0 ecdsa-0.19.1 email-validator-2.2.0 exceptiongroup-1.3.0 fastapi-0.116.0 greenlet-3.2.3 h11-0.16.0 httpcore-1.0.9 httptools-0.6.4 httpx-0.28.1 idna-3.10 iniconfig-2.1.0 packaging-25.0 passlib-1.7.4 playwright-1.53.0 pluggy-1.6.0 psycopg2-2.9.10 pyasn1-0.6.1 pycparser-2.22 pydantic-2.11.7 pydantic-core-2.33.2 pydantic-settings-2.10.1 pyee-13.0.0 pygments-2.19.2 pytest-8.4.1 python-dotenv-1.1.1 python-jose-3.5.0 python-multipart-0.0.20 pyyaml-6.0.2 requests-2.32.4 rsa-4.9.1 six-1.17.0 sniffio-1.3.1 soupsieve-2.7 starlette-0.46.2 tomli-2.2.1 typing-extensions-4.14.1 typing-inspection-0.4.1 urllib3-2.5.0 uvicorn-0.35.0 uvloop-0.21.0 watchfiles-1.1.0 websockets-15.0.1
Error: The operation was canceled


test (3.9)
failed 2 minutes ago in 28s
Search logs
1s
0s
0s
23s
1s
Run python -m pytest
ImportError while loading conftest '/home/runner/work/dashboards/dashboards/tests/conftest.py'.
tests/conftest.py:12: in <module>
    from p2p_api.main import app, get_db, get_api_key, configure_database
p2p_api/main.py:11: in <module>
    from . import (
p2p_api/crud.py:4: in <module>
    from . import auth, database as models, schemas
p2p_api/auth.py:11: in <module>
    from . import crud, schemas
p2p_api/schemas.py:87: in <module>
    class TokenData(BaseModel):
p2p_api/schemas.py:88: in TokenData
    username: str | None = None
E   TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'
Error: Process completed with exit code 4.


First Run to try to solve Gemnini answered:

  > check fixes.md and act as a very dilligent software enginner  │
╰──────────────────────────────────────────────────────────────────╯

 ╭───────────────────────╮
 │ ✔  ReadFile fixes.md  │
 ╰───────────────────────╯
✦ The fixes.md file shows a sqlite3.OperationalError: no such table: users when attempting to create an admin
  user. This indicates that the database tables are not being created on application startup.


  My plan is to ensure the database tables are created by calling Base.metadata.create_all(engine) during the
  FastAPI application's lifespan.


  First, I'll modify p2p_api/database.py to expose Base and engine. Then, I'll update p2p_api/main.py to use
  these to create the tables.
 ╭──────────────────────────────────╮
 │ ✔  ReadFile p2p_api\database.py  │
 ╰──────────────────────────────────╯
 ╭────────────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ✔  Edit p2p_api\database.py: Base = declarative_base()... => Base = declarative_base()...              │
 │                                                                                                        │
 │    10                                                                                                  │
 │    11                                                                                                  │
 │    12     Base = declarative_base()                                                                    │
 │    13   + engine = None                                                                                │
 │    14   + SessionLocal = None                                                                          │
 │    15                                                                                                  │
 │    16     def init_db(db_url: str):                                                                    │
 │    17         """Initialize database engine and session factory."""                                    │
 │    18   +     global engine, SessionLocal                                                              │
 │    19         from p2p_api.config import Settings                                                      │
 │    20         effective_url = db_url or Settings().database_url                                        │
 │    21                                                                                                  │
 ╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯
 ╭──────────────────────────────╮
 │ ✔  ReadFile p2p_api\main.py  │
 ╰──────────────────────────────╯
 ╭────────────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ✔  Edit p2p_api\main.py:     if not global_settings.tes... =>     if not global_settings.tes...        │
 │                                                                                                        │
 │    48         configure_database(global_settings.database_url)                                         │
 │    49         # Make the session factory available to the dependency injector                          │
 │    50         set_session_local(_SessionLocal)                                                         │
 │    51   +     # Create database tables                                                                 │
 │    52   +     Base.metadata.create_all(bind=_engine)                                                   │
 │    53     yield                                                                                        │
 │    54                                                                                                  │
 │    55     logger.info("Shutting down P2P Dashboard API...")                                            │
 ╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ I've updated p2p_api/database.py and p2p_api/main.py to ensure database tables are created on startup. I'll now
  run the app to verify the fix.

ℹ Request cancelled.
 
 ╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ -  Shell uvicorn p2p_api.main:app --reload (Running the FastAPI application to verify database table creation.)  │


 and the result

 (.venv) PS C:\Users\DELL\P2P-Dashboard> uvicorn p2p_api.main:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Users\\DELL\\P2P-Dashboard']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [10860] using WatchFiles
Process SpawnProcess-1:
Traceback (most recent call last):
  File "C:\Python313\Lib\multiprocessing\process.py", line 313, in _bootstrap
    self.run()
    ~~~~~~~~^^
  File "C:\Python313\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\uvicorn\_subprocess.py", line 80, in subprocess_started
    target(sockets=sockets)
    ~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\uvicorn\server.py", line 67, in run
    return asyncio.run(self.serve(sockets=sockets))
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python313\Lib\asyncio\runners.py", line 195, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "C:\Python313\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "C:\Python313\Lib\asyncio\base_events.py", line 725, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\uvicorn\server.py", line 71, in serve
    await self._serve(sockets)
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\uvicorn\server.py", line 78, in _serve
    config.load()
    ~~~~~~~~~~~^^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\uvicorn\config.py", line 436, in load
    self.loaded_app = import_from_string(self.app)
                      ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "C:\Users\DELL\P2P-Dashboard\.venv\Lib\site-packages\uvicorn\importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
  File "C:\Python313\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1022, in exec_module
  File "<frozen importlib._bootstrap_external>", line 1160, in get_code
  File "<frozen importlib._bootstrap_external>", line 1090, in source_to_code
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "C:\Users\DELL\P2P-Dashboard\p2p_api\main.py", line 56
    global _engine
    ^^^^^^^^^^^^^^
SyntaxError: name '_engine' is used prior to global declaration


Second Try: (Idea is avoid looping over and over, also not to change core logic and watch for the context to not create conflicts in changes)

╭───────────────────────────────────────────────╮
│  > check fixes.md, i have added last results  │
╰───────────────────────────────────────────────╯

 ╭───────────────────────╮
 │ ✔  ReadFile fixes.md  │
 ╰───────────────────────╯
 ╭────────────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ✔  Edit p2p_api\main.py: @asynccontextmanager... => @asynccontextmanager...                            │
 │                                                                                                        │
 │    40                                                                                                  │
 │    41     @asynccontextmanager                                                                         │
 │    42     async def lifespan(app: FastAPI):                                                            │
 │    43   +     global _engine, _SessionLocal, global_settings                                           │
 │    44         setup_logging()                                                                          │
 │    45         logger.info("Starting P2P Dashboard API...")                                             │
 │    45   -     global global_settings                                                                   │
 │    46         global_settings = Settings()                                                             │
 │    47         if not global_settings.testing:                                                          │
 │    48             configure_database(global_settings.database_url)                                     │
 │    53         yield                                                                                    │
 │    54                                                                                                  │
 │    55         logger.info("Shutting down P2P Dashboard API...")                                        │
 │    56   -     global _engine                                                                           │
 │    56         if not global_settings.testing and _engine:                                              │
 │    57             _engine.dispose()                                                                    │
 │    58                                                                                                  │
 ╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ I've addressed the SyntaxError by correctly declaring _engine and _SessionLocal as global at the start of the
  lifespan function in p2p_api/main.py. I'll now run the application to confirm the fix.
 ╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
 │ ⊷  Shell uvicorn p2p_api.main:app --reload (Running the FastAPI application to verify the fix.)               │
 │                                                                                                               │
 │    ... first 5 lines hidden ...                                                                               │
                             │- p2p_api.main - INFO - Starting P2P Dashboard API...
 │                                                                                   

 The result:

 