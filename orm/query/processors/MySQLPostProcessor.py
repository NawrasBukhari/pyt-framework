class MySQLPostProcessor:
    """Post processor classes are responsable for modifying the result after a query.

    Post Processors are called after the connection calls the database in the
    Query Builder but before the result is returned in that builder method.

    We can use this oppurtunity to get things like the inserted ID.

    For the SQLite Post Processor we have an attribute on the connection class we can use to fetch the ID.
    """

    def process_insert_get_id(self, builder, results, id_key):
        """Process the results from the query to the database.

        Args:
            builder (orm.builder.QueryBuilder): The query builder class
            results (dict): The result from an insert query or the creates from the query builder.
            This is usually a dictionary.
            id_key (string): The key to set the primary key to. This is usually the primary key of the table.

        Returns:
            dictionary: Should return the modified dictionary.
        """

        if id_key not in results:
            results.update({id_key: builder._connection.get_cursor().lastrowid})
        return results

    def get_column_value(self, builder, column, results, id_key, id_value):
        """Gets the specific column value from a table. Typically done after an update to
        refetch the new value of a field.

            builder (orm.builder.QueryBuilder): The query builder class
            column (string): The column to refetch the value for.
            results (dict): The result from an update query from the query builder.
            This is usually a dictionary.
            id_key (string): The key to fetch the primary key for. This is usually the primary key of the table.
            id_value (string): The value of the primary key to fetch
        """

        new_builder = builder.select(column)
        if id_key and id_value:
            new_builder.where(id_key, id_value)
            return new_builder.first()[column]

        return {}