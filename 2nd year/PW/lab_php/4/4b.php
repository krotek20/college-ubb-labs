<?php

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "labphp";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if (isset($_GET["key"])) {
        $list = array();
        $input_key = addslashes(htmlentities($_GET["key"], ENT_COMPAT, "UTF-8"));

        $sql_select = "SELECT * FROM confirmari WHERE unique_key = ?";
        $stmt = $conn->prepare($sql_select);
        $stmt->bind_param("s", $input_key);
        $stmt->execute();
        $stmt->bind_result($username, $password, $key);

        if (!$stmt->fetch()) {
            exit();
        }

        $stmt->close();

        $sql_delete = "DELETE FROM confirmari WHERE unique_key = ?";
        $stmt_delete = $conn->prepare($sql_delete);
        $stmt_delete->bind_param("s", $key);
        $exec_delete = $stmt_delete->execute();

        if ($exec_delete == true) {
            $sql_insert = "INSERT INTO utilizatori VALUES (?, ?)";
            $stmt_insert = $conn->prepare($sql_insert);
            $stmt_insert->bind_param("ss", $username, $password);
            $exec_insert = $stmt_insert->execute();

            if ($exec_insert == true) {
                echo "Successful registration!";
            }
        }
    }

?>