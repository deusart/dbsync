from tests.engine_tests import run_dbengine_test
import connections
pgsql = connections.test_pgsql
mssql = connections.test_mssql

run_dbengine_test(pgsql)
run_dbengine_test(mssql)