<?php 

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "labajax";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "SHOW TABLES FROM labajax like '%s'";
    $statement = $conn->prepare($sql);

    $statement->execute();
    $statement->bind_result($table);

    $tables = array();
    while ($statement->fetch()) {
        array_push($tables, $table);
    }
    $allTables = new StdClass();
    $allTables->tables = $tables;

    echo json_encode($allTables);
    $statement->close();
    $conn->close();

?>