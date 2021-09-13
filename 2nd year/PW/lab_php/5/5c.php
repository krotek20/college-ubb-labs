<?php

    session_start();

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "labphp";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if (isset($_POST["id"]) && isset($_POST["username"])) {
        $id = addslashes(htmlentities($_POST["id"], ENT_COMPAT, "UTF-8"));
        $username = addslashes(htmlentities($_POST["username"], ENT_COMPAT, "UTF-8"));

        if($username == "" || strlen($username) > 255) {
            header("Location: 5.html");
            exit();
        }
        
        $sql = "DELETE FROM Imagini WHERE id = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("i", $id);
        $stmt->execute();

        header("Location: 5b.php?user=$username");
        exit();
    }

?>