import pyodbc
import Selenium.Utilities.Logger as ml

class DatabaseConnection():
    """
    DatabaseCursor class stores all methods, that can be used to get/insert some data from/into database.
    Also the cursor to support a database operations is being created here.
    """

    # Create logger object
    logs = ml.MESlogger()

    # Create database cursor
    try:
        conn = pyodbc.connect(r"Driver={SQL Server Native Client 11.0};"
                              r"Server=krksql3\sql2012;"
                              r"Database=KRKPMIVAL35;"
                              r"Trusted_Connection=yes;", autocommit=True)

        cursor = conn.cursor()
        logs.info("Database cursor has been created. Connection to database set")
    except Exception as ex:
        logs.error("Database cursor creating has been failed.\nException occured" + str(ex))

    def select(self, query, *parameters):
        """
        select is base class in order to executing select operations from database
        """
        try:
            # For each given parameter, replace it with '@@@parameter@@@' in received query
            for parameter in parameters:
                query = query.replace('@@@parameter@@@', parameter, 1)

            # Execute query
            self.cursor.execute(query)

            # Check if query has been executed in order to get one or more rows
            if "TOP 1" in query.upper():
                rows = self.cursor.fetchone()
            else:
                rows = self.cursor.fetchall()

            if rows == None:
                self.logs.warning("No record has been received from database (select method)")
            else:
                self.logs.info("At least one record has been received from database")

            return rows

        except Exception as ex:
            self.logs.error("select method has been failed\nException occured: " + str(ex))